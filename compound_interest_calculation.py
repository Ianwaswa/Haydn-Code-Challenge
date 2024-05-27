# Ask for the money and the interest rate
# Convert the value to float and round it to 2 decimal places
# Cycle through a period of 10 years using a for loop
# Print the result
money = input("How much do you want to invest? ")
interest_rate = input("What is the interest rate? ")
money = float(money)
interest_rate = float(interest_rate) * .01
for i in range(10):
    money = money + (money * interest_rate)
print("Investment after 10 years : {:.2f}".format(money))
