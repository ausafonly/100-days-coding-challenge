import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
user_guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == user_guess:
        print(f"You chose the right letter: {letter}")
    else:
        print(f"You chose the wrong letter: {letter}")  