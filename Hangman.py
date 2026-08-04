import random

words = ["python", "apple", "tomato", "parshant", "random"]
secret_word = random.choice(words)

wrong_guesses = 0
guessed_letters = []

print("\nGame Start")

while wrong_guesses < 6:
    
    display_word = ""

    for i in secret_word:
        if i in guessed_letters:
            display_word += i
        else:
            display_word += "_"

    print(display_word)

    if "_" not in display_word:
        print("You Win!")
        break

    guess = input("Enter the Letter: ")

    if guess in secret_word:
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("Correct Guess")
        else:
            print("You already guessed this letter.")
    else:
        wrong_guesses += 1
        print("Wrong Guess")
        print("Remaining Chances:", 6 - wrong_guesses)

if wrong_guesses == 6:
    print("Game Over!")
    print("The word was:", secret_word)