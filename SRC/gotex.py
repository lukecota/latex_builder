#!/usr/bin/env python3

import argparse

from cleanup  import cleanup
from make_pdf import make_pdf

"""
Created on Wed Jul27 16:30:19 2022

@author: Luke Cota

PURPOSE:
    Short description here

INPUTS:
    List all input here

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
def main():
    descript = '''Build Latex files into a PDF'''
    src_help = '''Path to main Latex file'''
    bem_help = '''Build a Beamer project. ** NOT YET IMPLIMENTED **'''
    hyp_help = '''Use this option to add hyperlinks to your document.
                  ** NOT YET IMPLIMENTED **'''
    cln_help = '''Clean up all unused tiles created by the pdflatex command. When this
                  option is used the SOURCE argument should be the path to the folder
                  which is to be cleand'''

    parser = argparse.ArgumentParser(description = descript)
    parser.add_argument('SOURCE', help = src_help)
    parser.add_argument('-b', '--beamer', help = bem_help, action = 'store_true',
                        default = False)
    parser.add_argument('-c', '--cleanup', help = cln_help, action = 'store_true',
                        default = False)
    parser.add_argument('-H', '--hyperlink', help = hyp_help, action = 'store_true',
                        default = False)

    # Create list of keys to the args dictionary
    args = parser.parse_args().__dict__

    if (args['cleanup']):
        cleanup(args['SOURCE'])
        return

    if (not args['beamer']):
        make_pdf(args['SOURCE'], args['hyperlink'])

    else:
        print(f'NOT YET IMPELMENTED')

    return

######################################### main ###########################################
if (__name__ == '__main__'):
    main()

