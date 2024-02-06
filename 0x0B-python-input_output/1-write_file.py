#!/usr/bin/python3
def write_file(filename="", text=""):
    # Use the with statement to open the file in write mode
    with open(filename, "w", encoding="utf-8") as f:
        # Write the text to the file and return the number of characters written
        return f.write(text)

