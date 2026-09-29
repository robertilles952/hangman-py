# import necessary modules
# Import the random module to select a random word from the list of secret words
import random

# Placeholder for hidden letters in the word to guess
# if we want to change the placeholder for hidden letters, we only need to modify this constant.
# This constant and constants are capitalized in accordance with Python naming conventions for constants.
HIDDEN_WORD_PLACEHOLDER = "_"

# List of secret words for the Hangman game
secret_words: list[str] = ["python", "hangman", "challenge", "programming", "development"]


# Select a random word from the list of secret words
word_to_guess: str = random.choice(secret_words)

# List of letters that have been guessed so far
guessed_letters: list[str] = ['a']

### I use [f-string](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) 
# to display the word to guess 
# example: https://www.w3schools.com/python/python_strings_format.asp
print(f"The word which you need to guess is: {word_to_guess}")


def get_already_guessed_word(word: str, guessed_letters: list[str]) -> str:
    """Return the word with already guessed letters revealed and hidden letters replaced by the placeholder.

    Args:
        word (str): The word to guess.
        guessed_letters (list[str]): The list of letters that have been guessed so far.

    Returns:
        str: The word with guessed letters revealed and hidden letters replaced by the placeholder.
    Example:
        >>> get_already_guessed_word("python", ["p", "o"])
        'p___o_'
    """

    result: str = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            # Consants can be used without sending them as parameters
            # Note that if we are moving this function to another module, we need to import the constant there as well.
            # (if we do not, want to do that, we have to pass it as a parameter)
            result += HIDDEN_WORD_PLACEHOLDER
    return result


# Display the word with already guessed letters
print(get_already_guessed_word(word_to_guess, guessed_letters))