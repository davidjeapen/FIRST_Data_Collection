import py_pdf_parser.loaders as pdf
from py_pdf_parser.common import BoundingBox
import re

import py_pdf_parser.visualise.main

document = pdf.load_file('zipcodes.pdf')

print(document.elements)
# Zip codes
bb = BoundingBox(110, 145, 45, 730)
# Assembly districts
bb = BoundingBox(270, 320, 45, 730)
# Senator Districts
bb = BoundingBox(375, 435, 45, 730)

inbox = document.elements.filter_partially_within_bounding_box(bb, 1)

def remove_letters(input_string):
    # Using regular expression to remove all letters
    result = re.sub(r'[a-zA-Z ]', '', input_string)
    return result

for e in inbox:
    alist.append(e.text())

for i in range(0, len(alist)):
    ass_copy.append(alist[i])
    if '\n' in alist[i]:
        x = alist[i].split('\n')
        ass_copy[len(ass_copy) - 1] = x[0]
        ass_copy.append(x[1])

final_data = []
for page in range(1, document.number_of_pages + 1):
    zlist_raw = []
    alist_raw = []
    slist_raw = []

    zlist = []
    alist = []
    slist = []

    # parse zip codes
    bb = BoundingBox(110, 145, 45, 730)
    inbox = document.elements.filter_partially_within_bounding_box(bb, page)
    for e in inbox:
        alist_raw.append(e.text())

    # fix any rows with new line
    for i in range(0, len(zlist_raw)):
        zlist.append(zlist_raw[i])
        if '\n' in zlist_raw[i]:
            x = zlist_raw[i].split('\n')
            zlist[len(zlist) - 1] = x[0]
            zlist.append(x[1])

    # parse assembly districts
    bb = BoundingBox(270, 320, 45, 730)
    inbox = document.elements.filter_partially_within_bounding_box(bb, page)
    for e in inbox:
        alist_raw.append(e.text())

    # fix any rows with new line
    for i in range(0, len(alist_raw)):
        alist.append(alist_raw[i])
        if '\n' in alist_raw[i]:
            x = alist_raw[i].split('\n')
            alist[len(alist) - 1] = x[0]
            alist.append(x[1])

    # parse senate districts
    bb = BoundingBox(375, 435, 45, 730)
    inbox = document.elements.filter_partially_within_bounding_box(bb, page)
    for e in inbox:
        alist_raw.append(e.text())

    # fix any rows with new line
    for i in range(0, len(slist_raw)):
        slist.append(slist_raw[i])
        if '\n' in slist_raw[i]:
            x = slist_raw[i].split('\n')
            slist[len(slist) - 1] = x[0]
            slist.append(x[1])

    page_data = [list(a) for a in zip(zlist, alist, slist)]

    final_data += page_data


final_data1 = []
for page in range(1, document.number_of_pages + 1):
    zlist_raw = []
    alist_raw = []
    slist_raw = []
    zlist = []
    alist = []
    slist = []
    # parse zip codes
    bb = BoundingBox(110, 145, 45, 730)
    inbox = document.elements.filter_partially_within_bounding_box(bb, page)
    for e in inbox:
        text = remove_letters(e.text())
        zlist_raw.append(text)
    # fix any rows with new line
    for i in range(0, len(zlist_raw)):
        zlist.append(zlist_raw[i])
        if '\n' in zlist_raw[i]:
            x = zlist_raw[i].split('\n')
            zlist[len(zlist) - 1] = x[0]
            zlist.append(x[1])
    # parse assembly districts
    bb = BoundingBox(270, 320, 45, 730)
    inbox = document.elements.filter_partially_within_bounding_box(bb, page)
    for e in inbox:
        text = remove_letters(e.text())
        alist_raw.append(text)
    # fix any rows with new line
    for i in range(0, len(alist_raw)):
        alist.append(alist_raw[i])
        if '\n' in alist_raw[i]:
            x = alist_raw[i].split('\n')
            alist[len(alist) - 1] = x[0]
            alist.append(x[1])
    # parse senate districts
    bb = BoundingBox(375, 435, 45, 730)
    inbox = document.elements.filter_partially_within_bounding_box(bb, page)
    for e in inbox:
        text = remove_letters(e.text())
        slist_raw.append(text)

    # fix any rows with new line
    for i in range(0, len(slist_raw)):
        slist.append(slist_raw[i])
        if '\n' in slist_raw[i]:
            x = slist_raw[i].split('\n')
            slist[len(slist) - 1] = x[0]
            slist.append(x[1])
    page_data = [list(a) for a in zip(zlist, alist, slist)]
    final_data1 += page_data




