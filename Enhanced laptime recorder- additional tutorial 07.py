total = 0
fastest = 9999
slowest = 0
count = 1

while True:
    lap_time = input(f"Enter lap time {count} ('x' to end): ")  
    if lap_time == 'x':
        break
    else:
        lap_time = float(lap_time)
        if lap_time < fastest:
            fastest = lap_time
        if lap_time > slowest:
            slowest = lap_time
        total += lap_time
        count += 1

print("\n")
print("Fastest lap time: ", fastest, " seconds")
print("Slowest lap time: ", slowest, " seconds")
print("Average lap time:", total / (count - 1), "seconds")