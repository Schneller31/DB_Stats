import json
import requests

with open("api.json", "r") as file:
    api_keys = json.load(file)


url = "https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/fchg/8000157"

headers = {
    "DB-Client-Id": api_keys["DB_CLIENT_ID"],
    "DB-Api-Key": api_keys["DB_API_KEY"],
    "accept": "application/xml"
}


response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)

print(api_keys["DB_CLIENT_ID"])
print(api_keys["DB_API_KEY"])