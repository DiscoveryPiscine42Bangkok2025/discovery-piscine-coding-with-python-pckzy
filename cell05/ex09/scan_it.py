import sys

def main():
    if (len(sys.argv) != 3):
        print('none')
    else:
        count = sys.argv[2].count(sys.argv[1])
        print('none' if count == 0 else count)

main()