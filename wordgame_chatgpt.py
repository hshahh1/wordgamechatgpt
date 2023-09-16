#using chatgpt

import random

# Dictionary of words and hints
word_data = {
    "apple": "A fruit that is red or green and grows on trees.",
    "banana": "A yellow fruit that monkeys love to eat.",
    "cherry": "A small, round fruit that is usually red or pink.",
    "grape": "A small, juicy fruit that can be purple, green, or red.",
    "orange": "A citrus fruit known for its orange color and juice.",
    "pear": "A fruit with a sweet and juicy flesh and a narrow neck.",
    "strawberry": "A red fruit with tiny seeds on the outside."
}

# Select a random word and its hint
word_to_guess, hint = random.choice(list(word_data.items()))

# Initialize variables
attempts = 6
guessed_letters = []

# Display underscores for unguessed letters
def display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    return display

# Game loop
while attempts > 0:
    print("\nAttempts left:", attempts)
    print("Hint:", hint)
    print("Word:", display_word(word_to_guess, guessed_letters))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

    if set(word_to_guess) == set(guessed_letters):
        print("Congratulations! You guessed the word:", word_to_guess)
        break

if attempts == 0:
    print("Out of attempts! The word was:", word_to_guess)