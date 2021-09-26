#!/usr/bin/env python3

import sys
import argparse

opts = argparse.ArgumentParser(description='Chimera Input Values')
opts.add_argument('--input-file',       type = str,     required = True,  dest = 'input_file',      default = None,                     help = 'Name of source file',               )
opts.add_argument('--output-file',      type = str,     required = True,  dest = 'output_file',     default = None,                     help = 'Name of output file',               )
opts.add_argument('--residue-change',   type = int,     required = True,  dest = 'res_change',      default = None,                     help = 'First value to change',             )
opts.add_argument('--increment',        type = int,     required = True,  dest = 'inc_val',         default = None,                     help = 'How much to increment by',          )
args = opts.parse_args()


if args.input_file == args.output_file:
    print("Don't be stupid, input and output files cannot be the same!")
    sys.exit()

f = open(args.input_file, 'r')
new_f = open(args.output_file, 'w+')

residue_first_change = args.res_change
increment_value = args.inc_val

for line in f:
    token_check = ''
    if len(line) > 3:
        token_check = line.split()[0]
    if token_check in ['ATOM', 'HETATM', 'ANISOU', 'OTHERS']:
        residue = int(line[23:27])
        if residue >= residue_first_change:
            # print(line)
            line = line[:22] + str(residue + increment_value).rjust(4) + line[26:]
            # print(line)
    new_f.write(line)
new_f.close()
f.close()
