#!/usr/bin/env python
"""
pirate.py - Jenni Pirate Module
Copyright 2012, Kyle Lady, kylelady.com
Licensed under the Eiffel Forum License 2.

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import re
import urllib2

pirate_page = 'http://gangstaname.com/quotes/pirate'
pirate_regex = re.compile(r'''quote: '(.*[^\\])'.*''')

def pirate(jenni, input):
    '''say something piratey when someone says "arr" '''

    url = urllib2.urlopen(pirate_page)
    content = ''.join(url.readlines())
    r = pirate_regex.search(content)
    if r is not None:
        jenni.say(r.group(1).decode('string_escape'))

pirate.rule = r'(.*\s|^)y?a+r+(\s|$)'
pirate.priority = 'low'
pirate.rate = 30

if __name__ == '__main__':
    print __doc__.strip()
