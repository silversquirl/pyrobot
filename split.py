#!/usr/bin/env python3
try:
    from lxml import etree
except ImportError:
    from xml.etree import ElementTree as etree
import sys
import os.path

filename = sys.argv[1]
prefix = os.path.splitext(filename)[0]

pick = etree.parse(filename).getroot()
for i, flame in enumerate(pick):
    fn = "{}_{}.flam3".format(prefix, i)
    with open(fn, "wb") as f:
        f.write(etree.tostring(flame))
        print(fn)
