# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add/new, show/display, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        to_do = user_action[4:]

        # with context manager helps us to read the file the same as above, but better handled
        to_dos = functions.get_todos()

        to_dos.append(to_do + '\n')

        functions.write_todos(to_dos)

    elif user_action.startswith("show"):
        to_dos = functions.get_todos()

        # new_to_dos = []

        # for item in to_dos:
        # new_item = item.strip('\n')
        # new_to_dos.append(new_item)

        # new_to_dos = [item.strip('\n') for item in to_dos] #this is called list comprehension, which does a for
        # loop in a line

        for index, item in enumerate(to_dos):
            item = item.strip('\n')  # another way to remove the line break
            row = f"{index + 1}.- {item}"  # fstrings are for displaying strings as we want, with or without spaces between,it is important to use curly brackets
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            to_dos = functions.get_todos()
            new_item = input("Edit the current item: ")
            to_dos[number] = new_item + '\n'

            functions.write_todos(to_dos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            to_dos = functions.get_todos()

            index = number - 1
            to_do_to_remove = to_dos[index].strip('\n')
            to_dos.pop(index)  # pop removes an item from a list using index

            functions.write_todos(to_dos)

            message = f"To do item: {to_do_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is no such number in the to-do")

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye")
