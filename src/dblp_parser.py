#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from collections import defaultdict

from lxml import etree


# Ignore the following fields
ignore_field = ['volume', 'pages', 'series', 'note', 'number']
# The following fields can have multiple values
mv_field = ['author', 'address', 'cdrom', 'pages', 'cite', 'crossref',
            'editor', 'school', 'ee', 'isbn', 'url', 'publisher']
# The following field can only have a single value
sv_field = ['booktitle', 'chapter', 'journal', 'month', 'title', 'year']
# Possible genre of the doc
genre = {'article', 'inproceedings', 'proceedings', 'book', 'incollection',
         'phdthesis', 'mastersthesis', 'www'}


def iterate_dblp(dblp):
    """Iterate through xml file and read doc by doc.

    Code from stackoverflow: https://stackoverflow.com/a/42193997.

    Parameters
    ----------
    dblp : str
        Path to dblp data file.

    """

    docs = etree.iterparse(dblp, events=('start', 'end'), dtd_validation=True,
                           load_dtd=True)
    _, root = next(docs)
    start_tag = None
    for event, doc in docs:
        if event == 'start' and start_tag is None:  # a new start
            start_tag = doc.tag
        if event == 'end' and doc.tag == start_tag:
            yield start_tag, doc
            start_tag = None
            root.clear()


def parse_record(dblp, output):
    """Parse each record in dblp dataset.

    Parameters
    ----------
    dblp : str
        Path to dblp path.
    output : str
        Path to output path.

    """

    with open(output, 'w') as ofp:
        for genre, record in iterate_dblp(dblp):
            attrs = defaultdict(list)
            for attr in record:
                if attr not in ignore_field:  # field to ignore
                    attrs[attr.tag].append(attr.text)
            attrs['genre'] = genre
            try:  # make sure the record has valid format
                for key in set(attrs.keys()) & set(sv_field):
                    if not attrs[key]:  # empty is okay
                        continue
                    if len(attrs[key]) > 1:  # should have only one value
                        raise ValueError('Record {} has multi-value in {}. '
                                         'Ignored.'.format(attrs['title'],
                                                           key))
                    attrs[key] = attrs[key][0]
                json.dump(dict(attrs), ofp)
                ofp.write('\n')
            except ValueError as err:
                print(err)
                continue
