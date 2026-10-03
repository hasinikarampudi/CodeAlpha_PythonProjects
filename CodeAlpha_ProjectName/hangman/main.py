
import random
WORDS =["HINANNA","VISWANATHANDSONS","KALKI","RADHEYSHYAM","HIT"]
def choose_word():
    return random.choice(WORDS)
def display_word(word,guessed_letters):
    display =""
    for ch in word:
        if ch.isalpha() and ch not in guessed_letters:
            display+="- "
        else:
            display += ch+" "
    return display.strip()
def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter:").strip().upper()
        if len(guess) != 1 or not guess.isalpha() :
              print("Please enter a single letter (A-Z).")
              continue
        if guess in guessed_letters:
              print("You already guessed this letter.")
              continue
        return guess
if __name__ == "__main__":
    word = choose_word()
    guessed_letters = set()
    lives = 6
    print("Let's play hangman")
    print("Hint: The word is a TFI movie")
    while True:
        print(display_word(word,guessed_letters))
        print(f"Lives left: {lives}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        if guess not in word:
            lives -= 1
            print("Wrong guess")
        else:
            print("Good guess")
        if all((ch.isalpha() and ch in guessed_letters) or not ch.isalpha() for ch in word):
                print(display_word(word,guessed_letters))
                print("congrats muggle you guessed the word!")
                break
        if lives <= 0:
                print(f"'Game over! The word was: {word}")
                break

