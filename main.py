from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos, 1):
            item = item.strip('\n')
            print(f"{index}.- {item}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()

            number = user_action[5:]
            number = int(number) - 1
            new_todo = input(f"Enter text to edit --> {todos[number]}: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("Wrong task number: out of range")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            number = user_action[9:]
            number = int(number) - 1
            removed = todos.pop(number).strip("\n")
            print(f"The '{removed}' task was completed and deleted from the list")

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("Wrong task number: out of range")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")

print("Bye!")
