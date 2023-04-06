import datetime

alarmhour = int(input("what hour do you want:"))

alarmmint = int(input("what  mint do you want:"))
amPm = str(input("am or pm::"))

if (amPm == "pm"):
    alarmhour = alarmhour + 12

if (alarmhour == datetime.datetime.now().hour and
        alarmmint == datetime.datetime.now().minute):
    print("lazy")
