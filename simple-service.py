#! /usr/bin/python3

import sys, time

while True:
    print('test out', flush=True)
    print('test error', file=sys.stderr, flush=True)
    time.sleep(5)
