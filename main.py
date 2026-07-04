import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# VARIABLES
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

bahnhof = "Heilbronn Hbf"

# LIST
zuege = []

for s in root.findall("s"):

    for ar in s.findall("ar"): # 'ar' bedeutet Ankunft
        zug = ar.get("l")

        if zug:
            zuege.append({
                "bahnhof": bahnhof,
                "zug": zug,
                "typ": "Ankunft",
                "geplant": ar.get("pt"),
                "aktuell": ar.get("ct")
            })

    for dp in s.findall("dp"): # 'dp' bedeutet Abfahrt
        zug = dp.get("l")

        if zug:
            zuege.append({
                "bahnhof": bahnhof,
                "zug": zug,
                "typ": "Abfahrt",
                "geplant": dp.get("pt"),
                "aktuell": dp.get("ct")
            })

# OUTPUT
print("Gefundene Züge:\n")

for zug in zuege:

    zeit = zug["geplant"] if zug["geplant"] else zug["aktuell"]

    # Zeit lesbar machen
    if zeit:
        zeit = datetime.strptime(zeit, "%y%m%d%H%M").strftime("%d.%m.%Y %H:%M")
    else:
        zeit = "Keine Zeit"

    print(
        f"{zug['typ']:9} | "
        f"{zug['zug']:8} | "
        f"{zeit} | "
        f"{zug['bahnhof']}"
    )

# print(response.text)