age = int(input('Please tell me yoyr age: '))
print(f'You are currently {age} years old.')

plus = 10
for i in range(3):
    print(f"In {plus*(i+1)} years, you'll be {age+(plus*(i+1))} years old.")