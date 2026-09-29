# import necessary modules
# Import the random module to select a random word from the list of secret words
import random

# Placeholder for hidden letters in the word to guess
# if we want to change the placeholder for hidden letters, we only need to modify this constant.
# This constant and constants are capitalized in accordance with Python naming conventions for constants.
HIDDEN_WORD_PLACEHOLDER = "_"

# Number of lives the player has at the start of the game
lives: int = 6

# List of secret words for the Hangman game
secret_words: list[str] = ["python", "hangman", "challenge", "programming", "development"]


# Select a random word from the list of secret words
word_to_guess: str = random.choice(secret_words)

# List of letters that have been guessed so far
guessed_letters: list[str] = []

### I use [f-string](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) 
# to display the word to guess 
# example: https://www.w3schools.com/python/python_strings_format.asp
print(f"The word which you need to guess is: {word_to_guess}")

def ask_for_letter() -> str:
    """Prompt the user to guess a letter and return it.

    Returns:
        str: The guessed letter in lowercase.
    """
    return input("Guess a letter: ").strip().lower()

def check_guess(letter: str, word: str) -> bool:
    """Check if the guessed letter is in the word to guess.

    Args:
        letter (str): The guessed letter.
        word (str): The word to guess.

    Returns:
        bool: True if the guessed letter is in the word, False otherwise.
    """
    return letter in word


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

def update_lives(lives: int, is_good_guess: bool) -> int:
    """Update the number of lives based on whether the guessed letter is correct.

    Args:
        lives (int): The current number of lives.
        is_good_guess (bool): True if the guessed letter is correct, False otherwise.

    Returns:
        int: The updated number of lives.
    """
    if not is_good_guess:
        lives -= 1
    return lives

def is_still_alive(lives: int, guessed_word: str, word_to_guess: str) -> bool:
    """
    Check if the player is still alive based on the number of lives remaining and whether the word has been completely guessed.

    Args:
        lives (int): The number of lives remaining.
        guessed_word (str): The current state of the guessed word.
        word_to_guess (str): The word to guess.

    Returns:
        bool: True if the player has at least one life remaining and has not yet guessed the word, False otherwise.
    Example:
        >>> is_still_alive(3, "p___o_", "python")
        True
        >>> is_still_alive(0, "p___o_", "python")
        False
        >>> is_still_alive(3, "python", "python")
        False
    """
    # Better to check the guessed_word against the word_to_guess rather than checking if no HIDDEN_WORD_PLACEHOLDER in the word.
    # What if the word_to_guess contains the HIDDEN_WORD_PLACEHOLDER character(not a good practice to rely on it)?
    return lives > 0 and guessed_word != word_to_guess

def is_won(guessed_word: str, word_to_guess: str) -> bool:
    """Check if the player has won the game based on the guessed word and the word to guess.

    Args:
        guessed_word (str): The current state of the guessed word.
        word_to_guess (str): The word to guess.

    Returns:
        bool: True if the player has guessed the word correctly, False otherwise.
    Example:
        >>> is_won("python", "python")
        True
        >>> is_won("p___o_", "python")
        False
    """
    return guessed_word == word_to_guess

def is_game_over(still_alive: bool, has_won: bool) -> bool:
    """Check if the game is over based on the player's status.

    Args:
        still_alive (bool): True if the player is still alive, False otherwise.
        has_won (bool): True if the player has won the game, False otherwise.

    Returns:
        bool: True if the game is over, False otherwise.
    """
    return not still_alive or has_won


# Boolean variable to track if the player is still alive
still_alive: bool = True

# Boolean variable to track if the player has won the game
has_won: bool = False

# Main game loop
# The loop will continue for as long as the player is still alive.
while not is_game_over(still_alive, has_won):

    # Ask the user for a letter and store it in a variable
    guessed_letter: str = ask_for_letter()
    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guessed_letter)
    # Get the current state of the guessed word based on the letters guessed so far
    guessed_word: str = get_already_guessed_word(word_to_guess, guessed_letters)
    # Check if the guessed letter is in the word to guess and store the result in a variable
    is_good_guess: bool = check_guess(guessed_letter, word_to_guess)
    # Check if the player has won the game based on the current guessed word and the word to guess.
    has_won = is_won(guessed_word, word_to_guess)
    # Update the number of lives based on whether the guessed letter is correct
    lives = update_lives(lives, is_good_guess)
    # Check if the player is still alive after updating the number of lives
    still_alive = is_still_alive(lives, guessed_word, word_to_guess)

    # Display a message based on whether the guessed letter is correct or not
    if is_good_guess:
        print("Good guess!")
    else:
        print("Not in the word.")
        print(f"Lives remaining: {lives}")


    # Display the word with already guessed letters
    print(get_already_guessed_word(word_to_guess, guessed_letters))
    print()  # Print an empty line for better readability between guesses
else:
    if has_won:
        print("Congratulations! You've guessed the word correctly!")
    else:
        print(f"Game over! The word was: {word_to_guess}")