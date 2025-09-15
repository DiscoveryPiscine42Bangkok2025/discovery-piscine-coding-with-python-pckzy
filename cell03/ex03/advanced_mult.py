i = 0
while (i <= 10):
    count = 0
    print(f'Table de {i}:', end=" ")
    while (count <= 10):
        print(count*i, end=" ")
        count += 1
    i += 1
    print()