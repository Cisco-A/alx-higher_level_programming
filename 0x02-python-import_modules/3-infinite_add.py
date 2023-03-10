#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    sum = 0
    while i < len(argv):
        convert_num = int(argv[i])
        sum += convert_num
    print(sum)
