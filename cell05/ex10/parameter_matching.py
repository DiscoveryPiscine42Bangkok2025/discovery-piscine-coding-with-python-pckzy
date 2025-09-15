import sys

def main():
    if (len(sys.argv) != 2):
        print('none')
    else:
        txt = input('What was the parameter? ')
        print('Good job!' if txt == sys.argv[1] else 'Nope, sorry...')

main()