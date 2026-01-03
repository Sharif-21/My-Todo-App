import time


def read():
    filepath = "todos.txt"
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write(todos_local):
    filepath = "todos.txt"
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


print(f"Hey! today is {time.strftime("%b-%d-%y  %H:%M:%S")}")
