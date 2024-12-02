from prettytable import PrettyTable


class Hubs:
    def __init__(self, data):
        self.data = data["data"]["hubs"]["results"]
        self.table = PrettyTable()
        self.table.field_names = ["id", "name"]
        self.table.title = "Hubs"
        for element in self.data:
            self.table.add_row([element['id'], element['name']])

    def get(self):
        return self.data

    def __str__(self):
        return self.table.__str__()


class Projects:
    def __init__(self, data):
        self.data = data["data"]["projects"]["results"]
        self.table = PrettyTable()
        self.table.field_names = ["id", "name"]
        self.table.title = "Projects"
        for element in self.data:
            self.table.add_row([element['id'], element['name']])

    def get(self):
        return self.data

    def __str__(self):
        return self.table.__str__()


class Folder:
    def __init__(self, data):
        self.data = data
        self.folder_table = PrettyTable()
        self.items_table = PrettyTable()
        self.exchange_table = PrettyTable()
        self.folder_table.title = "Folders"
        self.items_table.title = "Items"
        self.exchange_table.title = "Exchanges"
        self.folder_table.field_names = ["id", "name"]
        self.items_table.field_names = ["id", "name"]
        self.exchange_table.field_names = ["id", "name"]

        for element in data["folders"]["results"]:
            self.folder_table.add_row([element['id'], element['name']])
        for element in data["items"]["results"]:
            self.items_table.add_row([element['id'], element['name']])
        for element in data["exchanges"]["results"]:
            self.exchange_table.add_row([element['id'], element['name']])

    def get(self):
        return self.data

    def __str__(self):
        return self.folder_table.__str__() + "\n" + self.items_table.__str__() + "\n" + self.exchange_table.__str__()


class Exchange:
    def __init__(self, data):
        self.data = data
        self.info_table = PrettyTable()
        self.info_table.title = "Exchange Info"
        self.info_table.field_names = ["ID", "Name", "TipVersion", "File URN"]
        exchange = data["data"]["exchange"]
        self.info_table.add_row(
            [exchange["id"], exchange["name"], exchange["version"]["versionNumber"],
             exchange["alternativeIdentifiers"]["fileUrn"]])

        self.version_table = PrettyTable()
        self.version_table.title = "Versions"
        self.version_table.field_names = ["ID", "Version", "Created ON"]
        versions = data["data"]["exchange"]["versionHistory"]["versions"]["results"]
        for version in versions:
            self.version_table.add_row([version["id"], version["versionNumber"], version["createdOn"]])

    def get(self):
        return self.data

    def __str__(self):
        return self.info_table.__str__() + "\n" + self.version_table.__str__()


class Item:
    def __init__(self, data):
        self.data = data
        self.views = None
        self.views_table = None

        self.info_table = PrettyTable()

        item_id = data["data"]["id"]
        self.info_table.title = f"Item details: {item_id}"
        self.info_table.field_names = ["Name", "CreateTime", "CreateUserName"]
        self.info_table.add_row(
            [data["data"]["attributes"]["displayName"], data["data"]["attributes"]["createTime"], data["data"]["attributes"]["createUserName"]])
        self.item_extension = data["data"]["attributes"]["displayName"][-3:]

    def get(self):
        return self.views

    def get_format(self):
        return self.item_extension

    def add_info_on_views(self, views):
        self.views = views
        self.views_table = PrettyTable()
        self.views_table.title = "Views"
        self.views_table.field_names = ["Name", "Role", "GUID"]
        for view in self.views:
            if view["role"] == "3d":
                self.views_table.add_row([view["name"], view["role"], view["guid"]])

    def __str__(self):
        if self.views_table:
            return self.info_table.__str__() + "\n" + self.views_table.__str__()
        else:
            return self.info_table.__str__()
