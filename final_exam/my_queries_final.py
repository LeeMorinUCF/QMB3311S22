#!/usr/bin/python
"""
##################################################
# 
# QMB 3311: Python for Business Analytics
# 
# Using Databases with SQLite3
#
# Name: 
#
# Date:
# 
# Sample Program for Final Examination
# 
##################################################
"""


##################################################
# Import Modules.
##################################################


import os # To set working directory
import pandas as pd # To read and inspect data

# You would import some kind of API 
# to interact with the database
# We will continue using sqlite3
import sqlite3 as dbapi




##################################################
# Set Working Directory.
##################################################



# Find out the current directory.
os.getcwd()
# Change to a new directory.
drive_path = 'C:\\Users\\le279259\\OneDrive - University of Central Florida\\Documents\\'
git_path = 'Teaching\\UCF_QMB6358\\QMB6358_Spring_2022\\GitRepo\\BA_Assignments\\QMB3311S22\\'
os.chdir(drive_path + git_path + 'final_exam')
# Check that the change was successful.
os.getcwd()





##################################################
### Question 5 a) Create the Database
##################################################


# a. Create a new database called credit.db.

#--------------------------------------------------
# Code goes here.



# Code goes here.
#--------------------------------------------------


##################################################
### Question 5 b) i) Create the Applications Table
##################################################


# b) i) Read in the applications.csv dataset 
# and store the contents in a table called
# Applications.

#--------------------------------------------------
# Code goes here.



# Code goes here.
#--------------------------------------------------



# CREATE a TABLE called Applications with a schema 
# that is appropriate for the variables.

#--------------------------------------------------
# Code goes here.



# Code goes here.
#--------------------------------------------------


# Populate the table Applications.


#--------------------------------------------------
# Code goes here.




# Code goes here.
#--------------------------------------------------

# Retrieve the contents of the table to check.

# cur.execute('SELECT * FROM Applications')
# for row in cur.fetchall()[1:20]:
#  print(row)



##################################################
### Question 5 b) ii) Create the CreditBureau Table
##################################################


# b) ii) Read in the credit_bureau.csv dataset 
# and store the contents in a table
# called CreditBureau.

#--------------------------------------------------
# Code goes here.



# Code goes here.
#--------------------------------------------------


# CREATE a TABLE called CreditBureau with a schema 
# that is appropriate for the variables.

#--------------------------------------------------
# Code goes here.




# Code goes here.
#--------------------------------------------------



# Populate the table CreditBureau.


#--------------------------------------------------
# Code goes here.






# Code goes here.
#--------------------------------------------------

# Retrieve the contents of the table to check.

# cur.execute('SELECT * FROM CreditBureau')
# for row in cur.fetchall()[1:20]:
#  print(row)



##################################################
### Question 5 b) iii) Create the Demographic Table
##################################################


# b) iii) Read in the demographic.csv dataset 
# and store the contents in a table 
# Demographic.

#--------------------------------------------------
# Code goes here.




# Code goes here.
#--------------------------------------------------



# CREATE a TABLE called Demographic with a schema 
# that is appropriate for the variables.

#--------------------------------------------------
# Code goes here.




# Code goes here.
#--------------------------------------------------



# Populate the table Demographic.


#--------------------------------------------------
# Code goes here.






# Code goes here.
#--------------------------------------------------

# Retrieve the contents of the table to check.

# cur.execute('SELECT * FROM Demographic')
# for row in cur.fetchall()[1:20]:
#  print(row)










##################################################
### Question 5 c) Query the Database
### Part i)
##################################################



#--------------------------------------------------
# Code goes here.




# Code goes here.
#--------------------------------------------------




##################################################
### Question 5 c) Query the Database
### Part ii)
##################################################



# c) ii) Join the relevant tables and calculate the required quantities.


#--------------------------------------------------
# Code goes here.





# Code goes here.
#--------------------------------------------------




##################################################
### Question 5 c) Query the Database
### Part iii)
##################################################



# c) iii) Join the relevant tables and calculate the required quantities.

#--------------------------------------------------
# Code goes here.




# Code goes here.
#--------------------------------------------------




##################################################
### Question 5 c) Query the Database
### Part iv)
##################################################



# c) iv) Join the relevant tables and calculate the required quantities.

#--------------------------------------------------
# Code goes here.




# Code goes here.
#--------------------------------------------------




##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
con.commit()


# Close the connection when finished. 
con.close()



##################################################
# End
##################################################
