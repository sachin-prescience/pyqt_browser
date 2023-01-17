import requests
import json

# final_url="https://datausa.io/api/data?drilldowns=Nation&measures=Population"
final_url="https://datausa.io/api/data?drilldowns=State&measures=Population"

response = requests.get(final_url)

d=json.loads(response.text)
resp=d['data']