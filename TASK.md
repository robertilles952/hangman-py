# Hangman — Python practice task

## The goal

Build the classic word-guessing game **Hangman**, playable in the terminal.

The computer picks a secret word. The player guesses one letter at a time.
Correct letters are revealed in the word. Wrong guesses cost a life.
The player wins by revealing the whole word before running out of lives.

Example of a finished game:

```
Welcome to Hangman!

Word: _ _ _ _ _ _
Lives left: 6
Guess a letter: a

Good guess!
Word: _ a _ _ _ a
Lives left: 6
Guess a letter: z

Sorry, "z" is not in the word.
Word: _ a _ _ _ a
Lives left: 5
...

You won! The word was: banana
```

## What you will practise

- Variables and strings
- Lists
- `input()` and `print()`
- `if` / `elif` / `else`
- `while` and `for` loops
- Writing and calling functions
- Using a module from the standard library (`random`)

## Rules of the game

1. The secret word is picked at random from a list of words.
2. At the start, every letter is shown as `_`.
3. The player has **6 lives**.
4. Each turn the player types one letter.
5. If the letter is in the word, every place it appears is revealed.
6. If the letter is not in the word, the player loses one life.
7. Guessing the same letter twice does not cost a life. Tell the player they already tried it.
8. The game ends when:
   - every letter is revealed → the player **wins**, or
   - lives reach 0 → the player **loses**, and the secret word is shown.

---

## Build tasks

Work through these in order. Run your program after **every** step and check it does
what the step says before moving on. Save your code in a file called `hangman.py`
in this folder.

Run it with:

```
python3 hangman.py
```

### Step 1 — Say hello

Print a welcome message when the program starts.

✅ Done when: running the file prints `Welcome to Hangman!`.

### Step 2 — Pick a secret word

Make a list with at least 5 words. Use the `random` module to pick one of them.
For now, print the word so you can check it works (you will remove this later).

✅ Done when: running the file several times shows different words.

### Step 3 — Show the hidden word

Write a function that takes the secret word and the letters guessed so far,
and **returns** a string where unguessed letters are `_`.

For example, word `"banana"` with guessed letters `["a"]` should give `"_ a _ a _ a"`.

✅ Done when: calling your function with a few test words and letters gives the right result.

### Step 4 — Ask for one guess

Ask the player to type a letter with `input()`. Check whether it is in the word
and print a message saying yes or no.

✅ Done when: typing a letter from the word says "Good guess!", and any other letter says it is not in the word.

### Step 5 — Keep asking (the game loop)

Put the guessing inside a `while` loop so the player can keep guessing.
Keep a list of guessed letters, and show the hidden word after every guess.

✅ Done when: you can guess letter after letter and watch the word fill in.

### Step 6 — Lives

Start with 6 lives. Take one away for each wrong guess. Show the lives left each turn.

✅ Done when: wrong guesses lower the number, right guesses do not.

### Step 7 — Winning and losing

Stop the loop when the player wins or runs out of lives, and print the right message.
On a loss, show the secret word.

✅ Done when: you can both win and lose a game, and each ends with the correct message.

### Step 8 — Handle bad input

Make the game handle things the player might type by mistake:

- a letter they already guessed (no life lost, just a message)
- more than one character
- something that is not a letter, like `3` or `?`
- a capital letter (`A` should count the same as `a`)

✅ Done when: none of these crash the game or unfairly cost a life.

### Step 9 — Tidy up

- Remove the line that prints the secret word at the start.
- Split your code into small functions with clear names.
- Put the game itself in a function called `main()` and call it at the bottom of the file.

✅ Done when: the game plays from start to finish and your code is easy to read.

---

## Extra challenges (optional)

Pick any you like once the main game works:

- **Draw the hangman.** Show an ASCII drawing that grows with each wrong guess.
- **Play again.** After a game ends, ask "Play again? (y/n)".
- **Difficulty levels.** Easy = more lives, hard = fewer lives or longer words.
- **Word file.** Load the word list from a `words.txt` file instead of writing it in the code.
- **Show wrong guesses.** Print the letters the player has tried that were not in the word.
- **Guess the whole word.** Let the player type the full word as a guess.

## Tips

- Python reads the file top to bottom — define a function before you call it.
- `input()` always gives back text. `.lower()` turns text into lowercase.
- `letter in word` gives `True` or `False` — very handy here.
- `.isalpha()` tells you if a string is only letters.
- If something breaks, read the **last line** of the error in the terminal first.
  It usually says what went wrong, and the lines above it say where.
