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
    for val in range(len(data)):
        if data[0] >= 192 and data[0] <= 247:
            if data[0] >= 192 and data[0] <= 223:
                if data[1] < 128 or data[1] > 191:
                    return False
            elif data[0] >= 224 and data[0] <= 239:
                if (((data[1] and data[2]) < 128) or
                        ((data[1] and data[2]) > 191)):
                    return False
            elif data[0] >= 240 and data[0] <= 247:
                if (((data[1] and data[2] and data[3]) < 128) or
                        ((data[1] and data[2] and data[3]) > 191)):
                    return False
    return True
