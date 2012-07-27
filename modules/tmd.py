#!/usr/bin/env python
'''
tmd.py - Jenni's The Michigan Difference Module
Copyright 2012 - Kyle Lady
Derived from the TWSS module
Licensed under the Eiffel Forum License 2.

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
'''

import os
import pprint
import random
import re
import sys
import urllib2

if not os.path.exists('modules/tmd.txt'):
    with open('modules/tmd.txt', 'w') as f:
        url = 'http://www.themichdiff.com/best-all-time?page='
        tmd_re = re.compile(r'<div class="nodebody">([^<>]*)</div>', re.DOTALL)

        print 'Now creating TMD database. This will take a few minutes.',
        for page in range(1,16):
            sys.stdout.flush()
            print '.',
            curr_url = url + str(page)
            html = urllib2.urlopen(curr_url)
            story_list = tmd_re.findall(html.read())
            for story in story_list:
                f.write("%s\n" % story.lstrip('\n'))

def tmd(jenni, input):
    user_quotes = None
    with open('modules/tmd.txt') as f:
        scraped_quotes = frozenset([line.rstrip() for line in f])
    if os.path.exists('modules/tmd_user_added.txt'):
        with open('modules/tmd_user_added.txt') as f2:
            user_quotes = frozenset([line.rstrip() for line in f2])
    quotes = scraped_quotes.union(user_quotes) if user_quotes else scraped_quotes
    quote = random.choice(list(quotes))
    jenni.say(quote)

tmd.commands = ['tmd']
tmd.priority = 'low'
tmd.thread = False

if __name__ == '__main__':
    print __doc__.strip()
