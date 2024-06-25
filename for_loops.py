successful = False
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
    if successful:
        print("Successful")
        break
else:
    print("Unsuccessful")