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
# Exit the loop if the user doesn't want to add more lines