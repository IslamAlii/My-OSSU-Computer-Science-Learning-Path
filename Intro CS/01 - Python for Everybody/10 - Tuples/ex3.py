import string

letter_freq = {}
total_char = 0

file_path = "py4e.com_code3_romeo-full.txt"  
fname = input("Enter file name: ")
fhand = open(fname)
text = fhand.read()



for char in text:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Convert to lowercase
            letter_freq[char] = letter_freq.get(char, 0) + 1
            total_char = total_char + 1

sorted_letters = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

print(sorted_letters)

for letter, freq in sorted_letters:
    print(f"{letter}: {(freq / total_char * 100): .2f}%")