# Testing Hangman

This guide covers the automated logic tests and a quick manual check of the game in [bende/solution/hangman.py](bende/solution/hangman.py).

## What is a virtual environment?

A virtual environment (venv) is a separate Python workspace for one project. It keeps project tools, such as pytest, separate from Python packages used by other projects or installed for the whole computer. The `.venv` folder is generated on your computer and should not be committed to Git; this repository already ignores it.

## Set up and use the venv

Open a terminal at the repository root. The repository may already have a `.venv` folder; create it only if it is missing.

### Linux or macOS

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

When the venv is active, the terminal prompt usually shows `(.venv)`. Use `python` and `python -m pip` in that terminal so commands use the venv. To leave it, run `deactivate`.

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

In Command Prompt, activate with `.venv\Scripts\activate.bat` instead. Leave the venv with `deactivate`.

If VS Code uses a different Python interpreter, choose the interpreter inside this repository's `.venv` (Linux/macOS: `.venv/bin/python`; Windows: `.venv\Scripts\python.exe`).

## Run the automated tests

Open a terminal in the repository root (the folder containing `.venv`). On Linux or macOS, you can run the tests with the venv's Python directly, even if the venv is not active:

```sh
./.venv/bin/python -m pytest bende/solution
```

If you activated the venv first, this equivalent command works:

```sh
python -m pytest bende/solution
```

The current suite has 18 tests. A successful run ends with `18 passed`. The tests check difficulty filtering, guessed-letter tracking, correct and incorrect guesses, showing hidden letters, lives, win/loss conditions, and loading the word list. They call the game functions directly; they do not play through the interactive game.

Use `python -m pytest` to run pytest as a Python module. Do not use `pytest -m hangman.py` to name the test file: pytest's `-m` option selects tests by marker, not by file path.

You can also run the game manually from the repository root:

```sh
./.venv/bin/python bende/solution/hangman.py
```

If the venv is active, use `python bende/solution/hangman.py` instead. Choose a difficulty, then check correct and incorrect guesses, invalid input, repeated guesses, and the play-again prompt. The game currently prints the secret word at the start of a round, so it is visible during this manual check.