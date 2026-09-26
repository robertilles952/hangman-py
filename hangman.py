import random

print("Welcome to Hangman!")

words = ["kecske", "alma", "laptop", "telefon", "automobil"]
word = random.choice(words)
guesses = []

while True: 
    given_letter = input("give me a letter:")
    if given_letter in guesses:
        continue
    else:
        guesses.append(given_letter)
    def show_hidden_word(secret_word, guessed_letters):
        word_i_need_to_guess = " "
        for letter in secret_word:
            if letter in guessed_letters:
                word_i_need_to_guess = word_i_need_to_guess + letter
                print("Good guess!")
            else:
                word_i_need_to_guess = word_i_need_to_guess + "_"
                print("Not in the word!")

        return word_i_need_to_guess

    hidden_word = show_hidden_word(word, guesses)
    print(hidden_word)

