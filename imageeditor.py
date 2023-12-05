from PIL import Image
import os

path = "C:\\Users\\adamc\\Pictures\\Screenshots"

for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    try:
        img = Image.open(file_path)
        # Process the image here
        img.show()
    except Image.UnidentifiedImageError:
        print(f"Skipping non-image file: {file_path}")
