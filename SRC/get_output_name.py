
import os

from os.path import basename, isfile

"""
Created on Wed Jul27 19:30:05 2022

@author: Luke Cota

PURPOSE:
    Creates the fully qualified file name for the output pdf file

INPUTS:
    src = str, Path to Latex source file. If dst = None, then the output name will be the
               same as the source file name
    dst = str, Path to destination file (could be None)

OUTPUTS:
    oname = str, Fully qualified file name for output pdf file

DEPENDENCIES:
    NONE

NOTES:
    Some notes here

    VARIABLES (Important non IO variables):
        NONE
"""
def get_output_name(src, dst):

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

    oname = f'{dir_path}{oname}'

    return oname
