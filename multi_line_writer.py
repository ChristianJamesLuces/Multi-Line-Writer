# Write a method in python to write multiple line of text contents into a text file mylife.txt.
import pyfiglet
import time

# Define the variable
intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font = "digital")
# Welcome message and its function
print(intro)
print("\033[44;1m" + "This program will write multiple line of text contents into a text file mylife.txt.\n" + "\033[0m")
input("Press the ENTER key to run the program....\n")
time.sleep(5)
# Open the file in write mode
with open("mylife.txt", "w") as my_file:
# Create a while loop with a True condition
    while True:
        # Ask the input line from the user
        user_input = input("\033[93;1m" + "Enter Line: " + "\033[0m")
        # Write the line to the file
        my_file.write(user_input + "\n")
        # Check if the user wants to input more lines
        more_lines = input("\033[95;1m" + "Are there more lines y/n? " + "\033[0m")
        # Check if the user input 'y'
        if more_lines == "y":
            continue
        # Exit the loop if the user doesn't want to add more lines
        elif more_lines == "n":
            print("\n" + ":" * 50)
            print("\033[102;1m" + "(: Thank you for using the program! :)".center(50) + "\033[0m")
            print(":" * 50)
            break
        # Check if it is an invalid input
        while more_lines != "y" and "n":
            print("INVALID INPUT. Please input only 'y' or 'n'.")
            more_lines = input("\033[95;1m" + "Are there more lines y/n? " + "\033[0m")
            # Check if the user input 'y'
            if more_lines == "y":
                continue
            # Exit the loop if the user doesn't want to add more lines
            elif more_lines == "n":
                print("\n" + ":" * 50)
                print("\033[102;1m" + "(: Thank you for using the program! :)".center(50) + "\033[0m")
                print(":" * 50)
                break