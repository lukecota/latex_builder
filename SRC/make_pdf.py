
import os

from os.path import basename, isfile

"""
Created on Wed Jul27 16:43:57 2022

@author: Luke Cota

PURPOSE:
    Compiles a Latex project into pdf

INPUTS:
    src   = str,     Path to main Latex document
    hflag = logical, If True add hyperlinks
    dst   = str,     Path to output file. If "None" then use the name from "src"

OUTPUTS:
    NONE

DEPENDENCIES:
    NONE

NOTES:
    Some notes here

    VARIABLES (Important non IO variables):
        NONE
"""
def make_pdf(src, hflag, dst):

    # Checking that the file in "src" exists
    if (not isfile(src)):
        msg = f'** ERROR: Cannot find the file "{src}"'
        print(msg)
        return

    # Setting up to build output file name
    if (dst == None):
        dst_dir = src

    else:
        dst_dir = dst

    # Getting path to folder where pdf file will be placed
    plist = dst_dir.split(os.path.sep)

    # Getting name of output file without extension
    oname = basename(dst_dir).split('.')[0]

    # Building fully quilified ouput file name
    dir_path = ''
    for indx in range(len(plist)-1):
        dir_path += f'{plist[indx]}/'

    oname = f'{dir_path}{oname}.pdf'
    print(f'** Writing to file "{oname}"')


    return
