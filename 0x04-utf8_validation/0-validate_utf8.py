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
    res = True
    for i in range(len(data)):
        if data[i] >= 192 and data[i] <= 247:
            if (data[i] >= 192 and data[i] <= 223) and ((i + 1) < len(data)):
                if data[i+1] < 128 or data[i+1] > 191:
                    return False
            elif data[i] >= 224 and data[i] <= 239 and ((i + 2) < len(data)):
                if ((data[i+1] < 128 or data[i+2] < 128) or
                        (data[i+1] > 191 or data[i+2] > 191)):
                    return False
            elif data[i] >= 240 and data[i] <= 247 and ((i + 3) < len(data)):
                if ((data[i+1] < 128 or data[i+2] < 128 or data[i+3] < 128) or
                        (data[i+1] > 191 or data[i+2] > 191 or
                            data[i+3] > 191)):
                    return False
        elif (data[i] >= 247 and (data[i+1] >= 128 and data[i+1] <= 191) and
                (data[i+2] >= 128 and data[i+2] <= 191) and
                (data[i+3] >= 128 and data[i+3] <= 191)):
            return False
    return res
