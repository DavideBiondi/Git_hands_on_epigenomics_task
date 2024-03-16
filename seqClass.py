#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Converting the sequence to uppercase to make the script case-insensitive
seq_upper = args.seq.upper()

if re.search('^[ACGTU]+$', seq_upper):
    if 'T' in seq_upper and 'U' in seq_upper:
        # Excluding sequences that contain both 'T' and 'U'
        print('The sequence is invalid as it contains both T and U.')
    elif 'T' in seq_upper:
        print('The sequence is DNA')
    elif 'U' in seq_upper:
        print('The sequence is RNA')
    else:
        print('The sequence can be DNA or RNA')
else:
    print('The sequence is not DNA nor RNA')

