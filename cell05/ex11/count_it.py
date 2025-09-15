import sys

def main():
    if (len(sys.argv) == 1):
        print('none')
    else:
        count = len(sys.argv)-1
        print(f'parameters: {count}')
        for i in range(count):
            print(f'{sys.argv[i+1]}: {len(sys.argv[i+1])}')

main()