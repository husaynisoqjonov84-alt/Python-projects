
contacts = {}

def save_contact():
    name = input("Enter the contact name >>> ")
    number = int(input("Enter the contact number >>> "))

    contacts[name] = number


while True:
    save_contact()

    quest = input("Do you want some more contacts? yes/no >>> ")

    if quest == "yes":
        continue

    else:
        quest2 = input("The contacts are saved, do you want to see the list? Yes/No >>> ")

        if quest2 == "Yes":
            print(contacts)
        else:
            print("The contacts saved, thank you!")

        break

        
