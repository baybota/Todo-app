FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items"""
    # All with functions open files for either r (Reading) or w (Writing)
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Gets text file and writes new argument to list"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)