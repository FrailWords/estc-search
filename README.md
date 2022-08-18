## Description

Search [ESTC website](http://estc.bl.uk/) for given estc numbers.

### Pre-requisites 
* `Poetry` - https://python-poetry.org/docs/#installation
* Python 3.8 or above - Pandas requires this

## Usage

```shell
./estc_info.sh <command-separated-list-of-estc-numbers>`
```

For e.g. 

```shell
./estc_info.sh S109167,R218262
```

Example output -

```shell
╒════════════╤════════════════════════════════╤════════════════════════════╤════════════════════════════════╤══════════════════╤════════════════════════════════╤══════════════════════════════╤═══════════════════════════════╤════════════════════════════════╕
│ ESTC No.   │ Title                          │ Author                     │ Publisher Info                 │ Description      │ Locations                      │ General Notes                │ Citation/Ref. Notes           │ Electronic Location            │
╞════════════╪════════════════════════════════╪════════════════════════════╪════════════════════════════════╪══════════════════╪════════════════════════════════╪══════════════════════════════╪═══════════════════════════════╪════════════════════════════════╡
│ S109167    │ [A tragedye or enterlude       │ Bale, John, 1495-1563.     │ [Wesel : Dirik van der         │ [80] p. ;  4⁰.   │ bL = British Library,  London, │ Imprint from STC.       ---  │ STC (2nd ed.),   1305   ---   │ http://gateway.proquest.com/op │
│            │ manyfestyng the chefe promyses │                            │ Straten, 1547?]                │                  │ England, U.K..   SMK:          │ In verse.       ---     A2r, │ Greg,   I, 22 (a)       ---   │ enurl?ctx_ver=Z39.88-2003&res_ │
│            │ of God unto man by all ages in │                            │                                │                  │ C.34.c.2.   CPN: imperfect;    │ line 1 of text: If profyght  │ Luborsky & Ingram. Engl.      │ id=xri:eebo&rft_val_fmt=&rft_i │
│            │ the olde lawe, from the fall   │                            │                                │                  │ A1, title page, lacking.       │ may growe, moste Christe[n]  │ illustrated books, 1536-1603, │ d=xri:eebo:image:9663 ; Early  │
│            │ of Adam to the incarnacyon of  │                            │                                │                  │ Status: Primary   Copy ID:     │ audye[n]ce.        ---       │ 1305                          │ English Books Online (EEBO) ;  │
│            │ the lorde Iesus Christ.        │                            │                                │                  │ 998455   ---     nPC = Private │ Signatures: A-E⁴ (E4 blank). │                               │ { Reproduction of the original │
│            │ Compyled by Johan Bale ...]    │                            │                                │                  │ Collections,  North America.   │                              │                               │ in the British Library. }      │
│            │                                │                            │                                │                  │ SMK: [Shelfmark not            │                              │                               │                                │
│            │                                │                            │                                │                  │ available].   CPN: Elizabethan │                              │                               │                                │
│            │                                │                            │                                │                  │ Club, Yale University [CM].    │                              │                               │                                │
│            │                                │                            │                                │                  │ Status: Verified   Copy ID:    │                              │                               │                                │
│            │                                │                            │                                │                  │ 998456                         │                              │                               │                                │
├────────────┼────────────────────────────────┼────────────────────────────┼────────────────────────────────┼──────────────────┼────────────────────────────────┼──────────────────────────────┼───────────────────────────────┼────────────────────────────────┤
│ R218262    │ A brief exposition of the Ten  │ Patrick, Simon, 1626-1707. │ London : printed by J. Hayes   │ [6], 9, [1] p. ; │ bL = British Library,  London, │                              │ Wing (2nd ed.),   P757A       │ http://gateway.proquest.com/op │
│            │ Commandments and the Lords     │                            │ for S. Thomson, at the sign of │ 8⁰.              │ England, U.K..   SMK:          │                              │                               │ enurl?ctx_ver=Z39.88-2003&res_ │
│            │ Prayer. By Symon Patrick       │                            │ the Bishops Head in St. Pauls  │                  │ 1607/492[3].   CPN: Imperfect; │                              │                               │ id=xri:eebo&rft_val_fmt=&rft_i │
│            │ rector of St. Paul Covent      │                            │ Church-yard, 1665.             │                  │ stained; with print show-      │                              │                               │ d=xri:eebo:image:34319 ; Early │
│            │ Garden.                        │                            │                                │                  │ through.   Status: Primary     │                              │                               │ English Books Online (EEBO) ;  │
│            │                                │                            │                                │                  │ Copy ID: 815489       ---      │                              │                               │ { Reproduction of the original │
│            │                                │                            │                                │                  │ nDFo = Folger Shakespeare,     │                              │                               │ in the British Library. }      │
│            │                                │                            │                                │                  │ Washington, District of        │                              │                               │                                │
│            │                                │                            │                                │                  │ Columbia.   SMK: 146385q.      │                              │                               │                                │
│            │                                │                            │                                │                  │ CPN: Disbound; remnants of     │                              │                               │                                │
│            │                                │                            │                                │                  │ binding on spine..             │                              │                               │                                │
│            │                                │                            │                                │                  │ ProvInfo:acquired from A.      │                              │                               │                                │
│            │                                │                            │                                │                  │ Sutton (7/29/54), 8/17/54.     │                              │                               │                                │
│            │                                │                            │                                │                  │ Status: Verified   Copy ID:    │                              │                               │                                │
│            │                                │                            │                                │                  │ 815492       ---     bOcc =    │                              │                               │                                │
│            │                                │                            │                                │                  │ Oxford University Corpus       │                              │                               │                                │
│            │                                │                            │                                │                  │ Christi College,  Oxford,      │                              │                               │                                │
│            │                                │                            │                                │                  │ England.   SMK: LG.1.18(5).    │                              │                               │                                │
│            │                                │                            │                                │                  │ Status: Verified   Copy ID:    │                              │                               │                                │
│            │                                │                            │                                │                  │ 815491      ---     bO =       │                              │                               │                                │
│            │                                │                            │                                │                  │ Oxford University, Bodleian    │                              │                               │                                │
│            │                                │                            │                                │                  │ Library,  Oxford, England,     │                              │                               │                                │
│            │                                │                            │                                │                  │ United Kingdom.   SMK: 8° C    │                              │                               │                                │
│            │                                │                            │                                │                  │ 721 Linc. (3).   Status:       │                              │                               │                                │
│            │                                │                            │                                │                  │ Verified   Copy ID: 3427613    │                              │                               │                                │
╘════════════╧════════════════════════════════╧════════════════════════════╧════════════════════════════════╧══════════════════╧════════════════════════════════╧══════════════════════════════╧═══════════════════════════════╧════════════════════════════════╛
```