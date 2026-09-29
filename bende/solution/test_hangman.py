from bende.solution import hangman


def test_easy_difficulty_keeps_short_words():
    words = ["cat", "piano", "watermelon"]
    difficulty = {"level": "easy", "word_length": 6}

    # Easy mode keeps words with 6 or fewer letters.
    result = hangman.select_secret_words(difficulty, words)

    assert result == ["cat", "piano"]


def test_medium_difficulty_keeps_words_from_5_to_10_letters():
    words = ["cat", "apple", "watermelon", "abcdefghijkl"]
    difficulty = {"level": "medium", "word_length": 10}

    # Medium mode skips words that are too short or too long.
    result = hangman.select_secret_words(difficulty, words)

    assert result == ["apple", "watermelon"]


def test_hard_difficulty_keeps_long_words():
    words = ["elephant", "abcdefghijkl", "abcdefghijklmnop"]
    difficulty = {"level": "hard", "word_length": 12}

    # Hard mode keeps words with at least 12 letters.
    result = hangman.select_secret_words(difficulty, words)

    assert result == ["abcdefghijkl", "abcdefghijklmnop"]


def test_new_guessed_letter_is_added_to_the_list():
    guessed_letters = []

    # The function adds the new letter to this list and says it was added.
    was_added = hangman.append_guessed_letter("a", guessed_letters)

    assert was_added is True
    assert guessed_letters == ["a"]


def test_repeated_guessed_letter_is_not_added_again():
    guessed_letters = ["a"]

    # The function says the letter is already there and leaves the list unchanged.
    was_added = hangman.append_guessed_letter("a", guessed_letters)

    assert was_added is False
    assert guessed_letters == ["a"]


def test_check_guess_returns_true_when_letter_is_in_word():
    assert hangman.check_guess("p", "python") is True


def test_check_guess_returns_false_when_letter_is_not_in_word():
    assert hangman.check_guess("z", "python") is False


def test_guessed_letters_are_shown_and_other_letters_are_hidden():
    # The guessed a and m are shown; the other letters become underscores.
    result = hangman.get_already_guessed_word("hangman", ["a", "m"])

    assert result == "_a__ma_"


def test_punctuation_in_the_word_stays_visible():
    # The hyphen and exclamation mark are not hidden like letters.
    result = hangman.get_already_guessed_word("hang-man!", ["a", "m"])

    assert result == "_a__-ma_!"


def test_correct_guess_does_not_remove_a_life():
    lives = hangman.update_lives(6, True)

    assert lives == 6


def test_wrong_guess_removes_one_life():
    lives = hangman.update_lives(6, False)

    assert lives == 5


def test_player_is_alive_with_lives_left_and_letters_to_guess():
    still_alive = hangman.is_still_alive(3, "p___o_", "python")

    assert still_alive is True


def test_player_is_not_alive_with_no_lives_left():
    still_alive = hangman.is_still_alive(0, "p___o_", "python")

    assert still_alive is False


def test_player_is_not_alive_after_guessing_the_whole_word():
    still_alive = hangman.is_still_alive(3, "python", "python")

    assert still_alive is False


def test_player_wins_when_the_guessed_word_matches():
    assert hangman.is_won("python", "python") is True


def test_player_has_not_won_while_letters_are_hidden():
    assert hangman.is_won("p___o_", "python") is False


def test_game_is_over_after_a_win_or_when_the_player_is_out_of_lives():
    # False means the game continues; True means it has ended.
    game_continues = hangman.is_game_over(True, False)
    game_ends_after_loss = hangman.is_game_over(False, False)
    game_ends_after_win = hangman.is_game_over(True, True)

    assert game_continues is False
    assert game_ends_after_loss is True
    assert game_ends_after_win is True


def test_load_words_returns_nonempty_lowercase_words():
    words = hangman.load_words()

    # There should be words in the file, and each word should be cleaned up.
    assert len(words) > 0
    for word in words:
        assert len(word) > 0
        assert word == word.lower()