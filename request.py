import requests
import json

url = "http://bob.quintoandar.com.br/house-draft"

headers = {
    "Cookie": "5andar_carrinho=[]; amplitude_id_crossquintoandar.com.br=eyJkZXZpY2VJZCI6ImM3ZGQ2M2Q1LWRmNTAtNGZlMi1hZWE4LWY0NzA1ZjM4NTViYVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0Nzg4NTg1NTE0MywibGFzdEV2ZW50VGltZSI6MTY0Nzg4NTg1NTE0MywiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; amplitude_idquintoandar.com.br=eyJkZXZpY2VJZCI6Ijg1MGFiMDA3LTA2MDItNDRhZi05NTA2LWJlMzQ4Y2NhMDZjZlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0Nzg4NTg1NTE0MSwibGFzdEV2ZW50VGltZSI6MTY0Nzg4NTg1Njc4MywiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjF9; 5AJWT_AUTH=eyJraWQiOm51bGwsImFsZyI6IlJTMjU2In0.eyJqdGkiOiJhY0dYYUdtdENyNElMQlQtLURoRkFnIiwiaWF0IjoxNjQ3ODg1ODU4LCJpZCI6MzM4Njg0MiwibmFtZSI6Ikpvw6NvIFZpdG9yIGRlIFBhdWxhIEFsdmVzIiwiZmlyc3RuYW1lIjoiSm_Do28gVml0b3IiLCJ0aXR1bG8iOiJKb8OjbyBWaXRvciIsImVtYWlsIjoiam9hby5hbHZlc0BxdWludG9hbmRhci5jb20uYnIiLCJ0ZWxlZm9uZSI6bnVsbCwicm9sZXMiOiJhZG1pbiIsImNyZWF0aW9uRGF0ZSI6IjIxLzAzLzIwMjIgMTg6MDQiLCJ1c2VyQ3JlYXRlZEF0IjoiMjAyMS0wNC0wOFQxNzo1OToxNFoiLCJleHAiOjE2NDg0OTA2NTh9.b2Q6OCjn9UzopvzQuux9YYJBPY1-i53Vx8USHuNhrWROHZC2gp40QhbW99QWNOoVLkXFdej-4kbknirMIPIwYTkL84zYFupSdQi90fKWkCH6aLHOePOlhqVasgDpwPnYZl5du1NGNb2LFEWFlyAMfseLAyCVXK8w-jfBnh0rw7HfyE-eySw7O84c9Fgc2CS0VPQaOUpLnrC-2cluDZba1lPva1vdXWO6ixGkr1LMhuSBqt1HxldEfdYQjvTbH-vBBSxKoR5qzLIvBIYl_U3MNLjApq3Za_HoR30kXJ6zwgMDcH4Cl6xPfu7N24rsf2w9Nc54fxRdaPheRaCNxf22ew; _ga=GA1.3.707391054.1647885858; _hjSessionUser_2503898=eyJpZCI6IjU1Y2VhMTQ3LThhYmQtNTMyNS05OWI5LWVhMjk2NWNiMjVkMCIsImNyZWF0ZWQiOjE2NDgwNTY0NDI5MjMsImV4aXN0aW5nIjp0cnVlfQ==; 5A_SESSION=FfikzR5V60Lug0RNSlBrSA|1648066944|i1dnVZTZL1CbNKoLCebZ8OAUk0Y",
    "Content-Type": "application/json",
}
data = {
    "location": {
        "regionId": 53,
        "address": "Avenida Paulista",
        "floor": "2",
        "number": "205",
        "neighborhood": "Bela Vista",
        "complement": "3321",
        "state": "SP",
        "zipCode": "01311-000",
        "city": "São Paulo",
        "lat": -23.5700387,
        "lng": -46.6462292,
    },
    "pricing": {
        "rent": 3200,
        "salePrice": "null",
        "condoPrice": 630,
        "iptuNotPaid": False,
        "iptuList": [{"installmentAmount": 200, "installmentQuantity": 1}],
        "specialConditions": ["EXCLUSIVITY"],
    },
    "owner": {
        "email": "lucas.tomasi+sadir@quintoandar.com.br",
        "name": "Sadir",
        "phone": "(48) 9 91459142",
    },
    "businessContexts": ["RENT"],
    "blueprint": {
        "totalArea": 100,
        "bedrooms": 3,
        "suites": 1,
        "bathrooms": 3,
        "garages": 2,
        "houseType": "APARTMENT",
    },
    "details": {
        "isPetFriendly": True,
        "isPenthouse": False,
        "frontDoorType": "ALL_DAY",
        "installations": "null",
        "appliances": {
            "REFRIGERATOR": True,
            "STOVE": False,
            "MICROWAVE": False,
            "WASHING_MACHINE": False,
            "SOFA": True,
            "TABLE": True,
            "KITCHEN_CABINET": True,
            "BEDROOM_CABINET": True,
            "BED": True,
        },
        "accessibilityItems": "null",
        "description": "asd asdf asdfasdf asd f",
    },
    "access": {
        "accessType": "COMMON",
        "authorizationType": "OWNER_PRESENT",
        "occupantType": "OWNER",
        "password": "null",
        "optedKeysWithAgent": "null",
    },
    "clientSideId": "a28be171-24e9-4a9c-acb7-113852602334",
    "owners": {
        "list": [
            {
                "email": "lucas.tomasi+sadir@quintoandar.com.br",
                "name": "Sadir",
                "phone": "+5548991459142",
                "personType": "NATURAL_PERSON",
            }
        ]
    },
    "administrators": {
        "list": [
            {
                "email": "lucas.tomasi+sadir@quintoandar.com.br",
                "name": "Sadir",
                "phone": "+5548991459142",
            }
        ]
    },
    "type": "REFERRAL",
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r)
