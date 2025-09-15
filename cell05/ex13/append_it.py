import sys

def main():
    if (len(sys.argv) == 1):
        print('none')
    else:
        for i in range(len(sys.argv)-1):
            text = sys.argv[i+1]
            if text[-3:] != 'ism':
                print(f'{text}ism')
                
main()