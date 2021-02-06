#!/usr/bin/env python3

import sys

def palindrome(s):
	chars = []
	for c in s:
		if c.isalnum():
			chars.append(c)
	return chars == chars[::-1]

for line in sys.stdin:
	line = line.strip().lower()
	print(palindrome(line))
