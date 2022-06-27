import csv
from parse import parse


def csvMaker(html):
    rName, rPlace, oNumber, oDateTime, dDateTime, orders, totalAmount = parse(
        html + ".html"
    )
    csvArray = []

    for i in range(len(rName)):
        data = {}

        name = rName[i]
        place = rPlace[i]
        orderNumber = oNumber[i]
        orderDT = oDateTime[i]
        isDelivered = dDateTime[i][0]
        delDT = dDateTime[i][1]
        orderItems = orders[i]
        total = totalAmount[i]

        data["ID"] = i + 1
        data["Is Delivered"] = isDelivered
        data["Order Number"] = orderNumber
        data["Restaurant Name"] = name
        data["Restaurant Location"] = place
        data["Order Time"] = str(orderDT)
        data["Delivery Time"] = str(delDT)
        data["Items Ordered"] = orderItems
        data["Total Amount"] = total

        csvArray.append(data)

    with open(html + ".csv", "w+", newline="") as c:
        writer = csv.DictWriter(
            c,
            fieldnames=[
                "ID",
                "Is Delivered",
                "Order Number",
                "Restaurant Name",
                "Restaurant Location",
                "Order Time",
                "Delivery Time",
                "Items Ordered",
                "Total Amount",
            ],
        )
        writer.writeheader()
        writer.writerows(csvArray)
