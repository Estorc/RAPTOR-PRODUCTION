import requests
import json


jsontext = open("news.json", encoding='utf-8');
url = 'https://api.jsonbin.io/v3/b/6036417cf1be644b0a643be5'
headers = {
  'Content-Type': 'application/json',
  'X-Master-Key': '$2b$10$vETZtGKD3d0BedobYF52N.4JvqGDZmzHoWLVDxw5gpcYsabHBgQam'
}

jsonstring = jsontext.read();
data = json.loads(jsonstring);

req = requests.put(url, json=data, headers=headers)
print(req.text)
