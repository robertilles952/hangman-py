import random

def main():
    print("Welcome to Hangman!")

    words = ["kecske", "alma", "laptop", "telefon", "automobil"]
    word = random.choice(words)
    guesses = []
    lives = 6
    hidden_word = "_"

    while  lives > 0 and "_" in hidden_word: 
        given_letter = input("give me a letter:").lower()
        if not given_letter.isalpha():
            print("Not valid input!")
            continue
        if len(given_letter) > 1:
            print("Use just one letter at a time.")
            continue
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
            return lives
        
        hidden_word = show_hidden_word(word, guesses)
        how_much_life = count_lives(lives, given_letter, hidden_word)
        lives = how_much_life
        print("Remaining lives : " + str(how_much_life))
        print(hidden_word)
    if lives == 0:
        print("Game Over!""\n""The secret word was: " + word )
    if "_" not in hidden_word:
        print("WINNNER WIINER CHICKEN DINNER!")

main()

still_playing = True
while still_playing:
    answer = input("Do you want to try again? y/n")
    if "y" == answer:
        main()
    elif "n" == answer:
        still_playing = False
    else:
        print("Wrong input!")