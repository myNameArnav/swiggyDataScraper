from bs4 import BeautifulSoup
from util import twelveTo24, numMonth2strMonth, findStripAndReplace, splitArray
import datetime

with open("arnavData.html") as f:
    html = f.read()


soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())

# ? Restaurant Name

rName = []
rNameTemp = soup.find_all(class_="_3h4gz")
j = 0
for i in rNameTemp:
    rName.append((i.text).rstrip())
    rName[j] = rName[j].replace(
        "\n                                                                ", " "
    )
    j = j + 1
# print(len(rName))

# ? Restaurant Location
rLoc = []
rLocTemp = soup.find_all(class_="_2haEe")
j = 0
for i in rLocTemp:
    rLoc.append((i.text).rstrip())
    rLoc[j] = rLoc[j].replace(
        "\n                                                                ", " "
    )
    j = j + 1
# print(len(rLoc))
# ? Order Number
oNumber = []
orderNumber = []
orderNumberTemp = soup.find_all(class_="_2uT6l")
j = 0
for i in orderNumberTemp:
    oNumber.append((i.text).rstrip())
    oNumber[j] = oNumber[j].replace(
        "\n                                                                ", " "
    )
    j = j + 1
for d in oNumber:
    orderNumber.append((oNumber[oNumber.index(d)].split(" ")[1])[1:])

# print(orderNumber)

# * ORDER #139030391698
# * ORDER #1147986806

# ? Order Date, Time
orderDTemp = []
orderDateTime = []
oDateTime = []
orderDTemp = oNumber

for orderDT in orderDTemp:
    orderDateTime.append((orderDTemp[orderDTemp.index(orderDT)].split(" ")))

for i in range(len(orderDTemp)):
    hour, minute = twelveTo24(
        int(orderDateTime[i][7][:-3]),
        int(orderDateTime[i][7][3:]),
        str(orderDateTime[i][-1]),
    )
    year = int(orderDateTime[i][6][:-1])
    month = numMonth2strMonth(orderDateTime[i][4])
    day = int(orderDateTime[i][5][:-1])
    x = datetime.datetime(year, month, day, hour, minute)
    oDateTime.append(x)

# print(oDateTime)
# print(len(oDateTime))

# ? Delivery Date, Time
delDate = []
deliveryDT = []
deliveryDateTime = []
dDateTemp = soup.find_all(class_="_2fkm7")

j = 0
for temp in dDateTemp:
    delDate.append((temp.text).strip())
    delDate[j] = delDate[j].replace(
        "\n                                                                    ", " "
    )
    j = j + 1

for d in range(len(delDate)):
    deliveryDT.append((delDate[d].split(" ")))

for a in range(len(delDate)):
    dORc = deliveryDT[a][0]
    year = int(deliveryDT[a][5][:-1])
    month = numMonth2strMonth(deliveryDT[a][3])
    day = int(deliveryDT[a][4][:-1])
    hour, minute = twelveTo24(
        int(deliveryDT[a][6][:-3]), int(deliveryDT[a][6][3:]), deliveryDT[a][-1]
    )
    dt = datetime.datetime(year, month, day, hour, minute)
    deliveryDateTime.append([dORc, dt])

# print(len(deliveryDateTime))

# ? Items Ordered
orders = []
iOrders = []
itemsOrdered = []

# ordersTemp = soup.find_all(class_ = "nRCg_")
iOrders = splitArray(
    findStripAndReplace(
        html, "nRCg_", "\n                                                            "
    ),
    ",",
)
print(iOrders)


# print(splitArray(iOrders, ","))

# print(ordersTemp)
# ? Items Detailed
# ? Total Paid
