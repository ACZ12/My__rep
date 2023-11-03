import tkinter
import time
canvas = tkinter.Canvas(width=500,height=500,bg='grey')
canvas.pack() 

def clock():
     hour= time.strftime("%H")
     minute= time.strftime("%M")
     second= time.strftime("%S")

     canvas.create_rectangle(0,400,510,510,fill='black',outline='white')
     canvas.create_text(250,450,text=hour+':'+minute+':'+second,fill='green',font='Ariel 80')
     canvas.create_rectangle(0,0,500,390,fill='grey',outline='grey')

#sec
     if second=='01' or second=='11' or second== '21' or second=='31' or second=='41' or second=='51':
      canvas.create_rectangle(420,305,480,380,fill='blue')   
     elif second=='02' or second=='12' or second== '22' or second=='32' or second=='42' or second=='52':  
      canvas.create_rectangle(420,210,480,285,fill='blue')   
     elif second=='03' or second=='13' or second== '23' or second=='33' or second=='43' or second=='53':  
      canvas.create_rectangle(420,210,480,285,fill='blue')   
      canvas.create_rectangle(420,305,480,380,fill='blue')   
     elif second=='04' or second=='14' or second== '24' or second=='34' or second=='44' or second=='54':  
      canvas.create_rectangle(420,115,480,190,fill='blue')   
     elif second=='05' or second=='15' or second== '25' or second=='35' or second=='45' or second=='55':  
      canvas.create_rectangle(420,115,480,190,fill='blue')   
      canvas.create_rectangle(420,305,480,380,fill='blue')   
     elif second=='06' or second=='16' or second== '26' or second=='36' or second=='46' or second=='56':  
      canvas.create_rectangle(420,210,480,285,fill='blue')   
      canvas.create_rectangle(420,115,480,190,fill='blue')    
     elif second=='07' or second=='17' or second== '27' or second=='37' or second=='47' or second=='57':  
      canvas.create_rectangle(420,115,480,190,fill='blue')  
      canvas.create_rectangle(420,210,480,285,fill='blue')
      canvas.create_rectangle(420,305,480,380,fill='blue')   
     elif second=='08' or second=='18' or second== '28' or second=='38' or second=='48' or second=='58':  
      canvas.create_rectangle(420,20,480,95,fill='blue')   
     elif second=='09' or second=='19' or second== '29' or second=='39' or second=='49' or second=='59':  
      canvas.create_rectangle(420,20,480,95,fill='blue')   
      canvas.create_rectangle(420,305,480,380,fill='blue')
     if second>='10' and second<='19':
      canvas.create_rectangle(340,305,400,380,fill='blue')
     elif second>='20' and second<='29':
      canvas.create_rectangle(340,210,400,285,fill='blue')
     elif second>='30' and second<='39':
      canvas.create_rectangle(340,210,400,285,fill='blue')
      canvas.create_rectangle(340,305,400,380,fill='blue')
     elif second>='40' and second<='49':
      canvas.create_rectangle(340,115,400,190,fill='blue')
     elif second>='50' and second<='59':
      canvas.create_rectangle(340,115,400,190,fill='blue')
      canvas.create_rectangle(340,305,400,380,fill='blue')

#min
     if minute=='01' or minute=='11' or minute== '21' or minute=='31' or minute=='41' or minute=='51':
      canvas.create_rectangle(260,305,320,380,fill='blue')   
     elif minute=='02' or minute=='12' or minute== '22' or minute=='32' or minute=='42' or minute=='52':  
      canvas.create_rectangle(260,210,320,285,fill='blue')   
     elif minute=='03' or minute=='13' or minute== '23' or minute=='33' or minute=='43' or minute=='53':  
      canvas.create_rectangle(260,210,320,285,fill='blue')   
      canvas.create_rectangle(260,305,320,380,fill='blue')   
     elif minute=='04' or minute=='14' or minute== '24' or minute=='34' or minute=='44' or minute=='54':  
      canvas.create_rectangle(260,115,320,190,fill='blue')   
     elif minute=='05' or minute=='15' or minute== '25' or minute=='35' or minute=='45' or minute=='55':  
      canvas.create_rectangle(260,115,320,190,fill='blue')   
      canvas.create_rectangle(260,305,320,380,fill='blue')   
     elif minute=='06' or minute=='16' or minute== '26' or minute=='36' or minute=='46' or minute=='56':  
      canvas.create_rectangle(260,210,320,285,fill='blue')   
      canvas.create_rectangle(260,115,320,190,fill='blue')    
     elif minute=='07' or minute=='17' or minute== '27' or minute=='37' or minute=='47' or minute=='57':  
      canvas.create_rectangle(260,115,320,190,fill='blue')  
      canvas.create_rectangle(260,210,320,285,fill='blue')
      canvas.create_rectangle(260,305,320,380,fill='blue')   
     elif minute=='08' or minute=='18' or minute== '28' or minute=='38' or minute=='48' or minute=='58':  
      canvas.create_rectangle(260,20,320,95,fill='blue')   
     elif minute=='09' or minute=='19' or minute== '29' or minute=='39' or minute=='49' or minute=='59':  
      canvas.create_rectangle(260,20,320,95,fill='blue')   
      canvas.create_rectangle(260,305,320,380,fill='blue')
     if minute>='10' and minute<='19':
      canvas.create_rectangle(180,305,240,380,fill='blue')
     elif minute>='20' and minute<='29':
      canvas.create_rectangle(180,210,240,285,fill='blue')
     elif minute>='30' and minute<='39':
      canvas.create_rectangle(180,210,240,285,fill='blue')
      canvas.create_rectangle(180,305,240,380,fill='blue')
     elif minute>='40' and minute<='49':
      canvas.create_rectangle(180,115,240,190,fill='blue')
     elif minute>='50' and minute<='59':
      canvas.create_rectangle(180,115,240,190,fill='blue')
      canvas.create_rectangle(180,305,240,380,fill='blue')

#hour
     if hour=='01' or hour=='11' or hour== '21':
      canvas.create_rectangle(100,305,160,380,fill='blue')   
     elif hour=='02' or hour=='12' or hour== '22':  
      canvas.create_rectangle(100,210,160,285,fill='blue')   
     elif hour=='03' or hour=='13' or hour== '23':  
      canvas.create_rectangle(100,210,160,285,fill='blue')   
      canvas.create_rectangle(100,305,160,380,fill='blue')   
     elif hour=='04' or hour=='14':  
      canvas.create_rectangle(100,115,160,190,fill='blue')   
     elif hour=='05' or hour=='15':  
      canvas.create_rectangle(100,115,160,190,fill='blue')   
      canvas.create_rectangle(100,305,160,380,fill='blue')   
     elif hour=='06' or hour=='16':  
      canvas.create_rectangle(100,210,160,285,fill='blue')   
      canvas.create_rectangle(100,115,160,190,fill='blue')    
     elif hour=='07' or hour=='17':  
      canvas.create_rectangle(100,115,160,190,fill='blue')  
      canvas.create_rectangle(100,210,160,285,fill='blue')
      canvas.create_rectangle(100,305,160,380,fill='blue')   
     elif hour=='08' or hour=='18':  
      canvas.create_rectangle(100,20,160,95,fill='blue')   
     elif hour=='09' or hour=='19':  
      canvas.create_rectangle(100,20,160,95,fill='blue')   
      canvas.create_rectangle(100,305,160,380,fill='blue')
     if hour>='10' and hour<='19':
      canvas.create_rectangle(20,305,80,380,fill='blue')
     elif hour>='20' and hour<='23':
      canvas.create_rectangle(20,210,80,285,fill='blue')

     canvas.after(1000,clock)

clock()

canvas.mainloop()