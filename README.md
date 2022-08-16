## Description

Search [ESTC website](http://estc.bl.uk/) using given estc number.

### Pre-requisites 
* `Poetry` - https://python-poetry.org/docs/#installation
* Python 3.8 or above - Pandas requires this

## Usage

```shell
./estc_info.sh <estc_no.>`
```

For e.g. 

```shell
./estc_info.sh R218262
```

Example output -

```shell
╒════╤════════════════════════════════╤════════════════════════════╤══════════════════════════════════════════════════════════════════════════════════════════════════════════════╤═══════════════════════╕
│    │ Title                          │ Author                     │ Pub_Info                                                                                                     │ Description           │
╞════╪════════════════════════════════╪════════════════════════════╪══════════════════════════════════════════════════════════════════════════════════════════════════════════════╪═══════════════════════╡
│  0 │ A brief exposition of the      │ Patrick, Simon,1626-1707.  │ London printed by J. Hayes for S. Thomson, at the sign of the Bishops Head in St. Pauls Church-yard,1665.    │ [6], 9, [1] p. ; 8⁰.  │
│    │ Ten Commandments and the Lords │                            │                                                                                                              │                       │
│    │ Prayer. By Symon Patrick       │                            │                                                                                                              │                       │
│    │ rector of St. Paul Covent      │                            │                                                                                                              │                       │
│    │ Garden.                        │                            │                                                                                                              │                       │
╘════╧════════════════════════════════╧════════════════════════════╧══════════════════════════════════════════════════════════════════════════════════════════════════════════════╧═══════════════════════╛
```