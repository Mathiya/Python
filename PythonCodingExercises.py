#my_name = 'Big Muta'
#my_age = 35 #not a lie
#my_height = 74 #inches
#my_weight = 180 #lbs
#my_eyes = 'Brown'
#my_teeth = 'porcelain white'
#my_hair = 'Black'


#print "Let's talk about %s" % my_name
#print "He's %d inches in height" % my_height
#print "He weighs in at %d lbs" % my_weight
#print "He's teeth are %s all the time, even when his had a cup of coffee" % my_teeth
#print "He has beautiful %s hair and piercing %s eyes" % (my_hair, my_eyes)


#i = 1
#j = 2.0
#x = 3

#print i + j
#print x / j
#print i - x
#print j * x

#x = "there are %d types of people." % 10
#binary = "binary"
#do_not = "don't"
#y = "those who know %s and those who %s." % (binary, do_not)

#print "I said: %r." % x
#print "I also said: '%s'." %

#formatter = "%r %r %r %r"

#print formatter % (1,2,3,4)
#print formatter % ("one", "two", "three", "four")
#print formatter % (formatter, formatter, formatter, formatter)
#print formatter %(
#"I had this thing.",
#"that you could type upright.",
#"But it didn't sing.",
#"So I said goodnight."
#)

#days = "Mon Tue Wed Thur Fri Sat Sun"
#months = "jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#print "Here are the days: ", days
#print "Here are the months:", months

#print """
#There's something going on here.
#With the three double-quotes.
#We'll be able to type as much as we like.
#Even 4 lines if we want, or 5, or 6.
#"""

#tabby_cat = "\rI'm tabbed in."
#persian_cat = "I'm \\a \\ cat."
#backslash_cat = "I'm \\ a \\ cat."

#fat_cat = """
#\t* Cat food
#\t* Fishies
#\t* Catnip\n\t* Grass
#"""

#print tabby_cat
#print persian_cat
#print backslash_cat
#print fat_cat

#age = raw_input("How tall are you?")
#height = raw_input("How old are you?")
#weight = raw_input("How much do you weigh?")

#print "So, you'er %s old, %s tall and %s heavy." % (
#age, height, weight)

#from sys import argv

#script, first, second, third = argv
#fourth = raw_input()
 
#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third
#print "Your fourth variable is: %r" %fourth

from sys import argv

script, age, user_name = argv
user_input = '> '

year_older = int (age) + 1

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

