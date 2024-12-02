import os
from typing import Optional

import typer
from config import AUTH_TOKEN
from typing_extensions import Annotated
from data_exchange.utils import decode_item
from data_exchange.query import queryHubs, queryProjects, queryFolder, queryExchange, get_item_data, \
    create_exchange_from_revit, create_exchange_from_ifc

__app_name__ = "dx-tools"
__version__ = "0.1.0"




app = typer.Typer(help="CLI Data Exchange tool", no_args_is_help=True)
exchange_app = typer.Typer()
app.add_typer(exchange_app, name="exchange", no_args_is_help=True, help="Commands on exchanges")
item_app = typer.Typer()
app.add_typer(item_app, name="item", no_args_is_help=True, help="Commands on items")


@app.command()
def getHubs(raw: Annotated [bool, typer.Option(help="get the list of hubs as JSON array")] = False):
    """
    Get list of hubs that can be either in form of table or as JSON array
    """
    try:
        results = queryHubs(AUTH_TOKEN)
        if raw:
            print(results.get())
        else:
            print(results)
    except Exception as e:
        print("ERROR: The Auth token expired")


@app.command()
def getProjects(hubid: str, raw: Annotated [bool, typer.Option(help="get the list of hubs as JSON array")] = False):
    """
    Get list of projects, providing the id of the hub.
    """
    try:
        results = queryProjects(AUTH_TOKEN, hubid)
        if raw:
            print(f"Listing hubs for {hubid}.")
            print(results.get())
        else:
            print(results)
    except Exception as e:
        print("ERROR: The Auth token expired")


@app.command()
def getFolder(id: str, raw: Annotated [bool, typer.Option(help="get the list of hubs as JSON array")] = False):
    """
    Get the content of a folder, providing its id.
    """
    try:
        results = queryFolder(AUTH_TOKEN, id)
        if raw:
            print(results.get())
        else:
            print(f"Listing folders for {id}.")
            print(results)
    except Exception as e:
        print("ERROR: The Auth token expired")


@exchange_app.command()
def info(id: str, raw: Annotated [bool, typer.Option(help="get the data on exchange in JSON format")] = False):
    """
    Get info about an exchange by providing the id of the exchange.
    """
    try:
        results = queryExchange(AUTH_TOKEN, id)
        if raw:
            print(results.get())
        else:
            print(f"Getting the exchange data for {id}.")
            print(results)
    except Exception as e:
        print("ERROR: The Auth token expired")


@item_app.command()
def info(item_id: str, raw: Annotated [bool, typer.Option(help="get the views as JSON array")] = False):
    """
    Get info about an item by providing the id of the item.
    """
    try:
        results = get_item_data(AUTH_TOKEN, item_id)
        if raw:

            print(results.get())
        else:
            print(f"Getting the item data for {item_id}.")
            print(results)
    except Exception as e:
        print("ERROR: The Auth token expired")





@item_app.command()
def createExchange(id: str,
                   name: Annotated [str, typer.Option(help="name of to be created exchange")],
                   folder: Annotated [str, typer.Option(help="folder id where the exchange should be created")],
                   view: Annotated [str, typer.Option(help="view name that should be used for creating the exchange")] = ""):
    """
       Create an exchange given the id of the source file
    """
    item_urns = decode_item(id)
    destination_folder = folder if folder else item_urns[-2]
    response = None
    item = get_item_data(AUTH_TOKEN, id)
    if item.get_format() == "rvt":
        if view == "":
            print("For Revit source files, you have to specify the view name")
            return
        print(f"Creating exchange from Revit file with {id} and saving it in {destination_folder}.")
        response = create_exchange_from_revit(AUTH_TOKEN, id, view, destination_folder, name)
    if item.get_format() == "ifc":
        print(f"Creating exchange from IFC file with {id} and saving it in {destination_folder}.")
        response = create_exchange_from_ifc(AUTH_TOKEN, id, destination_folder, name)
    if response is None:
        print("ERROR: Unsupported format for creating the exchange.")
    else:
        exchange_id = response["id"]
        exchange_name = response["name"]
        print(f"The exchange with id = {exchange_id} and name = '{exchange_name}' is now in process of being created.")


def _version_callback(value: bool):
    if value:
        typer.echo(f"APP: {__app_name__}\nVersion: {__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the app version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


if __name__ == "__main__":
    app(prog_name=__app_name__)
    # typer.run(main)