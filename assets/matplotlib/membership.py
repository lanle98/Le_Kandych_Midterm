import csv
import numpy as np
import matplotlib.pyplot as plt

membership = []
year = [] # push the year data here
categories = []
# open the csv file and parse it
with open("data/membership.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0: # strip the headers out 
             print('pushing text row to city array')
             categories.append(row)
             line_count += 1
        else:
            # collect the medal info
            membershipData = int(row[1])
            membership.append(membershipData)
            yearData = int(row[0])
            year.append(yearData)
            line_count += 1

        


print('processed', line_count - 1, "rows of data")



np_membership = np.array(membership)
np_year = np.array(year)

print(np_membership)
print(np_year)






plt.bar(year, membership, align='center', alpha=1, color='#6BBD4B',edgecolor='white')
plt.yticks([0,10,20,30,40,50,60,70,80,90])
plt.xticks(year)
plt.ylabel('Membership Number', fontweight='bold')
plt.xlabel('Year', fontweight='bold')
plt.title('Membership Number Of TRAA', fontweight='bold')
 
plt.show()
