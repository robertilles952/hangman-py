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
    def show_hidden_word(secret_word, guessed_letters):
        word_i_need_to_guess = " "
        
        for letter in secret_word:
            if letter in guessed_letters:
                word_i_need_to_guess = word_i_need_to_guess + letter                
            else:
                word_i_need_to_guess = word_i_need_to_guess + "_"
                
        return word_i_need_to_guess
    
    def count_lives(lives, given_letter, hiding_one):
        if given_letter in hiding_one:
            print("Good guess!")
        else:
            lives -= 1
            print("Not in the word!")
        #print("Remaining lives : " + str(lives))
        #print("Hello from count lives:" + str(lives), str(given_letter), hiding_one)
        return lives
    
    hidden_word = show_hidden_word(word, guesses)
    how_much_life = count_lives(lives, given_letter, hidden_word)
    lives = how_much_life
    print("Remaining lives : " + str(how_much_life))
    print(hidden_word)

