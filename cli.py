# from functions import get_todos, write_todos
import functions
import time


prompt = "Type add, show, edit, complete, or exit: "
now = time.strftime('%b-%d-%y %H:%M:%S')
print(now)


# while loop runs until user exits
while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    # match case to take user input and enact certain actions
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # this allows the user to do an inline for loop to strip items from list and save in new variable
        # new_todos = [item.strip('\n') for item in todos]

        # for loop to strip break line from each string in list
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}- {item}"
            print(row)

    # This allows the user to edit any item on list must put "edit param(int)"
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Please enter number of item on list")
            continue

    elif user_action.startswith('complete'):
        try:
            todo_complete = int(user_action[9:])

            todos = functions.get_todos()

            todo_to_remove = todos[todo_complete - 1].strip('\n')
            todos.pop(todo_complete - 1)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from list."
            print(message)
        except IndexError:
            print("Item number does not exist")
            continue
    elif user_action.startswith('exit'):
        break

    else:
        print("Command Invalid")

print("Bye!")
