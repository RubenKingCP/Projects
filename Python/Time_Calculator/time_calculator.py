def add_time(curtime, spendtime, passday = None):
    expanded = curtime.split(" ")
    time = expanded[0].split(":")
    hours = int(time[0])
    minutes = int(time[1])
    am_pm = expanded[1]
    toggle = None
    if am_pm == "AM":
        toggle = True
    elif am_pm == "PM":
        toggle = False
    spendtime_expanded = spendtime.split(":")
    hours_to_add = int(spendtime_expanded[0])
    minutes_to_add = int(spendtime_expanded[1])
    hours_total = hours + hours_to_add
    minutes_total = minutes + minutes_to_add
    if minutes_total > 59:
        hours_total += 1
    if hours_total > 12:
        hours_total -= 12
        if toggle is True:
            toggle = False
        elif toggle is False:
            toggle = True
    if toggle is True:
        am_pm = "AM"
    elif toggle is False:
        am_pm = "PM"
    time_string = str(hours_total) + ":" + str(minutes_total) + " " + am_pm
    return time_string


print(add_time("13:00 AM", "2:10"))