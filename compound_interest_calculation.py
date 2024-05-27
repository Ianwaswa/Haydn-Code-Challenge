# Have the users enter their investment amount and their expected interest.
# Each year their investment will increase by their investment + their investment * the interest rate.
# Print out their earnings after a 10 year period.
investment = float(input("Enter your investment amount: "))
expected_interest = float(input("Enter your expected interest: "))
interest_rate = 1 + expected_interest
for i in range(1, 11):
    investment = investment * interest_rate
    print(f"Year {i}: ${investment:.2f}")
# Output: