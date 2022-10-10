# Swiggy Data

---

:warning: **Important: Swiggy has changed the orders API on the web, now you can only look at orders dating back to 1 year as opposed to all your orders. But you can still view all your orders in the mobile app.** (as of 10 October 2022)

---

Get swiggy order history in a JSON format

#### JSON
```json
    {
        "id": 52,
        "info": {
            "isDelivered": "Delivered",
            "orderNumber": "11269035XXXX",
            "name": "Mad Over Donuts",
            "place": "Greater Kailash",
            "orderDateTime": "2021-08-22 12:22:00",
            "deliveryDateTime": "2021-08-22 13:00:00",
            "items": [
                "Dounut1",
                "Dounut2",
                "Dounut3"
            ],
            "totalAmount": "898"
        }
```

#### CSV
```csv
52,Delivered,11269035XXXX,Mad Over Donuts,Greater Kailash,2021-08-22 12:22:00,2021-08-22 13:00:00,['Dounut1', 'Dounut2', 'Dounut3'],898
```

## Installation

1. Clone repo
2. ```pip install -r requirements.txt```
3. [Get HTML](https://github.com/myNameArnav/swiggyData/blob/master/Get%20HTML.md)
4. Change the argument in ```main.py```, ```export("<JSON or CSV>","<HTML FILE YOU MADE>")``` (dont add .html, just the name of the file)
5. Run ```main.py```
