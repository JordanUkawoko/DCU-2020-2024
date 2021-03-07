#!/usr/bin/env python3

def check_even_odd(numbers):
	even = []
	odd = []
	for x in numbers:
		if (x % 2 == 0):
			even.append(x)
		else:
			odd.append(x)
	print("the even numbers are:", even)
	print("the odd numbers are:", odd)

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
check_even_odd(list)
