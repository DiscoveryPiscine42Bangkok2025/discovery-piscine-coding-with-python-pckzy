def main():
    numbers = [2, 8, 9, 48, 8, 22, -12, 2]
    new_arr = [x + 2 for x in numbers if x > 5]

    print(f'{numbers}\n{new_arr}')

main()