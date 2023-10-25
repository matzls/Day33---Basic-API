import requests
"""<https://www.webfx.com/web-development/glossary/http-status-codes/"""

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]

longitude = data["longitude"]
latitude = data["latitude"]
iss_psoition = (longitude, latitude)



print(iss_psoition)


