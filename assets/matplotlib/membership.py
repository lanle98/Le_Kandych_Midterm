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

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = np_year
y_pos = np.arange(len(objects))


performance = np_membership

x_pos = np.arange(len(performance))

print(performance)
print(y_pos)



plt.bar(y_pos, x_pos, align='center', alpha=0.5, color=(0.2,0.4,0.6,1))
plt.xticks(y_pos, objects)
plt.yticks(x_pos, performance)
plt.ylabel('Membership Number')
plt.xlabel('Year')
plt.title('Membership Number Of TRAA')
 
plt.show()
