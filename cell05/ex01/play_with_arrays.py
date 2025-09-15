def add_two(num):
    return num + 2

def main():
    numbers = [2, 8, 9, 48, 8, 22, -12, 2]
    new_arr = list(map(add_two, numbers))

    print(f'Original array: {numbers}\nNew array: {new_arr}')

main()