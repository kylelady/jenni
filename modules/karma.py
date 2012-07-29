#!/usr/bin/env python
'''
jenni karma module
(c) 2012 kyle lady

tracks karma as designated by ++ and -- and spits back karma counts
'''

import os
import re
import sys
import yaml

yaml_path = 'modules/karma.yaml'

karma_tally = {}

if os.path.exists(yaml_path):
    with open(yaml_path) as f:
        karma_tally = yaml.load(f)

def writeout():
    with open(yaml_path, 'w') as f:
        yaml.dump(karma_tally, f)

def karma(jenni, input):
    item = input.group(2)
    oper = input.group(3)

    if oper not in ('++', '--'):
        raise StandardError('this shouldn\'t have happened')

    if item.lower() == input.nick.lower() and oper == '++':
        return

    try:
        karma_tally[item] += 1 if oper == '++' else -1
    except KeyError:
        karma_tally[item] = 1 if oper == '++' else -1
    writeout()
    return
karma.rule = r'(.*\s|^)(\w+)(\+\+|--).*'
karma.priority = 'high'
karma.thread = False

def say_karma(jenni, input):
    item = input.group(1)
    try:
        value = karma_tally[item]
        if value == 0:
            jenni.say('%s has neutral karma' % item)
        else:
            jenni.say('%s has karma of %d' % (item, value))
    except KeyError:
        jenni.say('%s has neutral karma' % item)
say_karma.rule = r'^karma\s+(\w+)$'
say_karma.priority = 'medium'
say_karma.thread = False
say_karma.rate = 1
