import random

words = ["python", "computer", "college", "coding", "program"]

word = random.choice(words)
guessed = []
chances = 6

print("Welcome to Hangman Game!")

while chances > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)
    print("Chances left:", chances)

    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet!")
        continue

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        chances -= 1
        print("Wrong guess!")

if chances == 0:
    print("Game Over!")
    print("The word was:", word)