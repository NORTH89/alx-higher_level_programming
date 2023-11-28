#!/usr/bin/python3
def uppercase(str):
    new = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            new += chr(ord(char) - 32)
        else:
            new += char
    print("{:s}".format(new))
