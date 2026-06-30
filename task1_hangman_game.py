# ============================================
#                TASK 1
#             Hangman Game
# ============================================

import random

# Predefined list of 5 words
WORDS = ["python", "hangman", "coding", "laptop", "keyboard"]

# Hangman ASCII art stages
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("\n" + "=" * 40)
    print("      Welcome to HANGMAN GAME!")
    print("=" * 40)

    while wrong_guesses < max_wrong:
        print(HANGMAN_STAGES[wrong_guesses])

        # Show word progress
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print(f"  Word:               {display}")
        print(f"  Wrong guesses left: {max_wrong - wrong_guesses}")
        print(f"  Letters guessed:    {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n  Congratulations! You guessed the word:", word.upper())
            break

        guess = input("\n  Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("  Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"  You already guessed '{guess}'. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"  '{guess}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"  '{guess}' is NOT in the word!")

    else:
        print(HANGMAN_STAGES[max_wrong])
        print(f"\n  Game Over! The word was: {word.upper()}")

    again = input("\n  Play again? (yes/no): ").lower()
    if again == "yes":
        play_hangman()
    else:
        print("\n  Thanks for playing! Goodbye!\n")


if __name__ == "__main__":
    play_hangman()