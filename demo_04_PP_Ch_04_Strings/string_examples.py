# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Digression on Strings
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
#
# January 19, 2021
#
# This script shows a few examples of working with
# strings in Python that most commonly occur when
# handling files.
#
##################################################
"""



##################################################
# Import Modules.
##################################################

# Soon we will import modules, which are
# collections of predefined functions. 
# The os module helps us interact with the 
# operating system.
import os # To set working directory



##################################################
# Set Working Directory.
##################################################

# Next, we can use the os module to direct the Python interpreter
# to work in a particular folder, often called a directory.

# Find out the current directory.
os.getcwd()
# Change to a new directory.
# You will have to specify a correct path on your own computer. 
os.chdir('C:\\Users\\le279259\\Documents\\Teaching\\ECP3004_Spring_2021\\GitRepo\\ECP3004S21\\demo_04_PP_Ch_04_Strings')
# os.chdir('C:\Users\le279259\Documents\Teaching\QMB6358_Fall_2020\GitRepos\QMB6358F20\demo_12_linear_models_in_python')
# Check that the change was successful.
os.getcwd()

# This preliminary step is often problematic because
# paths to directories often use special characters. 
# To execute a change in directory, you should
# understand how to define a string that represents
# your path. 


##################################################
# Digression about slashes in strings
# For handling text files.
##################################################

# Much of file IO is about handling strings.
# When you read and write to the computer, 
# you read and write character strings
# to and from the files.


# What's going on with the slashes and double slashes?
# A slash is a special character
"C:/Users/le279259/Documents/Teaching/QMB6358_Fall_2020/GitRepos/QMB6358F20"
# For this reason, python allows forward slashes in paths. 

# A slash can also replicate other buttons on your keyboard.
# for example '\t' prints a tab.
print("This\tis\ta\ttab")
# '\n' creates a new line, like the return button:
print("These\nare\nseparate\nlines")


# You have to be careful about what you put in a string.
# For quotes inside quotes, single quotes can appear in double quotes.
"This won't throw an error"

# If you used single quotes on the outside, you would need
# to use the slash to tell python that you actually 
# want to print an apostrophe, instead of endint the 
# string after 'This isn'.
'This won\'t throw an error'
# but
# 'This won't run without error'
# will throw an error. 

# The same goes if you want to print a double quote
# inside a string:
"This is a \"string\" inside a string"
# That prints as expected.
# but this throws an error:
# "This is two "strings" instead of one string"
# because Python prematurely ends the string at the second quote.

# These tricks will be useful for the sections on File IO
# and for loading data from spreadsheets.
# You use strings for the path to the file
# and the contents of many files are represented as strings. 


##################################################
# End
##################################################