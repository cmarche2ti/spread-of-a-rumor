import math
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import texttable as tt
import os

# Clear console on start of the program
os.system("cls" if os.name == "nt" else "clear")

# User directions
print("-" * 24)
print("Modeling Logistic Growth")
print("-" * 24)
print("This program will model the spread of a rumor")
print("The program will take a number of people and a spread rate")
print("(The number of people told the rumor each day) as input.")
print()

rumor_list = []
results_list = [(0, 1)]


def pause():
    print()
    input("Press Enter to continue...")
    print()


def trial(num_trials):
    for _ in range(num_trials):
        heard_rumor = random.randint(1, num_people)
        print(f"Person number {heard_rumor} heard the rumor.")
        time.sleep(0.2)
        if heard_rumor not in rumor_list:
            rumor_list.append(heard_rumor)
    pause()


while True:
    try:
        num_people = int(input("How many people are in your group? "))
        break
    except:
        print("The number of people must be a positive integer")
        print()

while True:
    try:
        num_spread = int(input("How fast does the rumor spread? "))
        break
    except:
        print("The rate of spread must be a positive integer")
        print()


print()
print(f"People in group: {num_people}")
print(f"Rate of spread: {num_spread}")
print()
num_trials = 1
round_num = 1

# Round 1
print("The first person to hear the rumor is ....")
trial(num_trials)
print()

# All rounds after round 1
while len(rumor_list) != num_people:
    num_trials = len(rumor_list) * num_spread
    print(f"In Round #{round_num}, {num_trials} people will hear the rumor.")
    pause()
    print(f"Round Number {round_num}")
    print("-" * 15)
    trial(num_trials)
    print()
    print(f"Results of Round #{round_num}")
    print("-" * 15)
    print(f"{len(rumor_list)} people have heard the rumor:")
    rumor_list.sort()
    print(rumor_list)
    results_list.append((round_num, len(rumor_list)))
    round_num += 1
    pause()

# Display results table in the console
print()
print("Final Results Table")
print()

xlist = []
ylist = []
for x, y in results_list:
    xlist.append(x)
    ylist.append(y)

results_table = tt.Texttable()
header = ["Round", "Total"]
results_table.header(header)
for x, y in results_list:
    results_table.add_row([x, y])

results_table.set_cols_width([8, 8])
results_table.set_cols_align(["c", "c"])
s = results_table.draw()
print(s)


# Create graph of results
fig = plt.figure(figsize=[6, 4])

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.set_xlabel("Number of Rounds (Days)")
axes.set_ylabel("Heard Rumor")
axes.set_title("Spread of a Rumor")

axes.plot(xlist, ylist, marker="o", lw=2)
plt.show()
