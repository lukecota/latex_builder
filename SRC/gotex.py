#!/usr/bin/env python3

import argparse

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
    NONE

NOTES:
    Some notes here

    VARIABLES (Important non IO variables):
        NONE
"""
def main():
    descript = '''Build Latex files into a PDF'''
    src_help = '''Path to main Latex file'''
    bem_help = '''Build a Beamer project'''
    hyp_help = '''Use this option to add hyperlinks to your document'''
    out_help = '''Path to output pdf file'''

    parser = argparse.ArgumentParser(description = descript)
    parser.add_argument('SOURCE', help = src_help)
    parser.add_argument('-b', '--beamer', help = bem_help, action = 'store_true',
                        default = False)
    parser.add_argument('-H', '--hyperlink', help = hyp_help, action = 'store_true',
                        default = False)
    parser.add_argument('-o', '--output', help = out_help)

    # Create list of keys to the args dictionary
    args = parser.parse_args().__dict__

    if (not args['beamer']):
        make_pdf(args['SOURCE'], args['hyperlink'], args['output'])

    else:
        print(f'NOT YET IMPELMENTED')

    return

######################################### main ###########################################
if (__name__ == '__main__'):
    main()

