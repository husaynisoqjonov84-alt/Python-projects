

tasks = []

while True:

    print("\n===== TASK MANAGER =====")
    print("1. Add new task")
    print("2. See tasks list")
    print("3. Edit task")
    print("4. Finish the process")

    quest1 = int(input("\nChoose >>> "))

    if quest1 == 1:

        task1 = input("\nEnter the task >>> ")

        process = input(
            "Finished = a / Not finished = b >>> "
        ).lower()

        if process == "a":
            process = "Finished"

        elif process == "b":
            process = "Not finished"

        else:
            print("Invalid status!")
            continue

        tasks.append([task1, process])

        print("Task successfully added!")

    elif quest1 == 2:

        print("\n===== YOUR TASKS =====")

        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task[0]} - {task[1]}")

    elif quest1 == 3:

        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task[0]} - {task[1]}")

        n = int(input("\nEnter task number >>> ")) - 1

        n2 = input("Enter new task name >>> ")

        tasks[n][0] = n2

        print("Congratulations, task successfully edited!")

    elif quest1 == 4:

        print("Tasks are saved. Thank you!")
        break

    else:
        print("Invalid choice!")
