import datetime
from playsound import playsound
alarmHour = int(input("Horas:  "))
alarmMin = int(input("Minutos:  "))
alarmAm = input("am  /  pm:  " )

if alarmAm=="pm":
    alarmHour+=12
    
while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Acorda...")
        playsound("samsung.mp3") 
        break   
    