import datetime
from playsound import playsound
alarmHour=int(input("óra: "))
alarmMin=int(input("perc: "))
alarmAm=input("de/du: ")

if alarmAm=="du":
    alarmHour+=12
    
while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing...")
        playsound("punky.mp3")
        break
canvas.mainloop()