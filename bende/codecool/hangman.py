import random
import os

with open('text-files/countries-and-capitals.txt', 'r') as file:
    data = file.read().splitlines()
with open('text-files/lets-hang.txt', 'r') as file:
    lets_hang = file.read().splitlines()
with open('hang.txt', 'r') as file:
    hangman_pic = file.read().splitlines()
with open('text-files/game-over.txt', 'r') as file:
    game_over = file.read().splitlines()
with open('text-files/win.txt', 'r') as file:
    win = file.read().splitlines()
with open('text-files/good-bye.txt', 'r') as file:
    good_bye = file.read().splitlines()
with open('text-files/cheater.txt', 'r') as file:
    cheater = file.read().splitlines()


def game(data, lets_hang, hangman_pic, game_over, win, good_bye, cheater):
    random_choice = random.choice(data).split(' | ')
    countries = random.choice(data).split(' | ')[0]
    cities = random.choice(data).split(' | ')[1]
    level = level_function()
    lives = lives_function(level)
    word = countries_and_capitals(countries, cities, level, random_choice)
    play(word, lives, data, lets_hang, hangman_pic, game_over, win, good_bye, cheater)


def clear():
    os.system('clear')


def level_function():
    clear()
    for x in lets_hang:
        print(x)
    choose = input("Which level would you like to play?\nEasy--> Country, 7 lives: (1)\nMedium--> City, 5 lives:  (2)\nHard--> Random, 3 lives:  (3) ")
    while True:
        if choose == ("1"):
            return 1
        if choose == ("2"):
            return 2
        if choose == ("3"):
            return 3
        else:
            choose = input("That is not an option, please try again! 1/2/3!")


def lives_function(level):
    if level == 1:
        user_lives = 7
        return user_lives
    elif level == 2:
        user_lives = 5
        return user_lives
    elif level == 3:
        user_lives = 3
        return user_lives


def countries_and_capitals(countries, cities, level, random_choice):
    if level == 1:
        return (countries)

    if level == 2:
        return (cities)

    if level == 3:
        hard_choice = random.choice(random_choice)
        return hard_choice


def checking_wrong_guess(guess, guess_upper, wrong_list, lives, word,):
    if guess == 'developer.mode':
        print('Developer Mode activated. The solution is------->', word)
        return lives
    if not guess.isalpha():
        print("That is not a letter, please try again! \n", ", ".join(wrong_list))
        return lives
    if guess == 'help':
        print('Oh You noob.... this help was -2 lives points, but here is your help....', word, word, word, word, word,)
        lives = lives - 2
        return lives
    if guess in wrong_list:
        print("You have tried--->" + guess_upper + "<---letter already! Please try again! \n", ", ".join(wrong_list))
        return lives
    else:
        wrong_list.append(guess)
        lives = lives - 1
        print("You lost 1 life! Only --->", lives, "<---left!")
        return lives


def hang_graphic(hangman_pic, lives):
    if lives == 7:
        return (hangman_pic[0:24])
    elif lives == 6:
        return (hangman_pic[24:47])
    elif lives == 5:
        return (hangman_pic[47:70])
    elif lives == 4:
        return (hangman_pic[70:93])
    elif lives == 3:
        return (hangman_pic[93:116])
    elif lives == 2:
        return (hangman_pic[116:139])
    elif lives == 1:
        return (hangman_pic[139:162])
    elif lives == 0:
        return (hangman_pic[162:185])


def play(word, lives, data, lets_hang, hangman_pic, game_over, win, good_bye, cheater):
    clear()
    wrong_list = []
    word_list = list(word)
    hang_list = []
    help_word = word
    help_count = 0
    developer_count = 0
    for x in word_list:
        if x == (' '):
            hang_list += ' '
        elif x == ('-'):
            hang_list += '-'
        else:
            hang_list += '_'
    print('Type "help" for help')
    print(" ".join(hang_list))
    while word_list != hang_list:
        count_list = 0
        if lives == 0:
            clear()
            print("\n".join(game_over))
            print("The solution was: " + word)
            choice = input("\nWould you like to play again? y/n?")
            if choice.lower() == ("y"):
                return game(data, lets_hang, hangman_pic, game_over, win, good_bye, cheater)
            else:
                print("\n".join(good_bye))
                if help_count > 0:
                    print("\n".join(cheater))
                break
        guess = input("Please choose a letter ")
        clear()
        if developer_count > 0:
            print(word)
        elif help_count > 0:
            print(help_word)
        elif guess == 'quit':
            print("\n".join(good_bye))
            break
        if guess == 'developer.mode':
            developer_count += 1
        elif guess == 'help':
            help_count += 1
        guess = guess.lower()
        guess_upper = guess.upper()
        if guess in word_list or guess_upper in word_list:
            if guess in hang_list or guess_upper in hang_list:
                print("You have tried--->" + guess_upper + "<---letter already! Please try again!")
            for x in word:
                if x.lower() == guess:
                    if count_list == 0:
                        if word_list[count_list] == guess_upper:
                            hang_list[count_list] = word_list[count_list]
                    elif hang_list[count_list - 1] == " " or hang_list[count_list - 1] == "-":
                        if word_list[count_list] == guess_upper or guess:
                            hang_list[count_list] = word_list[count_list]
                    else:
                        hang_list[count_list] = word_list[count_list]
                count_list += 1
        else:
            lives_left = checking_wrong_guess(guess, guess_upper, wrong_list, lives, word)
            lives = lives_left
        pic = hang_graphic(hangman_pic, lives)
        print("Wrong guess:", ", ".join(wrong_list))
        print("lives left: ", lives, "\n", " ".join(hang_list), "\n", "\n".join(pic))
    if word_list == hang_list:
        clear()
        if help_count > 0:
            print("\n".join(cheater))
        print('Congratulation!')
        print("\n".join(win))
        choice = input("Zsu&Bende/'s game!\nPlay again?\nPress: Y\nOr press any button to quit!")
        if choice.lower() == "y":
            return game(data, lets_hang, hangman_pic, game_over, win, good_bye, cheater)
        else:
            clear()
            print("\n".join(good_bye))
            if help_count > 0:
                print("\n".join(cheater))


if __name__ == '__main__':
    game(data, lets_hang, hangman_pic, game_over, win, good_bye, cheater)
