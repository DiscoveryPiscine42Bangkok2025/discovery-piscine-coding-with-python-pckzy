def find_the_redheads(persons):
    return [name for name, hair in persons.items() if hair == "red"]

def main():
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    print(find_the_redheads(dupont_family))

main()