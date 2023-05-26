def count_characters(input_string):
    character_count = {}

    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

string = input("Введите строку: ")

result = count_characters(string)

for char, count in result.items():
    print(f"Символ '{char}': {count} раз(а)")
