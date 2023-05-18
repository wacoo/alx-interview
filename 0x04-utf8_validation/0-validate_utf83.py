#!/usr/bin/python3
''' Write a method that determines if a given data set represents
a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handlei
the 8 least significant bits of each integer
'''


def validUTF8(data):
    ''' return True or False depending on whether the data given is UTF-8 '''
    multi = False 
    for i in range(len(data)):
        bv = format(data[i], '08b')
        nxtb = '10'
        oneb = '110'
        twob = '1110'
        threeb = '11110'
        nxt1 = ''
        nxt2 = ''
        nxt3 = ''

        if len(data) > (i + 1):
            nxt1 = format(data[i + 1], '08b')
        if len(data) > (i + 2):
            nxt2 = format(data[i + 2], '08b')
        if len(data) > (i + 3):
            nxt3 = format(data[i + 3], '08b')

        if bv[:3] == oneb and ((i + 1) < len(data)):
            multi = True
            if nxt1[:2] != nxtb:
                return False
        elif bv[:4] == twob and ((i + 2) < len(data)):
            multi = True
            if nxt1[:2] != nxtb or nxt2[:2] != nxtb:
                return False
        elif bv[:5] == threeb and ((i + 3) < len(data)):
            multi = True
            if nxt1[:2] != nxtb or nxt2[:2] != nxtb or nxt3[:2] != nxtb:
                return False
    if not multi:
        return False

    return True
