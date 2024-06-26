number_of_laps = int(input("How many times have you run? "))
time_of_lap = 0
time_of_fastest_lap = 0
time_of_slowest_lap = 0
total_time_of_laps = 0
average_time_of_laps = 0
check = False

for x in range(1, number_of_laps +1):
    print("Lap ", x)
    time_of_lap = int(input("Enter the time of the lap in minutes: "))
    while check  ==  True:
        time_of_fastest_lap = time_of_lap
        time_of_slowest_lap = time_of_lap
        check = False
    total_time_of_laps += time_of_lap
        
    if time_of_lap > time_of_slowest_lap:
        time_of_slowest_lap = time_of_lap
    if time_of_lap < time_of_fastest_lap:
        time_of_fastest_lap = time_of_lap
    average_time_of_laps = total_time_of_laps / number_of_laps

print("Fastest lap: ", time_of_fastest_lap)
print("Slowest lap: ", time_of_slowest_lap)
print("Average lap time: ", average_time_of_laps)