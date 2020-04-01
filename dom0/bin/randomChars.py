#!/usr/bin/python

import sys
import string
import random

print "randomChars.py"
print "123456789-123456789-123456789-123456789-123456789-"
rows = 10
line_length = 80
#if len(sys.argv) >= 2:
#    rows = int(sys.argv[1])
#if len(sys.argv) >= 3:
#    line_length = int(sys.argv[2])

if len(sys.argv) >= 2:
    punctuation = sys.argv[1]
else:
    punctuation = string.punctuation

chars = ""
chars += string.ascii_letters *5 
chars += string.digits *5
chars += punctuation

#while True:
for x in range(rows):
    out_str = ""
    for x in xrange(line_length):
        out_str += chars[random.randint(0, len(chars) - 1)]
    print out_str

print

