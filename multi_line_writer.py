# Write a method in python to write multiple line of text contents into a text file mylife.txt.

# Open the file in write mode
with open("mylife.txt", "w") as my_file:
# Create a while loop with a True condition
    while True:
        # Ask the input line from the user
        user_input = input("Enter Line: ")
        # Write the line to the file
        my_file.write(user_input + "\n")
        # Check if the user wants to input more lines
        more_lines = input("Are there more lines y/n? ")
        # Check if the user input 'y'
        if more_lines == "y":
            continue
        elif more_lines == "n":
            break
        # Check if it is an invalid input
        else:
            print("INVALID INPUT. Please input only 'y' or 'n'.")
        # Exit the loop if the user doesn't want to add more lines