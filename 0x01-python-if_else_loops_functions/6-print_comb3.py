#!/usr/bin/python3
for i in range(0, 9):
    j = i + 1
    while j <= 9:
        print("{:d}{:d}".format(i, j), end='')
        print(end='\n' if i == 8 else ", ")
        j += 1
