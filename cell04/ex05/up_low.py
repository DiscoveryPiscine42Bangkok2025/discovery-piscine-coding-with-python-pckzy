txt = input()

for i in txt:
    print(i.upper() if i.islower() else i.lower(), end="")