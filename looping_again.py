# Ask the user to enter their age
# Convert the age to an integer
# Determine the age of an applicant if they qualify to apply for an ID card
age = input("Enter your age: ")

age = int(age)
minimum_age = 18
if age == minimum_age:
    print("You are eligible to apply for an ID card.")
elif age > minimum_age:
    print("You are eligible to apply for an ID card.")
else:
    print("You are not eligible to apply for an ID card.")