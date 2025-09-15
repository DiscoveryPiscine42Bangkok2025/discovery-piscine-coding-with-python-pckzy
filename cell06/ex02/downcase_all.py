import sys

def downcase_it(s: str):
    return s.lower()

def main():
    if (len(sys.argv) == 1):
        print('none')
    else:
        for i in range(len(sys.argv)-1):
            print(downcase_it(sys.argv[i+1]))
main()