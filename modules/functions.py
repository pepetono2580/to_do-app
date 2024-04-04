FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # default parameter as files/todos.txt because the path of the file will not change ever
    # this comment below is a docstring, helps with documentation
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        to_dos_local = file_local.readlines()
    return to_dos_local


def write_todos(to_dos_local, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(to_dos_local)


if __name__ == "__main__":
    # if it is anything outside this main, it will be executed anyway
    # this part will be executed if this script is executed
    print("Hello")
    print(get_todos())
