
import random

while True:
    number = random.randint(1, 100)

    counter = 1
    limit = 5

    while counter <= limit:
        savol = int(input("Guess a number between 1 and 100: "))

        if savol == number:
            print("Congratulations! You guessed the number!")
            break

        elif savol > number:
            print("Too high!")

        else:
            print("Too low!")

        counter += 1

    question = input("Do you want to play again? (yes/no): ")

    if question.lower() == "yes":
        continue
    else:
        print("Game is over. Thank you!")
        break
