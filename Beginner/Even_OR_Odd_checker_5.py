
while True:
    son = int(input("Enter the number >>> "))

    if son % 2 != 0:
        print("Odd number")
    else:
        print("Even number")

    question = input("Do you want to continue? yes/no >>> ")

    if question.lower() == "yes":
        continue
    else:
        print("Thank you, the program is over.")
        break
