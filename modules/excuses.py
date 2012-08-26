#!/usr/bin/env python
"""
excuses.py - Jenni Excuses Module
Copyright 2012, Kyle Lady, kylelady.com
Licensed under the Eiffel Forum License 2.

quotes from http://pages.cs.wisc.edu/~ballard/bofh/excuses

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import os
import random

quote_path = 'modules/excuses.dat'

quotes = []

if os.path.exists(quote_path):
    with open(quote_path) as f:
        quotes = [s.rstrip('\n') for s in f]

def excuses(jenni, input):
    '''say something excuses-y when someone says "excuses" '''

    if len(quotes) > 0:
        jenni.say(random.choice(quotes))

excuses.rule = r'^excuses*$'
excuses.priority = 'low'
excuses.rate = 1

if __name__ == '__main__':
    print __doc__.strip()
