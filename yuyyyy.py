import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
from folium import FeatureGroup, plugins
from datetime import datetime


def sort_output_table(output, location_df):
    df_in = output[['Location', 'Time_in',]].copy()
    df_in.rename(columns={'Time_in':'Time'}, inplace=True)
    df_out = output[['Location', 'Time_out',]].copy()
    df_out.rename(columns={'Time_out':'Time'}, inplace=True)

    df = pd.concat([df_in, df_out], axis =0).sort_values(by='Time', ascending=True)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    merged_df = df.merge(location_df[['Location', 'Latitude', 'Longitude']], on='Location', how='left')
    df['Latitude'] = merged_df['Latitude']
    df['Longitude'] = merged_df['Longitude']
    return(df)

def move_marker(current_time, df):
    # Find the segment that contains the current time
    for i, row in df[:-1].iterrows():
        if row['Time'] <= current_time <= df.iloc[i + 1]['Time']:
            point_before, point_after = row, df.iloc[i + 1]
            break
    else:
        return None

    # Interpolate between the two points based on time
    time_before = point_before['Time']
    time_after = point_after['Time']

    time_delta = (current_time - time_before) / (time_after - time_before)

    lat = point_before['Latitude'] + (point_after['Latitude'] - point_before['Latitude']) * time_delta
    lng = point_before['Longitude'] + (point_after['Longitude'] - point_before['Longitude']) * time_delta

    return lng, lat

# print(df)

# Define function to create the feature collection
def create_feature_collection(df, time_step):
    features = []

    # create moving marker features
    moving_points = []
    for i, row in df.iterrows():
        if i < len(df) - 1:
            next_row = df.iloc[i + 1]
            time_delta = (next_row['Time'] - row['Time']).total_seconds()
            num_points = int(time_delta / time_step)

            for j in range(num_points + 1):  # Include endpoint by adding 1
                time = row['Time'] + pd.Timedelta(seconds=time_step * j)
                moving_coords = move_marker(time, df)
                if moving_coords:
                    moving_points.append({
                        'coordinates': moving_coords,
                        'time': time.strftime('%Y-%m-%dT%H:%M:%S')
                    })

    moving_feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'MultiPoint',
            'coordinates': [point['coordinates'] for point in moving_points]
        },
        'properties': {
            'times': [point['time'] for point in moving_points],
            'iconstyle': {
                'iconUrl': 'https://example.com/myicon.png',
                'iconSize': [30, 30],
                'iconAnchor': [15, 15],
                'popupAnchor': [0, -15],
                'iconRotate': 45,            
            }
        }
    }

    features.append(moving_feature)

    feature_collection = {"type": "FeatureCollection", "features": features}
    return feature_collection


def main(location_df, output_table):
    # convert timedeltas to datetime
    df = sort_output_table(output_table, location_df)
    
    # Create the map
    m = folium.Map(location=[location_df['Latitude'].mean(), location_df['Longitude'].mean()], zoom_start=10)
           
    # Create the feature group and add it to the map
    fg = FeatureGroup(name="Marker Locations")

    # Create the feature collection
    feature_collection = create_feature_collection(df, 5)  # time_step = 1 second
    
    # Create the TimestampedGeoJson layer with custom styling
    timestamped_geojson = TimestampedGeoJson(
        data=feature_collection,
        period="PT10S",
        duration="PT5S", #needs to match feature collection seconds
        auto_play=True,
        loop=True,
        speed_slider=True,
        min_speed=50,
        max_speed=100,
        time_slider_drag_update=True,
        add_last_point=True,
        loop_button=True,
        date_options="HH:mm:ss",
        transition_time=0,
    )
    
   
    m.add_child(fg)
    # Add markers for each location
    for i, row in location_df.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=row["Location"],
            icon=folium.features.CustomIcon(
                r"C:\Users\u336708\Documents\Python-Scripts\Streamlit\wtg.png",
                icon_size=(20, 20),
                icon_anchor=(10, 14)
            )
        ).add_to(m)
    # Add a layer control to the map
    folium.LayerControl().add_to(m)
    
    m.add_child(timestamped_geojson)
    
    # add a mini map
    minimap = plugins.MiniMap()
    m.add_child(minimap)
    
    # Save the map as an HTML file
    
    html_string = m.get_root().render()
    m.save("map2.html")

    return (html_string)