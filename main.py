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

zuege = []

for s in root.findall("s"):

    for ar in s.findall("ar"): # 'ar' bedeutet Ankunft
        zug = ar.get("l")

        if zug:
            zuege.append({
                "typ": "Ankunft",
                "bahnhof": bahnhof,
                "zug": zug,
                "geplant": ar.get("pt"),
                "aktuell": ar.get("ct"),
                "ppth": ar.get("ppth")
            })


    for dp in s.findall("dp"): # 'dp' bedeutet Abfahrt
        zug = dp.get("l")

        if zug:
            zuege.append({
                "typ": "Abfahrt",
                "bahnhof": bahnhof,
                "zug": zug,
                "geplant": dp.get("pt"),
                "aktuell": dp.get("ct"),
                "ppth": dp.get("ppth")
            })


# OUTPUT
print("Typ       | Bahnhof            | Zielbahnhof               | Bahnname | Zeit\n")

for zug in zuege:

    zeit = zug["geplant"] or zug["aktuell"]

    if zeit:
        zeit = datetime.strptime(zeit, "%y%m%d%H%M").strftime("%d.%m.%Y %H:%M")
    else:
        zeit = "Keine Zeit"

    if zug["typ"] == "Abfahrt" and zug["ppth"]:
        ziel = zug["ppth"].split("|")[-1]
    else:
        ziel = "-"

    print(
        f"{zug['typ']:9} | "
        f"{zug['bahnhof']:18} | "
        f"{ziel:25} | "
        f"{zug['zug']:8} | "
        f"{zeit}"
    )

    # print(response.text)
