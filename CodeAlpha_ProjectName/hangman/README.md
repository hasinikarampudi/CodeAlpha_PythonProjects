# Hangman Game

A simple command-line Hangman game built in Python.

## Description

- The program randomly selects one word from 5 predefined computer science-related words.
- The user guesses one letter at a time.
- Correct guesses reveal the letter in the word.
- Wrong guesses reduce the number of lives.
- The game ends when:
  - The user guesses the entire word (win), or
  - Lives become 0 (lose).

This project uses only basic Python features and no external files or APIs.

## Features

- 5 predefined words: PYTHON, JAVA, NETWORK, DATABASE, ALGORITHM  
- 6 lives
- Input validation:
  - Only single letters (A–Z) allowed
  - Prevents repeated guesses
- Clear display of:
  - Current word status (e.g., `_ A _ _ _`)
  - Lives left
  - Previously guessed letters

## How to Run

1. Make sure you have Python installed (Python 3.x recommended).
2. Open the `hangman` folder.
3. Run the game:
   ```bash
   python main.py