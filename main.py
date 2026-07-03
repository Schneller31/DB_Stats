import json
import requests
import xml.etree.ElementTree as ET

# variables
with open("api.json", "r") as file:
    api_keys = json.load(file)

url = "https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/fchg/8000157"

headers = {
    "DB-Client-Id": api_keys["DB_CLIENT_ID"],
    "DB-Api-Key": api_keys["DB_API_KEY"],
    "accept": "application/xml"
}

response = requests.get(url, headers=headers)

root = ET.fromstring(response.text)


# sorting
for s in root.findall("s"):
    for ar in s.findall("ar"):
        zug = ar.get("l")
        if zug:
            print("Zug:", zug)

    for dp in s.findall("dp"):
        zug = dp.get("l")
        if zug:
            print("Zug:", zug)

print(response.status_code)
print(response.text)

#print(api_keys["DB_CLIENT_ID"])
#print(api_keys["DB_API_KEY"])