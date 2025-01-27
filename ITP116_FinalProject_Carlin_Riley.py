# Riley Carlin, rcarlin@usc.edu
# ITP 116, 10:00-10:50 a.m.
# Final Project
# Description:
# This program creates a dictionary of snake objects using data from a provided file. The user can then search snakes
# by name, filter through the snakes, and view various charts depicting snake statistics.
# Snake data comes from  "A Guide to Snakes of Southeast Texas" from inaturalist.org
# Code from the google search portion of sSearch() is derived from code from a geeksforgeeks guide
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/

import matplotlib.pyplot as plt
import numpy as np
from colour import Color
import webbrowser


# Snake object represents a snake
class Snake:
    # expects a string for the snake's name, a float for the snake's length, a 0 or 1 for the venomousness state, and
    # a list of colors the snake can be
    def __init__(self, _name, _len, _isVen, _colors):
        self.name = _name
        self.length = _len
        self.isVen = _isVen
        self.colors = _colors

    # Overwrites the toString method, formats the snake's information in a way that is easy to read
    def __str__(self):
        temp = "The " + self.name + " is a "

        # Adding venomousness to string
        if self.isVen:
            temp += "venomous snake."
        else:
            temp += "non-venomous snake."

        # Adding length to string
        temp += " It averages " + str(self.length) + " meters in length and is "

        # Adding the colors to the string, with correct commas and "and"
        if len(self.colors) == 1:
            temp += self.colors[0] + "."
        elif len(self.colors) == 2:
            temp += self.colors[0] + " and " + self.colors[1] + "."
        else:
            i = 0
            while i < len(self.colors) - 1:
                temp += self.colors[i] + ", "
                i += 1
            temp += "and " + self.colors[i] + "."

        return temp


# Prompts user for name of a file and will continue to prompt user until an open-able file is entered
# Returns the name of the file
def getFile():
    # Runs until a valid filename is entered
    while True:
        try:
            fileName = input("Please input a snake file: ")
            test = open(fileName, "r")
            test.close()
            break  # If the file can be opened
        except OSError:
            print("Could not open file.")

    return fileName


# Makes a dictionary of snake objects that represent the snakes in fileName.txt
def makeSnakeDict(fileName):
    snakeDict = {}

    reading = open(fileName, "r")
    # Adding each snake, one per line
    # The try/ except is to catch any lines that aren't in the correct format for the snake object
    for line in reading:
        try:
            temp = line.split("|")
            colors = temp[3].split(",")
            colors[len(colors) - 1] = colors[len(colors) - 1].strip("\n")

            snakeDict[temp[0]] = Snake(temp[0], float(temp[1]), int(temp[2]), colors)
        except:  # Catches any error (I'd expect out of bounds from colors or invalid type from the float cast
            continue  # Skips the invalid line

    reading.close()
    return snakeDict


# Prints main menu options
def printMainMenu():
    print("Menu:")
    print("\t1. Search")
    print("\t2. Filter")
    print("\t3. Stats")
    print("\t4. Exit")


# Prints filter menu options
def printFilterMenu():
    print("Filter:")
    print("\t1. Name")
    print("\t2. Length")
    print("\t3. Venomousness")
    print("\t4. Color")
    print("\t5. Print Results")
    print("\t6. Stats")
    print("\t7. Filter Progress")
    print("\t8. Back")


# Prints statistics menu options
def printStatsMenu():
    print("Stats:")
    print("\t1. Length")
    print("\t2. Venomousness")
    print("\t3. Color")
    print("\t4. Back")


# Prompts user for a command for the main menu, continues to prompt user until they choose to exit
# Takes in a dictionary of Snakes to pass to other functions
def getMainCommand(snakeDict):
    choice = ""
    while choice != "4":
        print("------")
        printMainMenu()
        choice = input("What would you like to do? ")
        if choice == "1":  # Search
            sSearch(snakeDict)
        elif choice == "2":  # Filter
            getFilterCommand(snakeDict)
        elif choice == "3":  # Statistics
            getStatsCommand(snakeDict)
        elif choice == "4":  # Exit
            print("Goodbye!")
        else:  # Invalid
            print("Sorry, " + choice + " is not an option.")


# Prompts user for a command for the filter menu, continues to prompt user until they choose to return to main menu
# Takes in a dictionary of Snakes to pass to other functions
def getFilterCommand(snakeDict):
    choice = ""
    working = snakeDict.copy()  # Don't want to be editing the original dictionary
    amountLeft = [len(snakeDict)]

    # Runs until the user selects to quit
    while choice != "8":
        printFilterMenu()

        choice = input("What would you like to do? ")
        if choice == "1":  # Name
            working = filterName(working)
            amountLeft.append(len(working))
            print("Filtered!")
        elif choice == "2":  # Length
            working = filterLen(working)
            amountLeft.append(len(working))
            print("Filtered!")
        elif choice == "3":  # Venomousness
            working = filterVen(working)
            amountLeft.append(len(working))
            print("Filtered!")
        elif choice == "4":  # Color
            working = filterColor(working)
            amountLeft.append(len(working))
            print("Filtered!")
        elif choice == "5":  # Print Results
            printAll(working)
        elif choice == "6":  # Go to stats menu
            getStatsCommand(working)
        elif choice == "7":  # Filter progress
            filterProg(amountLeft)
        elif choice == "8":  # Return to main menu
            return
        else:  # Invalid choice
            print("Sorry, " + choice + " is not an option.")


# Prompts user for a command for the stats menu, continues to prompt user until they choose to return to the
# previous menu
# Takes in a dictionary of Snakes to pass to other functions
def getStatsCommand(snakeDict):
    choice = ""
    # Runs until user chooses to return
    while choice != "4":
        printStatsMenu()

        choice = input("Which graph would you like? ")
        if choice == "1":  # Length
            lenHist(snakeDict)
        elif choice == "2":  # Venomousness
            venPie(snakeDict)
        elif choice == "3":  # Color
            colorBar(snakeDict)
        elif choice == "4":  # Return to previous menu
            return
        else:  # Invalid choice
            print("Sorry, " + choice + " is not an option.")


# Searches through the snakes in snakeDict for a snake with a given name
# If found, will provide information on the snake and offer pictures/ further reading on the snake
# Takes in a dictionary of Snake objects
def sSearch(snakeDict):
    looking = input("Please enter the name of a snake: ").title()

    # If the user-specified snake is in the file
    if looking in snakeDict:
        print(snakeDict[looking])

        # Pictures
        ans = input("Would you like to see some pictures of this snake? (y/n) ").lower()

        # Continues to prompt user until valid input is received
        while ans != "y" and ans != "n":
            print("Please respond “y” for yes or “n” for no.")
            ans = input("Would you like to see some pictures of this snake? (y/n) ").lower()

        # Opens a window of the Google images results of the snake
        if ans == "y":
            query = looking.replace(" ", "+")
            webbrowser.open_new("google.com/search?tbm=isch&q=" + query)

        # More info
        ans = input("Would you like more information on this snake? (y/n) ").lower()

        # Continues to prompt user until valid input is received
        while ans != "y" and ans != "n":
            print("Please respond “y” for yes or “n” for no.")
            ans = input("Would you like more information on this snake? (y/n) ").lower()

        # Prints out top 3 links a Google search finds on the snake
        if ans == "y":
            try:
                from googlesearch import search
                for link in search(looking, tld="co.in", stop=5):
                    print(link)

            except ImportError:
                print("Oops! Something went wrong :(")

    else:
        print("Sorry, I don't have information on that snake.")


# Returns a snake dictionary that only has snakes with user input in their name
# Takes in a dictionary of Snake objects
def filterName(snakeDict):
    tempDict = snakeDict.copy()
    unsplit = input("What word(s) are in the name of your snake? ").title()
    splitted = unsplit.split()

    # Removes snake if none of the words in splitted are in its name
    for key in snakeDict:
        none = True
        for s in splitted:
            if s in snakeDict[key].name:
                none = False

        if none:
            tempDict.pop(key)

    return tempDict


# Returns a snake dictionary that only has snakes whose length satisfies user-inputted inequality
# Takes in a dictionary of Snake objects
def filterLen(snakeDict):
    tempDict = snakeDict.copy()

    # Getting the inequality sign
    sign = input("Enter an equality or inequality sign (=, !=, >, >=, <, <=): ")
    while sign != "=" and sign != ">" and sign != ">=" and sign != "<" and sign != "<=" and sign != "!=":
        print("Sorry, " + sign + " is not an option.")
        sign = input("Enter an equality or inequality sign (=, !=, >, >=, <, <=): ")

    # Continues to prompt the user until they enter a float
    while True:
        try:
            length = float(input("Enter a length in meters: "))
            break  # If everything inputted was valid
        except ValueError:  # User inputted a non float value
            print("Please enter an int or a float. ")

    # Takes out every Snake whose length do not satisfy the inequality
    for key in snakeDict:
        if sign == "=":
            if snakeDict[key].length != length:
                tempDict.pop(key)
        elif sign == "!=":
            if not snakeDict[key].length != length:
                tempDict.pop(key)
        elif sign == ">":
            if not snakeDict[key].length > length:
                tempDict.pop(key)
        elif sign == ">=":
            if not snakeDict[key].length >= length:
                tempDict.pop(key)
        elif sign == "<":
            if not snakeDict[key].length < length:
                tempDict.pop(key)
        elif sign == "<=":
            if not snakeDict[key].length <= length:
                tempDict.pop(key)
    return tempDict


# Returns a snake dictionary that only has snakes who are/ are not venomous, according to the user
# Takes in a dictionary of Snake objects
def filterVen(snakeDict):
    tempDict = snakeDict.copy()
    ans = input("Is your snake venomous? (y/n) ").lower()

    # Continues to prompt user until given a valid answer
    while ans != "y" and ans != "n":
        print("Please respond “y” for yes or “n” for no.")
        ans = input("Is your snake venomous? (y/n) ").lower()

    if ans == "y":
        temp = 1
    else:
        temp = 0

    # Takes out snakes that do not match user criteria
    for key in snakeDict:
        if snakeDict[key].isVen != temp:
            tempDict.pop(key)

    return tempDict


# Returns a snake dictionary that only has snakes who appears in user-specified color
# Takes in a dictionary of Snake objects
def filterColor(snakeDict):
    color = input("What color is your snake (use “-” instead of spaces for multi-word colors)? ")
    tempDict = snakeDict.copy()

    # Continues prompting user until given exactly one word
    while " " in color:
        print("Please enter only one color.")
        color = input("What color is your snake (use “-” instead of spaces for multi-word colors)? ")

    color = color.lower()

    # Takes out snake that does not appear in color
    for key in snakeDict:
        if color not in snakeDict[key].colors:
            tempDict.pop(key)

    return tempDict


# Displays a line graph representing how many snakes remained after each filter call
# Takes in a list of digits
def filterProg(progress):
    plt.plot(progress, ls='dashdot', color='r')
    plt.show()


# Prints the names of Snakes remaining in snakeDict, or a special message if none remain
# Tales in a dictionary of Snake objects
def printAll(snakeDict):
    if len(snakeDict) == 0:
        print("No snakes meet your criteria!")
    else:
        print("Here are the snakes that meet your criteria:")
        for s in snakeDict:
            print(s)


# Displays a histogram of lengths of snakes remaining in snakeDict
# Takes in a dictionary of Snake objects
def lenHist(snakeDict):
    lengths = []

    # Gathering all the lengths
    for key in snakeDict:
        lengths.append(snakeDict[key].length)

    lengths.sort()
    plt.hist(lengths)
    print("Here is your histogram.")
    plt.show()


# Displays a pie chart depicting venomous/nonvenomousness of snakes remaining in snakeDict
# Takes in a dictionary of Snake objects
def venPie(snakeDict):
    ven = 0
    nonVen = 0

    for key in snakeDict:
        if snakeDict[key].isVen == 0:
            nonVen += 1
        else:
            ven += 1

    y = np.array([ven, nonVen])
    label = ["Venomous", "Nonvenomous"]
    pieColors = ['#b81d13', '#008450']
    plt.pie(y, labels=label, colors=pieColors, startangle=90)
    plt.legend()
    print("Here is your pie chart.")
    plt.show()


# Displays a bar graph of the different colors of the snakes remaining in snakeDict
# Takes in a dictionary of Snake objects
def colorBar(snakeDict):
    colorDict = {}

    # Counts number of appearances for each color
    for key in snakeDict:
        for c in snakeDict[key].colors:
            if c in colorDict:
                colorDict[c] += 1
            else:
                colorDict[c] = 1

    x = []
    y = []
    for key in colorDict:
        x.append(key)
        y.append(colorDict[key])

    # Trying to make the bars the corresponding color
    colorList = []
    for c in x:
        try:
            temp = Color(c)
            if c != "white":
                colorList.append(c)
            else:  # Don't want a white bar on white background
                colorList.append('lightGrey')
        except:  # If c is not a default color
            colorList.append('lightGrey')

    plt.bar(x, y, color=colorList)
    print("Here is your bar graph.")
    plt.show()


def main():
    print("Welcome!")
    getMainCommand(makeSnakeDict(getFile()))


main()
