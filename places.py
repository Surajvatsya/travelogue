import json
import urllib
import requests

BASEURL = 'https://www.universal-tutorial.com/api'

# TODO send private keys to env
def get_auth_token():
    
    url = BASEURL+"/getaccesstoken"

    headers = {
        "Accept": "application/json",
        "api-token": "OvZAwEkUuvZKGmSaP73_GoAB_XW3QohqcCqPhWl4azD1azz31dPKXkrX36NJqh7bFh0",
        "user-email": "rehansingh.4522@gmail.com"
    }
    return requests.get(url, headers=headers).json()["auth_token"] # Here you have the data that you need

def get_states():
    url = BASEURL + "/states/India"
    headers = {
    "Authorization": f"Bearer {get_auth_token()}",
    "Accept": "application/json"
    }

    states = requests.get(url, headers=headers).json()
    return states

def get_cities(state):
    url = BASEURL + f"/cities/{state}"
    headers = {
    "Authorization": f"Bearer {get_auth_token()}",
    "Accept": "application/json"
    }

    cities = requests.get(url, headers=headers).json()
    return cities

print(get_cities("Bihar"))
