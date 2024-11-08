#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    j = 1
    arg = len(argv) - 1

    print(f"{arg} {'argument' if arg == 1 else 'arguments'}", end="")
    print(f"{'.' if arg == 0 else ':'}")
    while (j <= arg):
        print(f"{j}: {argv[j]}")
        j += 1
