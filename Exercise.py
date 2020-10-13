Q: How do I get a number from someone so I can do math?
A: That?s a little advanced, but try x = int(raw_input()), which gets the number as a string from
	 raw_input() then converts it to an integer using int().

#=======================================================================
#Example 1

print "How old are you?",

age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

#Example 2

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

#=========================================================================

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#Run the program like this (and you must pass three command line arguments before running script):

$ python ex1.py first 2nd 3rd
The script is called: ex13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd

#====================================================================
#combining argv with raw_input()

from sys import argv

script, first, second, third = argv
fourth = raw_input()

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

#Run the program like this (and you must pass three command line arguments before running the script and add the fourth when prompted by raw_input):

$ python ex1.py first 2nd 3rd
The script is called: ex13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd
Your fourth variable is: 4th
#====================================================================

from sys import argv

script, user_name = argv
prompt = '> '			#the variable prompt is assigned a string 

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)									#prompt string is then given to raw_input() so  "> " is displayed when a user is requested to type in information,

print "Where do you live %s?" % user_name
lives = raw_input(prompt)									#raw_input() can store multiple inputs

print "What kind of computer do you have?"
computer = raw_input(prompt)							#third input stored in raw_input()

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)						#spits out out all the stored inputs in raw_input()

#=====================================================================

from sys import argv

script, age, user_name = argv
user_input = '> '

year_older = int (age) + 1			#converts arg "age" from a string to an int

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(user_input)

print "Where do you live %s?" % user_name
lives = raw_input(user_input)

print "What kind of computer do you have?"
computer = raw_input(user_input)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You have a %r computer and you
will be %r years old next year
""" % (likes, lives, computer, year_older)

# int() is the Python standard built-in function to convert a string into an integer value. 
# You call it with a string containing a number as the argument, and it returns the number 
# converted to an integer:

# print (int("1") + 1)
