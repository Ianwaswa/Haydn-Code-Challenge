total_days = 5
day = 1
total_bugs = 0

while day <= total_days:
    print("day", day)
    bugs = int(input("How many bugs did you catch? "))
    total_bugs = total_bugs + bugs
    day += 1
    
    print("You caught a total of", total_bugs, "bugs.")