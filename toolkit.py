# Personal Mini-Toolkit

print("Welcome to My Personal Mini-Toolkit!")

tasks = []

while True:
    print("\n--- MAIN MENU ---")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Simple Calculator
        print("\n--- SIMPLE CALCULATOR ---")

        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            print(f"Result: {num1 + num2}")

        elif operator == "-":
            print(f"Result: {num1 - num2}")

        elif operator == "*":
            print(f"Result: {num1 * num2}")

        elif operator == "/":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Cannot divide by zero.")

        else:
            print("Invalid operation.")

    elif choice == "2":
        # To-Do List
        while True:
            print("\n--- TO-DO LIST ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Back to main menu")

            task_choice = input("Enter your choice: ")

            if task_choice == "1":
                task = input("Enter your task: ")
                tasks.append(task)
                print(f"Task '{task}' added successfully!")

            elif task_choice == "2":
                if tasks:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")
                else:
                    print("Your task list is empty.")

            elif task_choice == "3":
                if tasks:
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

                    task_number = int(
                        input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("Invalid task number.")
                else:
                    print("Your task list is empty.")

            elif task_choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":
        # Number Checker
        print("\n--- NUMBER CHECKER ---")

        number = float(input("Enter a number: "))

        if number > 0:
            print(f"{number} is a positive number.")

        elif number < 0:
            print(f"{number} is a negative number.")

        else:
            print("The number is zero.")

    elif choice == "4":
        print("Thank you for using my toolkit. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 4.")
