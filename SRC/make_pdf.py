
import subprocess
import sys
import os

from get_output_name import get_output_name
from pdflatex        import PDFLaTeX as pdftex
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
    You will need to use the python package pdflatex. If you don't have it installed,
    use the command "pip install pdflatex" to install it.

NOTES:
    Some notes here

    VARIABLES (Important non IO variables):
        NONE
"""
def make_pdf(src, hflag):

    # Checking that the file in "src" exists
    if (not isfile(src)):
        msg = f'** ERROR: Cannot find the file "{src}"'
        print(msg)
        return

    pdf_obj = pdftex.from_texfile(src)
    pdf_file, log, cmpld_proc = pdf_obj.create_pdf(keep_pdf_file=True, keep_log_file=True)

    if (cmpld_proc.returncode != 0):
        last_dot = src.rindex('.')
        log_name = f'{src[:last_dot]}.log'
        msg  = f'\n** ERROR: There was a problem compiling the given tex documents. See'
        msg += f' "{log_name}" for details'
        print(msg)

    return
