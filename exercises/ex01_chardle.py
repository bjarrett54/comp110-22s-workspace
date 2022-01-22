"""Ex01 - Chardle - A cute step toward Wordle."""

__author__ = "730230236"


user_word_input: str = str(input("Enter a 5-character word: "))
if len(user_word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()


user_letter_input: str = str(input("Enter a single character: "))
if len(user_letter_input) != 1:
    print("Error: Character must be a single character.")
    exit()

user_search_response: str = str("searching for " + user_letter_input + " in " + user_word_input)
letter_index_count: int = int(0)


if user_letter_input == user_word_input[0]:
    print(str(user_letter_input + " found at index 0"))
    letter_index_count = letter_index_count + 1
if user_letter_input == user_word_input[1]:
    print(str(user_letter_input + " found at index 1"))
    letter_index_count = letter_index_count + 1
if user_letter_input == user_word_input[2]:
    print(str(user_letter_input + " found at index 2"))
    letter_index_count = letter_index_count + 1
if user_letter_input == user_word_input[3]:
    print(str(user_letter_input + " found at index 3"))
    letter_index_count = letter_index_count + 1
if user_letter_input == user_word_input[4]:
    print(str(user_letter_input + " found at index 4"))
    letter_index_count = letter_index_count + 1

if letter_index_count == 0: 
    print("No instances of " + user_letter_input + " found in " + user_word_input)
else:
    if letter_index_count == 1:
        print(str(letter_index_count) + " instance of " + user_letter_input + " found in " + user_word_input)
    else:
        if letter_index_count == 2:
            print(str(letter_index_count) + " instances of " + user_letter_input + " found in " + user_word_input)
        else:
            if letter_index_count == 3:
                print(str(letter_index_count) + " instances of " + user_letter_input + " found in " + user_word_input)
            else:
                if letter_index_count == 4: 
                    print(str(letter_index_count) + " instances of " + user_letter_input + " found in " + user_word_input)
                else: 
                    if letter_index_count == 5: 
                        print(str(letter_index_count) + " instances of " + user_letter_input + " found in " + user_word_input)