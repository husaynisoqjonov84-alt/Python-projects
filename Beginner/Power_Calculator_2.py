while True:
    
    number = input("Give me any random number>>>>")
    degree = input ("Give me any degree that you want to see of your number>>>")
    result = int(number) ** int(degree)
    
    print ("The result is >>>", result)
    
    Question = input("Do you want to perform another calculation? yes/no>>>")
    
    if Question.lower() == "yes":
        continue 
    else:
        print ("The calculation is over, thank you")
        break


