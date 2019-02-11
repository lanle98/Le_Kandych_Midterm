import csv
import numpy as np
import matplotlib.pyplot as plt

membership = []
year = [] # push the year data here
categories = []
# open the csv file and parse it
with open("data/eggs.csv") as csvfile:
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
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 5

recieved = (100000, 150000, 100000, 50000, 150000)
std_recieved = (2000)
hatched = (80000, 120000, 90000, 40000, 140000)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 1
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, recieved, bar_width,
                alpha=opacity, color='#6BBD4B',
                yerr=std_recieved, error_kw=error_config,
                label='Eggs Recieved')

rects2 = ax.bar(index + bar_width, hatched, bar_width,
                alpha=opacity, color='#48E4BD',
                error_kw=error_config,
                label='Eggs Hatched')

ax.set_xlabel('Year')
ax.set_ylabel('Number Of Eggs')
ax.set_title('Number Of Eggs Of Rainbow Trout')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('2014', '2015', '2016', '2017', '2018'))
ax.legend()

fig.tight_layout()
plt.show()