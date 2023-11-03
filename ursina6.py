from ursina import *
app=Ursina()



def fun():
    print_on_screen("szoveg",position=(0*.1,2*.1))
def colors():
    b.color=color.random_color()

b=Button(text="button",text_color=color.green,color=color.azure,scale=.5,icon="sword",text_origin=(0,-.5))

b.on_click=(colors)
b.on_click=(fun)
b.tooltip=Tooltip("fdfsd")








app.run()