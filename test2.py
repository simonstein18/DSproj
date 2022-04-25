import csv
# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def test():
    keys = []
    clubs = []

    with open('/Users/simonneuwirth-stein/Desktop/season-1516.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
    
        for row in csvreader:
            keys.append([row[2], row[3], row[6]]) #(Home Team, Away Team, Winner)

            #list of clubs
            if row[2] not in clubs:
                clubs.append(row[2])
        #taking out header
        clubs.pop(0)

    ary = []
    #inserting the club name as the first element in each row of the array
    for i in range(len(clubs)):
        ary.insert(i,[clubs[i]])
        ary[i].append(0)
    
    for match in keys: #[Home Team, Away Team, Winner]
        for i in range(len(ary)): #running through all of the 2d-array of team
            #Home team
            if ary[i][0] == match[0]: # if selected team is Home Team in match
                if match[2] == "H":
                    ary[i].append(3 + ary[i][-1])
                elif match[2] == "A":
                    ary[i].append(0 + ary[i][-1])
                else:
                    ary[i].append(1 + ary[i][-1])
            
            #Away team
            if ary[i][0] == match[1]: # if selected team is Away Team in match
                if match[2] == "A":
                    ary[i].append(3 + ary[i][-1])
                elif match[2] == "H":
                    ary[i].append(0 + ary[i][-1])
                else:
                    ary[i].append(1 + ary[i][-1])
    
    avrg = []
    total = 0
    for i in range(2, len(ary[0])):
        total = 0
        for j in range(len(ary)):
            total += ary[j][i]
        avrg.append(total//20)

    for i in range(len(ary)):
        for j in range(len(avrg)):
            if ary[i][j+2] != 0:
                #ary[i][j+2] = avrg[j] / ary[i][j+2]
                ary[i][j+2] = ary[i][j+2] / avrg[j]
            else:
                ary[i][j+2] = 0
    
    #Visualization
    
    x = np.arange(1, 39) #start x, end x | do not change
    xtix = [i for i in range(39)]
    plt.xticks(xtix[: :3])

    #Plot
    top_5 = ["Leicester", "Arsenal", "Tottenham", "Man City", "Man United"]
    colors = ["Blue", "Crimson", "LightCoral", "Black", "DeepSkyBlue"]
    for i in range(len(ary)):
        if ary[i][0] in top_5:
            plt.plot(x, np.array(ary[i][2:]), label = ary[i][0], color = colors[0])
            colors.pop(0)

    
    #Title
    plt.title("2015-2016 Premier League Season (Top 5)") 
    #Axes Labels
    plt.xlabel("Matchday") 
    plt.ylabel("Normalzied Point Lead")

    # Display
    plt.legend()
    plt.show()


test()