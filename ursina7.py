from ursina import *
app=Ursina()

e1=Entity(model="circle")
e2=Entity(model="quad",color=color.azure,position=(3,0,0))
e3=Entity(model="quad",color=color.cyan,position=(-3,0,0))
s1=Sequence(1,Func(e1.blink,duration=1),loop=True)
s1.start()
s2=Sequence(1,Func(e2.blink,duration=1),Func(e2.shake,duration=1),loop=1)
s2.start()
s3=Sequence(1,Func(e3.fade_out, duration=1),2,Func(e3.fade_in, duration=1),loop=1)
s3.start()












app.run()