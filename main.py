import os
import requests
from datetime import datetime

USERNAME = "khanshoaib"
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

#creating a user at pixela (by generating unique token)
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
response = requests.post(url=pixela_endpoint , json=user_params)
print(response.text)

#creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_configuration = {
    "id" : GRAPH_ID,
    "name" : "Python Daily Graph",
    "unit" : "km",
    "type" : "int",
    "color" : "ajisai"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
response = requests.post(url=graph_endpoint, headers=headers, json=graph_configuration)
print(response.text)

#creating a pixel
today = datetime.now()
pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours did you study today? ")
}
response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}" , headers=headers , json=pixel_params)
print(response.text)

