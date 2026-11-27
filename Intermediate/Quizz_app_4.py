scores = 0
limit = 3

counter = 0

while counter < limit:
    quest1 = input("1. What is the capital of France? >>> ")
    counter += 1

    if quest1.title() == "Paris":
        print("Congratulations! You got 20 points")
        scores += 20
        break
    else:
        print("Incorrect answer, try again")

counter = 0

while counter < limit:
    quest2 = input("2. How many days are there in a week? >>> ")
    counter += 1

    if quest2 == "7":
        print("Congratulations! You got 20 points")
        scores += 20
        break
    else:
        print("Incorrect answer, try again")

counter = 0

while counter < limit:
    quest3 = input("3. What is 5 + 5? >>> ")
    counter += 1

    if quest3 == "10":
        print("Congratulations! You got 20 points")
        scores += 20
        break
    else:
        print("Incorrect answer, try again")

counter = 0

while counter < limit:
    quest4 = input("4. What is the opposite of hot? >>> ")
    counter += 1

    if quest4.title() == "Cold":
        print("Congratulations! You got 20 points")
        scores += 20
        break
    else:
        print("Incorrect answer, try again")

counter = 0

while counter < limit:
    quest5 = input("5. Which fruit is yellow? >>> ")
    counter += 1

    if quest5.title() == "Banana":
        print("Congratulations! You got 20 points")
        scores += 20
        break
    else:
        print("Incorrect answer, try again")

print("Your total score is:", scores)
