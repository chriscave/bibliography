#!/usr/bin/python

import sys
import os
import pandas as pd

path_to_bib_dir = "/home/chris/bib"
bib_columns = ["author", "title", "year", "primary-topic", "secondary-topic", "tags",
           "last-opened","frequency","importance"]

if os.path.isdir(path_to_bib_dir) == False:
    os.makedirs(path_to_bib_dir)

def create_bib(name: str) -> str:
    path_to_new_bib = path_to_bib_dir + "/" + name
    if os.path.isdir(path_to_new_bib) == True:
        print("A bibliography of this name already exists!")
    else:
        os.makedirs(path_to_new_bib)
        df = pd.DataFrame(columns=bib_columns)
        df.to_csv(path_to_new_bib +"/"+name)


if len(sys.argv) == 4 and sys.argv[1] == "create" and sys.argv[2] == "bib":
    create_bib(sys.argv[3])
