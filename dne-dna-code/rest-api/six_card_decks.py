import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload = {}
headers = {
  'Cookie': '__cfduid=dfb09ede555616395fed74c25ed9b4d9b1595368194'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
