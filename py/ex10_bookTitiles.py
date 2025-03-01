# Book Titles
# You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
# The code is equal to the first letter of the book, followed by the number of characters in the title.
# For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

# You are provided a books.txt file, which includes the book titles, each one written on a separate line.
# Read the title one by one and output the code for each book on a separate line.

# For example, if the books.txt file contains:
# Some book
# Another book

# Your program should output:
# S9
# A12

# open the file for reading
file = open("/usercode/files/books.txt", "r")

# read and process each line in the file
for line in file:
    # remove leading and trailing whitespace
    title = line.strip()

    # calc and print the special code
    code = title[0] + str(len(title))
    print(code)

# close file
file.close()
