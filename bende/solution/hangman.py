# import necessary modules
# Import the random module to select a random word from the list of secret words
import random

# --------------------------- CONSTANTS ---------------------------

# Number of lives the player has at the start of the game
INITIAL_LIVES: int = 6

# List of secret words for the Hangman game
SECRET_WORDS: list[str] = ["python", "hangman", "challenge", "programming", "development"]

# Placeholder for hidden letters in the word to guess
# if we want to change the placeholder for hidden letters, we only need to modify this constant.
# This constant and constants are capitalized in accordance with Python naming conventions for constants.
HIDDEN_WORD_PLACEHOLDER = "_"


# --------------------------- FUNCTIONS ---------------------------

def ask_for_letter() -> str:
    """
    Prompt the user to guess a letter and return it.
    
    Only a single letter is considered valid.
    Returns:
        str: The guessed letter in lowercase.
    """

    is_valid_guess: bool = False
    while not is_valid_guess:
        current_guess: str = input("Guess a letter: ").strip().lower()
        is_valid_guess = current_guess.isalpha() and len(current_guess) == 1
        if not is_valid_guess:
            print("Invalid input. Please enter a single letter.")

    return current_guess

def append_guessed_letter(letter: str, guessed_letters: list[str]) -> bool:
    """
    Append the guessed letter to the list of guessed letters if it hasn't been guessed already.

    Args:
        letter (str): The guessed letter.
        guessed_letters (list[str]): The list of letters that have been guessed so far.

    Returns:
        bool: True if the letter was added to the list, False if it was already in the list.
    """
    if letter not in guessed_letters:
        # since the guessed_letter list is not a copy of the original list(like letter parameter), appending to it will modify the original list.
        # this means that the original list of guessed letters will be updated directly.
        # Therefore, any changes made to the guessed_letters list inside this function will be reflected outside the function as well.
        # This behavior is important to understand when working with mutable objects in Python.(this list object reflects the same object in memory as the original list)
        # In this case, the function modifies the list in place rather than returning a new list.
        # This behaviour is known as "modifying a mutable object in place."
        guessed_letters.append(letter)
        return True
    else:
        return False

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

def ask_to_play_again():
    """
    Ask the player if they want to play again.

    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    valid_yes_responses = ["yes", "y"]
    valid_no_responses = ["no", "n"]
    valid_responses = valid_yes_responses + valid_no_responses

    response: str = input(f"Do you want to play again? ({'/'.join(valid_responses)}): ").strip().lower()
    
    while response not in valid_responses:
        response = input(f"Please enter a valid response ({'/'.join(valid_responses)}): ").strip().lower()
    
    return response in valid_yes_responses


# --------------------------- MAIN GAME LOOP ---------------------------

def run_hangman_round():
    """Run a single round of the Hangman game."""

    # Number of lives the player has at the start of the game
    lives: int = INITIAL_LIVES

    # List of secret words for the Hangman game
    secret_words: list[str] = SECRET_WORDS


    # Select a random word from the list of secret words
    word_to_guess: str = random.choice(secret_words)

    # List of letters that have been guessed so far
    guessed_letters: list[str] = []

    ### I use [f-string](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) 
    # to display the word to guess 
    # example: https://www.w3schools.com/python/python_strings_format.asp
    print(f"The word which you need to guess is: {word_to_guess}")


    # Boolean variable to track if the player is still alive
    still_alive: bool = True

    # Boolean variable to track if the player has won the game
    has_won: bool = False

    # The loop will continue for as long as the player is still alive.
    while not is_game_over(still_alive, has_won):

        # Ask the user for a letter and store it in a variable
        guessed_letter: str = ask_for_letter()
        
        # Add the guessed letter to the list of guessed letters
        is_new_guess: bool = append_guessed_letter(guessed_letter, guessed_letters)
        if not is_new_guess:
            print(f"You have already guessed the letter '{guessed_letter}'.")
            continue

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

def main():
    # Boolean variable to track if the player is still alive
    still_playing: bool = True

    # Main game loop
    # The loop will continue for as long as the player wants to keep playing.
    while still_playing:
        run_hangman_round()

        # After each round, ask the player if they want to play again
        still_playing = ask_to_play_again()


# --------------------------- ENTRY POINT ---------------------------

# Python sets __name__ to "__main__" when this file is run directly.
# This check starts the game only then; importing this file from another
# Python file will not start the game automatically.
# Learn more: https://docs.python.org/3/library/__main__.html#name-main
if __name__ == "__main__":
    main()
