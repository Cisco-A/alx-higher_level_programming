#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_number = len(argv) - 1
    if len(argv) == 1:
        print(f"{arg_number:d} arguments.")
    elif len(argv) == 2:
        print(f"{arg_number:d} argument:")
        print(f"{arg_number:d}: {argv[1]}")
    else:
        print(f"{arg_number:d} arguments:")
        i = 1
        while i < len(argv):
            print(f"{(i):d}: {argv[i]}")
            i += 1
