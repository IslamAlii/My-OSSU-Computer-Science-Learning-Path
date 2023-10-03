def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count = count + 1
    return count

# Example usage:
word = 'banana'
letter_to_count = 'a'
result = count(word, letter_to_count)
print(result)  # This will print the count of 'a' in the word 'banana'