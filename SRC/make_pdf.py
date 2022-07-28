
import subprocess
import sys
import os

from get_output_name import get_output_name
from os.path         import basename, isfile

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

    # Getting ouput name
    oname = get_output_name(src, dst)
    print(f'** Writing to file "{oname}"')

    # Creating pdf file
    result = subprocess.run(['pdflatex', '-halt-on-error', '-jobname', oname, src],
                            capture_output=True, text=True)

    if (result.returncode != 0):
        msg  = f'** Error: There was an error processing the Latex files. See {oname}.log'
        msg += f' for more details'
        print(msg)

    # Need to run the pdflatex command again for building thing like table of contents
    # and appendecies
    result = subprocess.run(['pdflatex', '-halt-on-error', '-jobname', oname, src],
                            capture_output=True, text=True)

    return
