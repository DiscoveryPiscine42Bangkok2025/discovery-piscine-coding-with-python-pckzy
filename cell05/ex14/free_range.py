import sys

def main():
    if (len(sys.argv) != 3):
        print('none')
    else:
        j = -1 if (int(sys.argv[1]) > int(sys.argv[2])) else 1
        print([i for i in range(int(sys.argv[1]), int(sys.argv[2])+j, j)])

main()