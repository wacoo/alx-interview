#!/usr/bin/python3
''' Write a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code>
'''
from sys import stdin


counter = 0
tfile_size = 0
scodes = [200, 301, 400, 403, 404, 405, 500]
code_cnt = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
for line in stdin:
    code_no = line.strip().split(' ')
    if counter == 10:
        counter = 0
        print('File size: {}'.format(tfile_size))
        for key, val in code_cnt.items():
            if val != 0:
                print('{}: {}'.format(key, val))
    else:
        if int(code_no[-2]) in scodes:
            code_cnt[int(code_no[-2])] += 1
        tfile_size += int(code_no[-1])
        counter += 1
