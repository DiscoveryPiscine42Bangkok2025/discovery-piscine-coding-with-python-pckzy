import sys

def shrink(s: str):
    return s[:8]

def enlarge(s: str):
    return f'{s}{'Z'*(8-len(s))}'

def main():
    if (len(sys.argv) == 1):
        print('none')
    else:
        for i in range(len(sys.argv)-1):
            word = sys.argv[i+1]
            if (len(word) > 8):
                print(shrink(word))
            elif (len(word) < 8):
                print(enlarge(word))
            else:
                print(word)

main()