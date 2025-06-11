# Lap Time Recorder

# Method 1
total = 0
fastest = 9999
slowest = 0

laps = int(input("Enter the number of laps: "))

for i in range(laps):
    lap_time = float(input("Enter lap time in seconds: "))
    if lap_time < fastest:
        fastest = lap_time
    if lap_time > slowest:
        slowest = lap_time
    total += lap_time

print("Fastest lap time: ", fastest, " seconds")
print("Slowest lap time: ",slowest," seconds")  
print("Average lap time: ", total / laps, " seconds")

print("\n")

# Method 2
lapTimes = []
laps = int(input("Enter the number of laps: "))

for i in range(laps):
    lap_time = float(input("Enter lap time in seconds: "))
    lapTimes.append(lap_time)

fastest = min(lapTimes)
slowest = max(lapTimes)

print("Fastest lap time: ", min(lapTimes), " seconds")
print("Slowest lap time: ", max(lapTimes), " seconds")
print("Average lap time: ", sum(lapTimes) /len(lapTimes), " seconds")    