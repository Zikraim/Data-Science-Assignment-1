def count_vowels(text):
    """
    Counts the number of vowels in a string.
    """
    vowels = "aeiouAEIOU"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    return count


# Example usage
user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))