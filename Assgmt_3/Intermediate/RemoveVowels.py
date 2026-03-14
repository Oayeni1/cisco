def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char not in vowels:
            result += char

    return result

# Example usage
word = ("God is Good & His Blessing is on us")
print(remove_vowels(word))