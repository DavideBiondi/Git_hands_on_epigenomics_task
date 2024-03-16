#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description='Classify a sequence as DNA or RNA') #this is the description of the script
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence") #these are the options accepted by the script (Unix version and GNU version in double dash) 

if len(sys.argv) == 1: #if the user inserts only one argument (the script) but does not insert also a string sequence, the help page will be returned
    parser.print_help() #help page
    sys.exit(1) #exit code of 1, generally indicating an error, exit codes are particularly relevant in Unix systems, usually the exit status is chained
                #to conditional statements that include $? (a Bash variable indicating the exit status of the previous command in a script)

args = parser.parse_args()

# Converting the sequence to uppercase to make the script case-insensitive
seq_upper = args.seq.upper() #this automatically makes the search for regex as case insensitive

if re.search('^[ACGTU]+$', seq_upper):
    if 'T' in seq_upper and 'U' in seq_upper:
        # Excluding sequences that contain both 'T' and 'U'
        print('The sequence is invalid as it contains both T and U.')
    elif 'T' in seq_upper:
        print('The sequence is DNA') #T is exclusive of DNA
    elif 'U' in seq_upper:
        print('The sequence is RNA') #U is a base exclusive of RNA
    else:
        print('The sequence can be DNA or RNA')
else:
    print('The sequence is not DNA nor RNA')

