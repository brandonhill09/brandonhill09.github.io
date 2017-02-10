'''Brandon Hill, and Ashkon Bashkar Period 5'''
import numpy as np
import matplotlib.pyplot as plt
import os.path

#creates the filepath and opens the data file
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'B-Stats.csv')
B_stats = open(filename, 'r')
basket_stats = B_stats.readlines()

#creates an empty list for variables to go to
team_names = []
wins = []
losses = []


#assigns variables to empty lists
for line in basket_stats[1:]:
    line = line[0:-1]
    team_name, win, loss = line.split(',')
    team_names += [team_name]
    wins += [win]
    losses += [loss]
B_stats.close()

#makes a line plot
fig, ax = plt.subplots(1, 1)

ax.plot(losses, 'red')
ax.plot(wins, 'blue')
ax.set_xticklabels(team_names)
ax.set_title('Basketball Statistics: Blue(Wins) Red(Losses)')
ax.set_xlabel('Teams')
ax.set_ylabel('Wins/Losses')
fig.show()