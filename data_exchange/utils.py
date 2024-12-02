import requests
import json
import base64


def DX_Call(query, AUTH_TOKEN):
    url = "https://developer.api.autodesk.com/dataexchange/2023-05/graphql"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }

    response = requests.request("GET", url, headers=headers, data=json.dumps({"query": query}))
    return response.json()


def DX_Mutation_Call(query, AUTH_TOKEN):
    url = "https://developer.api.autodesk.com/dataexchange/2023-05/graphql"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps({"query": query}))

    return response.json()


def download_item_details(project_id, item_id, AUTH_TOKEN):
    url = f"https://developer.api.autodesk.com/data/v1/projects/{project_id}/items/{item_id}"

    headers = {
        'includeCustomAttributes': 'true',
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }

    response = requests.request("GET", url, headers=headers, )

    return response.json()


def get_views_for_item(urn, AUTH_TOKEN):
    url = f"https://developer.api.autodesk.com/modelderivative/v2/designdata/{urn}/metadata"
    headers = {
        'includeCustomAttributes': 'true',
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()["data"]["metadata"]


def extract_entity_type(id):
    decoded = base64.b64decode(id + "===")
    return decoded[0:4]


def decode_item(id):
    test = base64.b64decode(id)
    components = test.decode("utf-8").split("~")
    return [components[-3], components[-1], components[-2]]
