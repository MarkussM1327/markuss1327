# I know this isnt correct but I dont know how to make him find the biggest one
import os
os.system('cls')
import os
os.system('cls')

sentence = input('Enter a sentence - ').split()
longest_word = ''
max_length = 0  # Start with 0, so any word will be longer

for word in sentence:
    if len(word) > max_length:  # Check if the current word is longer
        max_length = len(word)  # Update the max length
        longest_word = word      # Store the longest word

print(f'The longest word is: "{longest_word}" ({max_length} letters)')




    
