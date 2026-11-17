#while True:
    start_number = int(input("Enter a number for multiplication table >>> "))
    
    start = int(input("Enter the starting number >>> "))
    
    end = int(input("Enter the ending number >>> "))

    for y in range(start, end + 1):
        result = start_number * y
        print(f"{start_number} x {y} = {result}")

    quest = input("Do you want to continue? (yes/no) >>> ")

    if quest.lower() == "yes":
        continue
    else:
        print("Thank you! Program is over.")
        break