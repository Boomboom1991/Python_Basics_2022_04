# from datetime import datetime
# ts = int(input())
# print(datetime.fromtimestamp(1485714600).strftime("%A, %B %d, %Y %I:%M:%S"))


def sec_converter(duration):
    if duration < 60:
        return print(duration, "секунд")
    else:
        days = duration //86400
        hours = (duration - days*86400)//3600
        mins = (duration - days*86400 - hours*3600)//60
        secs = duration - days*86400 - hours*3600 - mins*60
        return days, hours, mins, secs

duration  = int(input("Введите количество секунд: "))
days, hours, mins, sesc = sec_converter(duration)
print(f"{days} дней, {hours} часов, {mins} минут, {sesc} секунд ")