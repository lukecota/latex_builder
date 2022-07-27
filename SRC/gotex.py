#!/usr/bin/env python3

import argparse

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
    descript = '''Application description here'''
    arg_help = '''Description of argument here'''
    opt_help = '''Description of option here'''
    opno_help = '''Description of option with no arguments'''

    parser = argparse.ArgumentParser(description = descript)
    parser.add_argument('arg', help = arg_help)
    parser.add_argument('-o', '--opt', help = opt_help, metavar = 'opt_display_name')
    parser.add_argument('-n', '--no', help = opno_help, action = 'store_true',
                        default = False)

    # Create list of keys to the args dictionary
    args = parser.parse_args().__dict__

    return

######################################### main ###########################################
if (__name__ == '__main__'):
    main()

