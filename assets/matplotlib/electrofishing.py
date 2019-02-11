import csv
import numpy as np
import matplotlib.pyplot as plt

membership = []
year = [] # push the year data here
categories = []
# open the csv file and parse it
with open("data/electrofishing.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0: # strip the headers out 
             print('pushing text row to city array')
             categories.append(row)
             line_count += 1
        else:
            # collect the medal info
            membershipData = row[1]
            membership.append(membershipData)
            yearData = row[0]
            year.append(yearData)
            line_count += 1

        


print('processed', line_count - 1, "rows of data")



np_membership = np.array(membership)
np_year = np.array(year)

print(np_membership)
print(np_year)



import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [15, 10, 13]
bars2 = [14, 18, 15]
bars3 = [23, 12, 14]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot
plt.bar(r1, bars1, color='#6BBD4B', width=barWidth, edgecolor='white', label='Komoka')
plt.bar(r2, bars2, color='#48E4BD', width=barWidth, edgecolor='white', label='Oxbow')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='Dingman')
 
# Add xticks on the middle of the group bars
plt.xlabel('Year', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['2016', '2017', '2018'])
plt.ylabel("Number Of Fishes")
plt.title("Electro Fishing")

# Create legend & Show graphic
plt.legend()
plt.show()

