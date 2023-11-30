#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    print(sys.path)
    from hidden_4 import hidden_4
    for name in dir(hidden_4):
        if not name.startswith("__"):
            print(name)
