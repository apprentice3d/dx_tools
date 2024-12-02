# `dx-tools`

CLI Data Exchange tool

**Usage**:

```console
$ dx-tools [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-v, --version`: Show the app version and exit.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `gethubs`: Get list of hubs that can be either in form of table or as JSON array
* `getprojects`: Get list of projects, providing the id of the hub.
* `getfolder`: Get the content of a folder, providing its id.
* `exchange`: Commands on exchanges
* `item`: Commands on items

## `dx-tools gethubs`

Get list of hubs that can be either in form of table or as JSON array

**Usage**:

```console
$ dx-tools gethubs [OPTIONS]
```

**Options**:

* `--raw / --no-raw`: get the list of hubs as JSON array  [default: no-raw]
* `--help`: Show this message and exit.

## `dx-tools getprojects`

Get list of projects, providing the id of the hub.

**Usage**:

```console
$ dx-tools getprojects [OPTIONS] HUBID
```

**Arguments**:

* `HUBID`: [required]

**Options**:

* `--raw / --no-raw`: get the list of hubs as JSON array  [default: no-raw]
* `--help`: Show this message and exit.

## `dx-tools getfolder`

Get the content of a folder, providing its id.

**Usage**:

```console
$ dx-tools getfolder [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--raw / --no-raw`: get the list of hubs as JSON array  [default: no-raw]
* `--help`: Show this message and exit.

## `dx-tools exchange`

Commands on exchanges

**Usage**:

```console
$ dx-tools exchange [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `info`: Get info about an exchange by providing the id of the exchange.

### `dx-tools exchange info`

Get info about an exchange by providing the id of the exchange.

**Usage**:

```console
$ dx-tools exchange info [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--raw / --no-raw`: get the data on exchange in JSON format  [default: no-raw]
* `--help`: Show this message and exit.

## `dx-tools item`

Commands on items

**Usage**:

```console
$ dx-tools item [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `info`: Get info about an item by providing the id of the item.
* `createexchange`: Create an exchange given the id of the source file

### `dx-tools item info`

Get info about an item by providing the id of the item.

**Usage**:

```console
$ dx-tools item info [OPTIONS] ITEM_ID
```

**Arguments**:

* `ITEM_ID`: [required]

**Options**:

* `--raw / --no-raw`: get the views as JSON array  [default: no-raw]
* `--help`: Show this message and exit.

### `dx-tools item createexchange`

Create an exchange given the id of the source file

**Usage**:

```console
$ dx-tools item createexchange [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--name TEXT`: name of to be created exchange
* `--view TEXT`: view name that should be used for creating the exchange
* `--folder TEXT`: folder id where the exchange should be created
* `--help`: Show this message and exit.