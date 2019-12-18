import math
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import texttable as tt
import os

os.system('cls' if os.name == 'nt' else 'clear')

print('-'*20)
print('Modeling Logistic Growth')
print('-'*20)
print('This program will model the spread of a rumor')
print('Each program will take a number of people and a spread rate')
print('(The number of people told the rumor each day')
print()

rumor_list = []
results_list=[(0,1)]

def pause():
    print()
    input("Press Enter to continue...")
    print() 

def trial(num_trials):
    for i in range(num_trials):
        heard_rumor = random.randint(1, num_people)
        print(f'Person number {heard_rumor} heard the rumor.')
        time.sleep(.2)
        if heard_rumor not in rumor_list:
            rumor_list.append(heard_rumor)
    pause()

num_people = int(input('How many people are in your group? '))
num_spread = int(input('How fast does the rumor spread? '))
print()
num_trials = 1
round_num = 1
#Round 1
print('The first person to hear the rumor is ....')
trial(num_trials)
print()

while len(rumor_list) != num_people:
    num_trials = len(rumor_list) * num_spread
    print(f'In Round #{round_num}, {num_trials} people will hear the rumor.')
    pause()
    print(f'Round Number {round_num}')
    print('-'*15)      
    trial(num_trials)
    print()
    print(f'Results of Round #{round_num}')
    print('-'*15)
    print(f'{len(rumor_list)} people have heard the rumor:')
    rumor_list.sort()
    print(rumor_list)       
    results_list.append((round_num,len(rumor_list)))
    round_num+=1
    pause()

print()
print('Final Results Table')
print()

xlist = []
ylist = []
for x, y in results_list:
    xlist.append(x)
    ylist.append(y)

results_table = tt.Texttable()
header = ['Round', 'Total']
results_table.header(header)
for x, y in results_list:
    results_table.add_row([x, y])

results_table.set_cols_width([8,8])
results_table.set_cols_align(['c','c'])
s = results_table.draw()
print(s)



fig = plt.figure(figsize=[6,4])

axes = fig.add_axes([.1,.1,.8,.8])
axes.set_xlabel('Number of Rounds (Days)')
axes.set_ylabel('Heard Rumor')
axes.set_title('Spread of a Rumor')

axes.plot(xlist, ylist, marker ="o", lw=2)
plt.show()







