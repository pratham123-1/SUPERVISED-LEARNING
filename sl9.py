def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return {'vowels': vowel_count, 'consonants': consonant_count}


# Example usage:
input_string = "hello world"
result = count_vowels_consonants(input_string)
print(result)