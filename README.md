# DBLP Dataset Parser

The repo is forked from
[IsaacChanghau/DBLPParser](https://github.com/IsaacChanghau/DBLPParser) with
major codebase re-designed and bug fixed.

This script provides a simple way to convert the `XML` file of original
[DBLP Computer Science Bibliography](https://dblp.org/xml/) to a more
user-friendly `JSON` format.

The script was tested on DBLP screenshot published on `2019-04-29` which has
`6,850,920` in total.

## Installation

```bash
pip install lxml
```

## Usage

1. Download `dblp.xml.gz` and `dblp.dtd` from
[DBLP Computer Science Bibliography](https://dblp.org/xml/).
2. Decompress `dblp.xml.gz`.
3. Run the below script.

```bash
python main.py --dblp [path_to_dblp.xml] --output [output.json]
```

Each line of the generated document is a `JSON` record:
```json
{"author": ["Carmen Heine"], "title": "Modell zur Produktion von Online-Hilfen.", "year": "2010", "school": ["Aarhus University"], "pages": ["1-315"], "isbn": ["978-3-86596-263-8"], "ee": ["http://d-nb.info/996064095"], "genre": "phdthesis"}
```
