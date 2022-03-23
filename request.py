import requests
import json

url = "http://bob.forno.quintoandar.com.br/house-draft"

headers = {
    "Cookie": "5AJWT_AUTH=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
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
