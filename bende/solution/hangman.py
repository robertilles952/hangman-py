# import necessary modules
import random

# List of secret words for the Hangman game
secret_words: list[str] = ["python", "hangman", "challenge", "programming", "development"]

word_to_guess: str = random.choice(secret_words)

### I use [f-string](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) 
# to display the word to guess 
# example: https://www.w3schools.com/python/python_strings_format.asp
print(f"The word which you need to guess is: {word_to_guess}")