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
./estc_info.sh S109167
```

Example output -

```shell
╒════════════════════════════════╤════════════════════════╤════════════════════════╤════════════════╤════════════════════════════════╤═══════════════════════════╤══════════════════════════╕
│ Title                          │ Author                 │ Pub_Info               │ Description    │ Location                       │ General Note              │ Citation/Ref. Note       │
╞════════════════════════════════╪════════════════════════╪════════════════════════╪════════════════╪════════════════════════════════╪═══════════════════════════╪══════════════════════════╡
│ [A tragedye or enterlude       │ Bale, John,1495-1563.  │ [Wesel :Dirik van der  │ [80] p. ; 4⁰.  │ bL=British                     │ Imprint from STC.         │ STC (2nd ed.),1305       │
│ manyfestyng the chefe promyses │                        │ Straten,1547?]         │                │ Library,London, England, U.K   │                           │                          │
│ of God unto man by all ages in │                        │                        │                │ ..SMK:C.34.c.2.CPN:imp         │                           │                          │
│ the olde lawe,from the fall    │                        │                        │                │ erfect; A1, title page, lackin │                           │                          │
│ of Adam to the incarnacyon of  │                        │                        │                │ g.Status:PrimaryCopy           │                           │                          │
│ the lorde Iesus Christ.        │                        │                        │                │ ID:998455                      │                           │                          │
│ Compyled by Johan Bale ...]    │                        │                        │                │                                │                           │                          │
├────────────────────────────────┼────────────────────────┼────────────────────────┼────────────────┼────────────────────────────────┼───────────────────────────┼──────────────────────────┤
│ nan                            │ nan                    │ nan                    │ nan            │ nPC=Private                    │ In verse.                 │ Greg,I, 22 (a)           │
│                                │                        │                        │                │ Collections,North              │                           │                          │
│                                │                        │                        │                │ America.SMK:[Shelfmark not     │                           │                          │
│                                │                        │                        │                │ available].CPN:Elizabethan     │                           │                          │
│                                │                        │                        │                │ Club, Yale University [CM].    │                           │                          │
│                                │                        │                        │                │ Status:VerifiedCopy            │                           │                          │
│                                │                        │                        │                │ ID:998456                      │                           │                          │
├────────────────────────────────┼────────────────────────┼────────────────────────┼────────────────┼────────────────────────────────┼───────────────────────────┼──────────────────────────┤
│ nan                            │ nan                    │ nan                    │ nan            │ nan                            │ A2r, line 1 of text: If   │ Luborsky & Ingram. Engl. │
│                                │                        │                        │                │                                │ profyght may growe, moste │ illustrated books,       │
│                                │                        │                        │                │                                │ Christe[n] audye[n]ce.    │ 1536-1603,1305           │
├────────────────────────────────┼────────────────────────┼────────────────────────┼────────────────┼────────────────────────────────┼───────────────────────────┼──────────────────────────┤
│ nan                            │ nan                    │ nan                    │ nan            │ nan                            │ Signatures: A-E⁴ (E4      │ nan                      │
│                                │                        │                        │                │                                │ blank).                   │                          │
╘════════════════════════════════╧════════════════════════╧════════════════════════╧════════════════╧════════════════════════════════╧═══════════════════════════╧══════════════════════════╛
```