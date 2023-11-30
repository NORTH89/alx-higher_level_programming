#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    else:
        if len(sys.argv) - 1 == 1:
            print("1 argument:")
            print("1: {}".format(sys.argv[1]))
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
            i = 0
            while i < len(sys.argv) - 1:
                print("{}: {}".format(i + 1, sys.argv[i + 1]))
                i += 1
