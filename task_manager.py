import time

user_file = open("user.txt", "r", encoding="utf-8")

# Importing usernames and passwords from user.txt and saving them in two separate lists
username_list = []
password_list = []
for line in user_file:
    user, psw = line.strip("\n").split(", ")
    username_list.append(user)
    password_list.append(psw)
user_file.close()

username = input("Please enter your username: ")
# Using a while loop to validate their username
while not username in username_list:
    print("Invalid username")
    username = input("Please enter your username: ")

position = username_list.index(username)  # Finding index position of username

password = input("Please enter your password: ")
# Using a while loop to validate their password against username index position
while password != password_list[position]:
    print("Incorrect password")
    password = input("Please enter your password: ")

# Using a while loop asking user to select from menu. User 'admin' to have additional option 's' to menu
# Using if/elif/else statements for the option selected below
# If 'r' add new user to user.txt
# if 'a' add new task to tasks.txt
# if 'va' display all tasks
# if 'vm' display user own tasks
# if 's' and user 'admin' display number of tasks and users
# if 'e' exit
while True:
    if username == "admin":
        menu = input(
            """Please select one of the following options:
                    r - register user
                    a - add task
                    va - view all tasks 
                    vm - view my tasks
                    s - statistics
                    e - exit 
                """
        ).lower()
    elif username != "admin":
        menu = input(
            """Please select one of the following options:
                    r - register user
                    a - add task
                    va - view all tasks 
                    vm - view my tasks
                    e - exit 
                """
        ).lower()

    if menu == "r" and username == "admin":
        new_user = input("Please enter a new username: ")
        new_pass = input("Please enter a new password: ")
        confirm_pass = input("Please re-enter password: ")
        if new_pass == confirm_pass:
            user_file = open("user.txt", "a", encoding="utf-8")
            user_file.write(f"\n{new_user}, {new_pass}")
            user_file.close()
            print("New user registered successfully!")
        else:
            print("Password does not match, try again")

    elif menu == "r" and username != "admin":
        print("User not authorised to register other users!")

    elif menu == "a":
        user_task = input(
            "Please enter the username of the person whom the task is assigned to: "
        )
        task_tile = input("Please enter the task title: ")
        task_description = input("Please describe the task: ")
        task_due_date = input("Please enter the task due date: ")
        todays_date = time.strftime("%d %b %Y")
        task_file = open("tasks.txt", "a", encoding="utf-8")
        task_file.write(
            f"\n{user_task}, {task_tile}, {task_description}, {todays_date}, {task_due_date}, No"
        )
        task_file.close()
        print("Task added successfully!")

    elif menu == "va":
        task_file = open("tasks.txt", "r", encoding="utf-8")
        read_task_file = task_file.readlines()
        for pos, line in enumerate(
            read_task_file, 1
        ):  # Using enumerate to number the lines/tasks in tasks.txt
            split_task = line.split(", ")
            output = f"____________[{pos}]____________\n"
            output += "\n"
            output += f"Task: \t\t{split_task[1]}\n"
            output += f"Assigned to: \t{split_task[0]}\n"
            output += f"Date assigned: \t{split_task[3]}\n"
            output += f"Due date: \t{split_task[4]}\n"
            output += "Task complete: \tNo\n"
            output += f"Task description: {split_task[2]}\n"
            output += "___________________________\n"
            print(output)
        task_file.close()

    elif menu == "vm":
        task_file = open("tasks.txt", "r", encoding="utf-8")
        read_task_file = task_file.readlines()
        for line in read_task_file:
            split_task = line.split(", ")
            if username == split_task[0]:
                output = "___________________\n"
                output += "\n"
                output += f"Task: \t\t{split_task[1]}\n"
                output += f"Assigned to: \t{split_task[0]}\n"
                output += f"Date assigned: \t{split_task[3]}\n"
                output += f"Due date: \t{split_task[4]}\n"
                output += "Task complete: \tNo\n"
                output += f"Task description: {split_task[2]}\n"
                output += "___________________\n"
                print(output)
        task_file.close()

    elif menu == "s" and username == "admin":
        task_file = open("tasks.txt", "r", encoding="utf-8")
        user_file = open("user.txt", "r", encoding="utf-8")
        read_task_file = task_file.readlines()
        read_user_file = user_file.readlines()
        for task in range(len(read_task_file)):
            task += 1
        for user in range(len(read_user_file)):
            user += 1
            output = "_______________________\n"
            output += f"Number of tasks: {task})\n"
            output += f"Number of users: {user})\n"
            output += "_______________________\n"
            print(output)
        task_file.close()
        user_file.close()

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("Incorrect selection, please try again!")
