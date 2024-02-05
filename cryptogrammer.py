# Copyright 2024 Tanner Swett.
#
# This file is free software: you can redistribute it and/or modify it under the
# terms of version 3 of the GNU GPL as published by the Free Software
# Foundation.
#
# This file is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See version 3 of the GNU GPL for more details.

import argparse

def crypto(s):
    next_letter = 'A'
    codes = {}
    output = ''

    for c in s.lower():
        if not c.isalpha():
            output += c
        elif c in codes:
            output += codes[c]
        else:
            codes[c] = next_letter
            next_letter = chr(ord(next_letter) + 1)
            output += codes[c]

    return output

def test_crypto():
    assert crypto('Michelle Keegan') == 'ABCDEFFE GEEHIJ'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input.txt')
    parser.add_argument('--output', default='output.txt')
    args = parser.parse_args()

    input_file = open(args.input, 'r')
    output_file = open(args.output, 'w')

    for line in input_file:
        line = line.strip()
        crypted = crypto(line)
        output_file.write(f'{line},{crypted}\n')

    output_file.close()
    input_file.close()
