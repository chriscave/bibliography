#!/usr/bin/env python

import sys
import os
import pandas as pd

path_to_bib_dir = "/home/chris/bib"
bib_columns = ["author", "title", "year", "primary-topic", "secondary-topic", "tags",
               "last-opened", "frequency", "importance"]

if os.path.isdir(path_to_bib_dir) == False:
    os.makedirs(path_to_bib_dir)


def create_bib(name_of_bib: str):
    path_to_new_bib = path_to_bib_dir + "/" + name_of_bib
    if os.path.isdir(path_to_new_bib) == True:
        print("A bibliography of this name already exists!")
    else:
        os.makedirs(path_to_new_bib)
        df = pd.DataFrame(columns=bib_columns)
        df.to_csv(path_to_new_bib + "/" + name_of_bib + ".csv")


if len(sys.argv) == 4 and sys.argv[1] == "create" and sys.argv[2] == "bib":
    create_bib(sys.argv[3])


def add_to_bib(name_of_bib: str):
    path_to_bib_csv = path_to_bib_dir + "/" + name_of_bib + "/" + name_of_bib + ".csv"
    if os.path.isfile(path_to_bib_csv) == False:
        print("No bibliography of that name exists!")
    else:
        df = pd.read_csv(path_to_bib_csv)
        df.iloc[[0]] = [0,0,0,0,0,0,0,0,0] #todo figure out how to append to a Dataframe and how to retrieve meta-data from a pdf
        print(df)

if len(sys.argv) ==3 and sys.argv[1] == "add":
    add_to_bib(sys.argv[2])