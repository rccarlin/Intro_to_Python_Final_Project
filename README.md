# Intro to Python Final Project
Note: this code was originally written in Fall 2021 semester, and this README is a modified version of my submitted project description.

## Goals
- Utilize arithmetic operators
- Utilize list techniques
- Utilize conditional statements
- Utilize file I/O to read files
- Utilize objects
- Utilize dictionaries
- Utilize loops to repeat certain code blocks
- Utilize functions to streamline logic and code
- Produce graphs in Python
- Perform Google searches in Python

## Overall Description
- A dichotomous key is a tool for identifying organisms based on visual characteristics
like coloration, shape, and size. The user will have an [unnamed] organism in mind 
and the key will ask questions to try to guess the identity of said organism. 
Unfortunately, a dichotomous key requires a fixed pool of potential organisms to begin 
with. However, we can at least narrow down an arbitrary set of organisms by filtering 
them based on their characteristics (similar to how one filters products while online 
shopping). Like with online shopping, if the user already knows what they are looking 
for they should be allowed to search the name of the organism (bypassing the filtering 
stage).
- But sometimes the user is less concerned about a specific organism and more 
interested in a set of organisms. Graphs provide a helpful visual summary of the data; 
when used in the context of studying organisms, graphs can depict the distribution 
and/or popularity of certain characteristics.
- This program will not only allow the user to search and filter from a file of snakes (the 
organism of choice when coding in python), but will also create graphs for traits like 
length, color, venomousness for both the entire set of snakes and for the filtered 

## Input and Commands
- The program will begin by asking the user for an input file of snakes and snake 
information. One line per snake. The lines should be formatted as follows:
  - Name|average length in meters|isVenomous|color,color,color…
  - Ex: Ball python|1.13|0|brown
  - Ex: Eastern Coral Snake|.8|1|red,black,yellow
- The user is then offered the option to search a snake by name, filter snakes by 
characteristics, view statistics about all the snakes, or exit the program (make sure to 
verify the user inputted a valid request).
- Search: prompt the user to enter a snake name, either print out the 
characteristics of the snake or alert the user that the program does not have 
information on that snake. If the snake does exist, the program will ask the 
user if they would like to see pictures of the snake and if they would like 
additional reading on the snake. Agreeing to the pictures will open up a 
new browser tab on the Google image search results for that snake. 
Agreeing to the additional reading will return five links a Google search 
on the snake would return.
- Filter: Take user to secondary menu that allows them to filter by any of the 
characteristics. Current session continues until user selects Back (that means 
the user can continue filtering after printing results). Make sure user inputs 
valid commands and answers.
  - Name: removes snakes whose names don’t contain any of the user 
inputted words
  - Length: prompts the user for an (in)equality sign and then for a number, 
removes snakes whose length does not satisfy the expression
  - Venomousness: user inputs y or n for if the snake is venomous, removes 
snakes that don’t fit the criteria
  - Color: prompts the user for one color, removes any snakes that don’t 
have that color
  - Print results: prints names of remaining snakes (snakes that have so far 
satisfied all of the filters)
  - Stats: takes user to the stats menu (discussed below) but will make the 
graphs using only the remaining snakes
 - Filter Progress: creates a line graph representing how many snakes 
have been left after each filter command (name, length, 
venomousness, color)
  - Back: takes user back to main menu
- Stats: Take user to secondary (or possibly tertiary, if coming from the filter 
menu) menu that allows them to select what characteristics they would like to 
see in graph form. Will prompt the user for which graph they want (and 
provide the graph) until the user selects Back. As always, verify that the user 
inputted a valid request.
  - Length: makes a histogram of snake lengths; x axis has a range of lengths 
(e.g.: 0-30 cm, 31-60 cm…), y axis is the number of snakes whose 
average length falls in that range
  - Venomousness: makes a pie chart depicting the percent of snakes that 
are and aren’t venomous
  - Color: makes a bar graph depicting number of snakes known to be/ have 
that color (because some snakes are multi-colored, the sum of the bars’ 
values may be more than the total number of snakes); x axis is color, y 
axis is number of snakes
  - Back: takes user back to whichever menu they were on when they called 
stats
– Exit: terminates program
