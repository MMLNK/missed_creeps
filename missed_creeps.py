time, cs = input("Please provide the time at which the game ended and the number of cs you farmed:\n").split(", ")

cs_int = int(cs)
time_sec = int(time)*60

minion = 0
wave = 1


for i in range(130,time_sec,30):
    if i < 900:
        if wave != 3:
            minion += 6
        elif wave == 3:
            minion += 7
            wave = 1
        wave += 1
    elif i < 1500 and i > 900:
        if wave != 2:
            minion += 6
        elif wave == 2:
            minion += 7
            wave = 1
        wave += 1
    elif i > 1500:
        minion += 7

print(f"You missed approximately {minion-cs_int} creeps")