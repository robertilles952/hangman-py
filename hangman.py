import random

print("Welcome to Hangman!")

words = ["kecske", "alma", "laptop", "telefon", "automobil"]
word = random.choice(words)

print("The chosen word from " + str(words) + " is " + word)