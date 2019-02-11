import csv
import numpy as np
import matplotlib.pyplot as plt

received = []
hatched = []
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
        elif  line_count <= 5:
            # collect the medal info
            receivedData = float(row[2])
            received.append(receivedData)
            hatchedData = float(row[3])
            hatched.append(hatchedData)
            yearData = float(row[1])
            year.append(yearData)
            line_count += 1

        


print('processed', line_count-1, "rows of data")



np_received = np.array(received)
np_year = np.array(year)
np_hatched= np.array(hatched)

print(np_received)
print(np_hatched)
print(np_year)



n_groups = 5

bar1 = np.arange(len(np_received))


index = np.arange(n_groups)

barWidth = 0.25


r1 = np.arange(len(bar1))
r2 = [x + barWidth for x in r1]


# opacity = 1
# error_config = {'ecolor': '0.3'}

# rects1 = ax.bar(index, receivedChart, bar_width,
#                 alpha=opacity, color='#6BBD4B',
#                 yerr=std_recieved, error_kw=error_config,
#                 label='Eggs Received', edgecolor='white')

# rects2 = ax.bar(index + bar_width, hatchedChart, bar_width,
#                 alpha=opacity, color='#48E4BD',
#                 error_kw=error_config,
#                 label='Eggs Hatched', edgecolor='white')

plt.bar(r1, received, color='#6BBD4B', width=barWidth, edgecolor='white', label='Eggs Received')
plt.bar(r2, hatched, color='#48E4BD', width=barWidth, edgecolor='white', label='Eggs Hatched')

# Add xticks on the middle of the group bars
plt.xlabel('Year', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bar1))], ['2014','2015','2016', '2017', '2018'])
plt.yticks([0, 20000, 40000, 60000, 80000, 100000, 120000])
plt.ylabel("Number Of Eggs", fontweight='bold')
plt.title("Brown Trout Eggs", fontweight='bold')

# Create legend & Show graphic
plt.legend()
plt.show()