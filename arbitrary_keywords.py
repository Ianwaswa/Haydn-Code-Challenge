 # In this program use the **kwargs function to print the name of the user in the order of the first name and the last name
def my_function(**name):
    print("Your last name is " + name["lname"])
my_function(fname = "Haydn", lname = "Juma")
