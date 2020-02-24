#!/bin/python3

import timeit
import sys


def repLetter(string):
	for l in string:
		if string.count(l) > 1:
			return l

string = 'Intergalactic'
print('string: ', string)
result = repLetter(string)
print('1st repeated letter: ', result)

# Time complexity:
tcode = """
def repCount(string):
	for l in string:
		if string.count(l) > 1:
			return l

string = 'Intergalactic'
repCount(string)
"""

time_comp = timeit.repeat(stmt=tcode, repeat=10)
print('min time: ', min(time_comp), 'second')
print('max time: ', max(time_comp), 'second')

# Space complexity:
print('space usage: ', sys.getsizeof(result) + sys.getsizeof(string), 'bytes')