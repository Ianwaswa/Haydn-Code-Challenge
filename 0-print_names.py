# Using **kwargs print last name of the user
# Make this a 3 line code

def my_function(**name):
    print("Your last name is " + name["lname"])
my_function(fname = "Haydn", lname = "Juma")
