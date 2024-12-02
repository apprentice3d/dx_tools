from data_exchange.types import Hubs, Projects, Folder, Exchange, Item
from data_exchange.utils import DX_Call, extract_entity_type, download_item_details, get_views_for_item, decode_item


def queryHubs(AUTH_TOKEN):
    get_hubs = """
    query GetHubs {
      hubs {
        results {
          name
          id
        }
      }
    }
    """
    data = DX_Call(get_hubs, AUTH_TOKEN)
    return Hubs(data)


def queryProjects(AUTH_TOKEN, hub_id):
    get_projects = f"""
        query GetProjects {{
            projects(hubId: \"{hub_id}\") {{
                results {{
                    id
                    name
                }}
            }}
        }}
    """
    data = DX_Call(get_projects, AUTH_TOKEN)
    return Projects(data)

def queryProjectFolder(AUTH_TOKEN, project_id):
    get_project_folders = f"""
        query GetProjectFolders {{
            project(projectId: \"{project_id}\") {{
                folders {{
                    results {{
                        id
                        name
                    }}
                }}
            }}
        }}
    """
    data = DX_Call(get_project_folders, AUTH_TOKEN)
    return data["data"]["project"]["folders"]["results"]


def get_folder(AUTH_TOKEN, folder_id):
    get_folder_query = f"""
    query GetFolderContent {{
      folder(folderId: "{folder_id}") {{
        id
        name
        folders {{
          results {{
            id
            name
          }}
        }}
        exchanges {{
          results {{
            id
            name
          }}
        }}
        items{{
          results{{
            id
            name
          }}
        }}
      }}
    }}
        """
    data = DX_Call(get_folder_query, AUTH_TOKEN)
    return data["data"]["folder"]


def queryFolder(AUTH_TOKEN, id):
    if extract_entity_type(id) == b'proj':
        folders = queryProjectFolder(AUTH_TOKEN, id)
        for element in folders:
            if element["name"] == "Project Files":
                id = element["id"]
                print(f"found {element}")

    if extract_entity_type(id) == b'fold':
        data = get_folder(AUTH_TOKEN, id)
        return Folder(data)


def queryExchange(AUTH_TOKEN, id):
    get_exchange = f"""
query getExchangeInfo {{
  exchange(exchangeId: "{id}") {{
    id
    name
    version {{
      versionNumber
    }}
    versionHistory {{
      versions {{
        results {{
          id
          versionNumber
          createdOn
        }}
      }}
      tipVersion {{
        versionNumber
      }}
    }}
    alternativeIdentifiers {{
      fileUrn
      fileVersionUrn
    }}
  }}
}}
    """
    data = DX_Call(get_exchange, AUTH_TOKEN)
    return Exchange(data)


def get_item_data(AUTH_TOKEN, item_id):
    decoded_data = decode_item(item_id)
    data = download_item_details(decoded_data[0], decoded_data[1], AUTH_TOKEN)
    derivative = data["included"][0]["relationships"]["derivatives"]["data"]["id"]
    views = get_views_for_item(derivative, AUTH_TOKEN)
    item_details = Item(data)
    item_details.add_info_on_views(views)
    return item_details


def create_exchange_from_revit(AUTH_TOKEN, id, view, destination_folder):
    pass

def create_exchange_from_ifc(AUTH_TOKEN, id, destination_folder):
    pass