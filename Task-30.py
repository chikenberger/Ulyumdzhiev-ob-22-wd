def count_vowels_consonants(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

string = input("Введите строку: ")

vowel_count, consonant_count = count_vowels_consonants(string)

print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)
