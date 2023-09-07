def correct_time(time):
    try:
        hour, minute = time.split(':')
        hour, minute = int(hour), int(minute)
        return 0 <= hour < 24 and 0 <= minute < 60
    except ValueError:
        return False

print(correct_time("13:58")) 
print(correct_time("25:51")) 
print(correct_time("02:76")) 
