"""File I/O Assignment
This assignment focuses on reading from and writing to text files in Python."""

# ## Exercises

# 1. Write a function in python to read the content
# from a given text file line by line and display
# the contents of the file on the screen.


def read_and_print(filename):
    """Read and print the content of a file line by line."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")


# 2. Write a function in python to count the number of
# lines from a given text file which is not starting
# with an alphabet "T" and print the result.


def read_and_count(filename):
    """Count lines not starting with 'T' in a file."""
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if not line.lstrip().startswith("T"):
                count += 1
    print("Lines not starting with 'T':", count)


# 3. Write a function in Python to count and
# display the total number of words in a text file.


def count_words(filename):
    """Count and display the total number of words in a file."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        words = content.split()
        print("Total words:", len(words))


# 4. Write a function in Python to read lines
# from a text file. The function should find
# and print the occurrence of the word "the".


def count_the(filename):
    """Count occurrences of the word 'the' in a file."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().lower()
        words = content.split()
        count = sum(1 for word in words if "the" in word)
        print("Occurrences of 'the':", count)


# 5. Write a function in python to read lines
# from a text file and display those words,
# which are less than 4 characters.


def display_words(filename):
    """Display words less than 4 characters from a file."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) < 4:
                    print(word)


# 6. Write a function in Python to count the words "this" and "these"
# in a text file. [Note that the words "this" and "these" are
# complete words]


def count_this_these(filename):
    """Count occurrences of the words 'this' and 'these' in a file."""
    this_count = 0
    these_count = 0
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            if word == "this":
                this_count += 1
            elif word == "these":
                these_count += 1
    print("Count of 'this':", this_count)
    print("Count of 'these':", these_count)


# 7. Write a function in Python to count
# words in a text file those are ending with alphabet "e".


def count_ewords(filename):
    """Count words ending with 'e' in a file."""
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().split()
        for word in words:
            if word.endswith("e"):
                count += 1
    print("Words ending with 'e':", count)


# 8. Write a function in Python to count
# uppercase character in a text file.
#     > def count_upper(filename):


def count_upper_isupper(filename):
    """Count uppercase characters using str.isupper() method."""
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        for char in text:
            if char.isupper():
                count += 1
    print("Uppercase characters (isupper):", count)


def count_upper_ascii(filename):
    """Count uppercase characters using ASCII value check"""
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        for char in text:
            if "A" <= char <= "Z":
                count += 1
    print("Uppercase characters (ASCII):", count)


# 9. A text file contains some text, which needs to be displayed
# such that every next character is separated by a symbol "#".
# Write a function definition for hash_display() in Python
# that would display the entire content of the file in the desired format.

#     > def hash_display():

#     Example :
#     If the file has the following content stored in it :
#     THE WORLD IS ROUND

#     The function hash_display() should display the following content :
#     T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#


def hash_display(filename):
    """Display file content with characters separated by '#'."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        char_list = list(content)
        result = "#".join(char_list)
        print(result)
