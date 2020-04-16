'''
Client ID
ZxECXD6C-chZSsF7BEhGqQ

API Key
jMa-RCY8bSBNy_yUn697pz8b7q4garQ7wErUUP7AvlwOnYsaUv0f-856QhUe8nCIOwbacrNWwO3fB9z40Z05gUiHKT4Kk3mA6p_zmAe9WHo4yFvvQrdNuoI_b1eWXnYx
'''
import requests
import config
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
l = [business["name"] for business in businesses if business["rating"] > 4.5]
print(l)
