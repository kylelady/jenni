#!/usr/bin/env python
"""
theo.py - Jenni Theo Module
Copyright 2012, Kyle Lady, kylelady.com
Licensed under the Eiffel Forum License 2.

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import os
import random

quote_path = 'modules/theo.dat'

quotes = []

if os.path.exists(quote_path):
    with open(quote_path) as f:
        quotes = [s.rstrip('\n') for s in f]

def theo(jenni, input):
    '''say something theo-y when someone says "theo" '''

    if len(quotes) > 0:
        jenni.say(random.choice(quotes))

theo.rule = r'^theo$'
theo.priority = 'low'
theo.rate = 1

if __name__ == '__main__':
    print __doc__.strip()
