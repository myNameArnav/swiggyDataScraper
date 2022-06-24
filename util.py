def numMonth2strMonth(strMonth):
    m2m = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
    return m2m[strMonth]

def twelveTo24(hour, minute, amORpm):
    if hour >= 12 & minute >= 60:
        if amORpm == "AM":
            if hour == 12:
                finalHour = 00
                finalMin = minute
            else:
                finalHour = hour
                finalMin = minute
        elif amORpm == "PM":
            if hour == 12:
                finalHour = 12
                finalMin = minute
            else:
                finalHour = hour + 12
                finalMin = minute
        else:
            print("Enter AM or PM only")
        return [finalHour, finalMin]
    else:
        return "Invalid Time Format"