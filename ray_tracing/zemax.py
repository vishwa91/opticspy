#!/usr/bin/env python

'''
Zemax .zmx file reading utility. Returns a Lens class
'''

#import lens

# List of starting tokens
TOKENS = ['VERS',
          'MODE',
          'NAME',
          'NOTE',
          'PFIL',
          'UNIT',
          'ENPD',
          'ENVD',
          'GFAC',
          'GCAT',
          'RAIM',
          'PUSH',
          'SDMA',
          'FTYP',
          'ROPD',
          'PICB',
          'XFLN',
          'YFLN',
          'FWGN',
          'VDXN',
          'VDYN',
          'VCYN',
          'VANN',
          'WAVM',
          'PWAV',
          'POLS',
          'GLRS',
          'GSTD',
          'NSCD',
          'COFN',
          'SURF',
          'TYPE',
          'CURV',
          'HIDE',
          'MIRR',
          'SLAB',
          'DISZ',
          'DIAM',
          'POPS',
          'COMM',
          'STOP',
          'COAT',
          'GLAS',
          'FLAP',
          'BLNK',
          'TOL',
          'MNUM',
          'MOFF']

def read_zmx(filename):
    '''
        Function to read a .zmx file and return a lens class

        Inputs:
            filename: Name of file to read

        Outputs:
            lens: A Lens class with all configurations in place
    '''
    # Read all lines first
    f = open(filename, 'r')

    lines = f.readlines()
    return lines

def _parse_line(line):  
    '''
        Parse a single line and find out tokens and values.

        Inputs:
            line: Single line string with tokens separated by spaces
    '''
    # First split
    tokens = line.split(' ')

    # Convert any numbers in tokens
    for idx in range(len(tokens)):
        try:
            tokens[idx] = float(tokens[idx])
        except:
            pass

    return tokens
