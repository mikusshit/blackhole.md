import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

def get_file():
    target_file = input("Enter file name: (Include the file extension, and make sure the file is placed in the same directory as the program): ")
    if target_file == "":
        print("Please enter a file name")
        return get_file()  # Return result
    return target_file

def file_read(target_file):
    if os.path.isfile(target_file):
        with open(target_file, "r") as file:  
            data = file.read()
        return data
    else:
        print("File doesn't exist")
        return None

def print_highlighted_code(code):
    if code:
        # Highlighting the code using Pygments
        formatter = TerminalFormatter()
        highlighted_code = highlight(code, PythonLexer(), formatter)
        print(highlighted_code)
    else:
        print("No code to highlight.")

filetoopen = get_file()
data = file_read(filetoopen)
print_highlighted_code(data)
