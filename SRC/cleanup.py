
import glob
import subprocess

"""
Created on Wed Jul27 20:18:47 2022

@author: Luke Cota

PURPOSE:
    Cleanes up all the unnecissary files created by the pdflatex command

INPUTS:
    List all input here

OUTPUTS:
    src = str, Path to folder which is to be cleaned

DEPENDENCIES:
    NONE

NOTES:
    Some notes here

    VARIABLES (Important non IO variables):
        NONE
"""
def cleanup(src):

    extensions = ['.out', '.aux', '.log', '.toc']

    for elem in extensions:
        g_cmd = f'*{elem}'
        flist = glob.glob(g_cmd)
        for jelem in flist:
            result = subprocess.run(['rm', jelem])

    return
