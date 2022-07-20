def strMonth2numMonth(strMonth):
    """
    Takes input as a string(Jan, Feb, Mar) and returns the corresponding number of the month
    Example: Mar --> 3
    """
    m2m = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
    }
    return m2m[strMonth]


def twelveTo24(hour, minute, amORpm):
    """
    Converts twelve hour clock time (4:20PM) to 24 hour clock time (1620)
    """
    if hour <= 12 and minute <= 60:
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
            print("Enter AM or PM")
        return [finalHour, finalMin]
    else:
        return "Invalid Time Format"


def find(html, className):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "lxml")
    temp = soup.find_all(class_=className)
    return temp


def findStripAndReplace(html, className, replaceText=None):
    from bs4 import BeautifulSoup

    result = []
    soup = BeautifulSoup(html, "lxml")
    temp = soup.find_all(class_=className)
    j = 0
    if replaceText == None:
        for i in temp:
            result.append((i.text).strip())
    else:
        for i in temp:
            result.append((i.text).strip())
            result[j] = result[j].replace(replaceText, " ")
            j = j + 1
    return result


def splitArray(arr, splitStr):
    final = []
    for i in range(len(arr)):
        final.append(arr[i].split(splitStr))
    return final


def export(csvORjson, html, output=True):
    """
    Exports html file to json or csv
    """
    if csvORjson == "json":
        from jsonMaker import jsonMaker

        jsonMaker(html, output)
    if csvORjson == "csv":
        from csvMaker import csvMaker

        csvMaker(html)
