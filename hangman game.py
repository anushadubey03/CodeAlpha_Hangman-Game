#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

def choose_word():
    words = ["python", "hangman", "game", "jupyter", "notebook", "programming", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(display_word(word, guessed_letters))

    while "_" in display_word(word, guessed_letters) and incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(f"Sorry, {guess} is not in the word.")
        else:
            print(f"Good guess! {guess} is in the word.")

        print(display_word(word, guessed_letters))
        print(f"Attempts left: {max_attempts - incorrect_guesses}")

    if "_" not in display_word(word, guessed_letters):
        print("Congratulations! You guessed the word.")
    else:
        print(f"Sorry, you ran out of attempts. The word was '{word}'.")

hangman()


# In[ ]:




