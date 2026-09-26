import random

print("Welcome to Hangman!")

words = ["kecske", "alma", "laptop", "telefon", "automobil"]
word = random.choice(words)
guesses = []
lives = 6

while True: 
    given_letter = input("give me a letter:")
    if given_letter in guesses:
        print("Letter already given.")
        continue
    else:
        guesses.append(given_letter)
    def show_hidden_word(secret_word, guessed_letters, lives):
        word_i_need_to_guess = " "
        is_good_guess = False
        
        for letter in secret_word:
            if letter in guessed_letters:
                word_i_need_to_guess = word_i_need_to_guess + letter
                is_good_guess = True
                print("Good guess!")
            else:
                word_i_need_to_guess = word_i_need_to_guess + "_"
                print("Not in the word!")
        if is_good_guess == False:
                    lives -= 1
        return word_i_need_to_guess, is_good_guess, lives
    
    
    hidden_word = show_hidden_word(word, guesses, lives)
    lives = hidden_word[2]
    print(hidden_word[2])
    print(hidden_word[0])
    print(hidden_word[1])

