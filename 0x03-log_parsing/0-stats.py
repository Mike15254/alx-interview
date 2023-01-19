#!/usr/bin/python3
'''
computes metrics using log formatted input from stdin
'''

import sys


total_file_size = 0
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}


def print_stats():
    '''prints required log stats'''
    print('File size: {}'.format(total_file_size))
    keys = sorted(status_codes.keys())
    for i in range(len(keys)):
        code = keys[i]
        if status_codes[code] != 0:
            print('{}: {}'.format(code, status_codes[code]))


try:
    for pos, line in enumerate(sys.stdin, start=1):
        matches = [tmp_line.strip() for tmp_line in line.split()]
        try:
            status_code = matches[-2]
            file_size = int(matches[-1])
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
            total_file_size += file_size
        except Exception:
            pass
        if pos % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
