#!/usr/bin/env python3

import sys

def gcd(a,b):
	t = b
	b = a % b
	
	if b == 0:
		return t
	else:
		return gcd(t,b)
		
def main(argv):
	if (len(sys.argv) != 3):
		sys.exit('Usage: gcd.py <a> <b>')
	
	print(gcd(int(sys.argv[1]),int(sys.argv[2])))

if __name__ == "__main__":
	main(sys.argv[1:])