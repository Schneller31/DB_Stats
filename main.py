import requests
from dotenv import load_dotenv
import os


url = "https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/fchg/8000157"



load_dotenv(override=True)
headers = {
    "DB-Client-Id": os.getenv("DB_CLIENT_ID"),
    "DB-Api-Key": os.getenv("DB_API_KEY")
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)

print(os.getenv("DB_CLIENT_ID"))
