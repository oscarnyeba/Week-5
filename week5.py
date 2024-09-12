# file_handling_assignment.py

# Task 1: File Creation
def create_file():
    try:
        # Open file in write mode and create it if it doesn't exist
        with open("my_file.txt", 'w') as file:
            # Write three lines of text to the file
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: Python File Handling 101\n")
            file.write("Line 3: Number 42\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating or writing to the file: {e}")

# Task 2: File Reading and Display
def read_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", 'r') as file:
            # Read the contents of the file
            content = file.read()
            # Display the contents of the file
            print("File Contents:")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

# Task 3: File Appending
def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", 'a') as file:
            # Append three additional lines of text
            file.write("Line 4: Appending text is easy!\n")
            file.write("Line 5: Learning is fun.\n")
            file.write("Line 6: The number 99\n")
        print("Text appended successfully.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File handling operations completed.")

# Running the functions to complete the tasks
create_file()
read_file()
append_to_file()
read_file()  # Read again to verify appending
