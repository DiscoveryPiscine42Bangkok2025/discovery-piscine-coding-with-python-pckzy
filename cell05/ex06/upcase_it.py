import sys

def main():
    print('none' if len(sys.argv) != 2 else sys.argv[1].upper())

main()