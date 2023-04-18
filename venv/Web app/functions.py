FILEPATH = "C:/pythonProject/webapp/venv/Web app/Todos.txt"


# create a custom function outside the loop to remove repetitive codes - use def for custom function. 2 break lines
# after
# custom function for opening/reading the filepath


def get_todos(filepath=FILEPATH):  # filepath is a parameter
    """" Read a text file and return the list of to-do items """  # Doc string
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# when writing you need to include the filepath and input that's local. todos in the loop is global.
# put non default parameters before default parameters
def write_todos(todos_Arg, filepath=FILEPATH):
    """ Writes the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_Arg)


# controls what is run directly by the module file. if you run this in the main file then prints will not show only when
# run the program in bonusf.py
if __name__ == "code with notes":
    print("hello")
    print(get_todos())
