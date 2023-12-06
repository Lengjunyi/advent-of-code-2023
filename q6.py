s = """Time:        40     82     84     92
Distance:   233   1011   1110   1487"""

times, distances = s.split("\n")
times = map(int, times.split()[1:])
distances = map(int, distances.split()[1:])

times,distances = s.split("\n")
times = times.split(":")[1]
distances = distances.split(":")[1]
times = times.replace(" ", "")
distances = distances.replace(" ", "")
times = [int(times)]
distances = [int(distances)]

ans = 1
for time, dis in zip(times, distances):
    count = 0
    for hold in range(time):
        if hold * (time-hold) > dis:
            count += 1
    ans *= count
print(ans)