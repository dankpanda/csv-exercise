import csv
import statistics
import matplotlib.pyplot as plt
# 1
with open('activity.csv') as f:
    steps_per_day = {}
    f_read = csv.reader(f)
    for row in f_read:
        if row[0] != 'steps':
            if row[0] != 'NA':
                if row[1] not in steps_per_day.keys():
                    steps_per_day[row[1]] = int(row[0])
                else:
                    steps_per_day[row[1]] += int(row[0]) 
    

with open('activity.csv') as f:
    f_read = csv.reader(f)
    interval_steps_per_day = {}
    for row in f_read:
        if row[1] != 'date' and row[0] != 'NA' and row[0] != '0':
                if row[1] not in interval_steps_per_day.keys():
                    interval_steps_per_day[row[1]] = [int(row[0])]
                else:
                    interval_steps_per_day[row[1]].append(int(row[0]))

mean_per_day = {}
median_per_day = {}
for key,value in interval_steps_per_day.items():
        mean_per_day[key] = round(statistics.mean(value),2)
        median_per_day[key] = statistics.median(value)

data = steps_per_day.values()
labels = steps_per_day.keys()
plt.xticks(range(len(data)), labels)
plt.xlabel('Date')
plt.ylabel('Total Steps')
plt.title('Total steps per day')
plt.bar(range(len(data)), data) 
plt.show()

# I can't figure out how to make a scattergraph with matplotlib because I keep getting the same error and idk how to fix it :(. I also have no idea how to put the logic of 2B into a code

# 3
na_counter = 0
new_dict = {}
with open('activity.csv','r') as f:
    f_read=csv.reader(f)

    for row in f_read:
        if row[0] == 'NA':
            na_counter +=1
            row[0] =0
    
with open('activity.csv','r') as f:
    f_read = csv.reader(f)

    for row in f_read:
        if row[0] == 'NA':
            row[0] = 0
        if row[1] != 'date':
            if row[1] not in new_dict.keys():
                new_dict[row[1]] = [int(row[0])]
            else:
                new_dict[row[1]].append(int(row[0]))

data = steps_per_day.values()
labels = steps_per_day.keys()
plt.xticks(range(len(data)), labels)
plt.xlabel('Date')
plt.ylabel('Total Steps')
plt.title('Total steps per day')
plt.bar(range(len(data)), data) 
plt.show()
print(na_counter)
new_mean = {}
new_median = {}
for key,value in new_dict.items():
        new_mean[key] = round(statistics.mean(value),2)
        new_median[key] = statistics.median(value)
print(mean_per_day,median_per_day)
print(new_mean,new_median)

# 4
import calendar
temp = []
year=[]
month=[]
date=[]
new_dict_week = {'weekday':[],'weekend':[]}
with open('activity.csv','r') as f:
    f_read = csv.reader(f)
    for row in f_read:
        if row[1] != 'date':
            temp = row[1].split('-')
            year.append(temp[0])
            month.append(temp[1])
            date.append(temp[2])

    def weekcheck(year,month,date):
        return calendar.weekday(year,month,date)
        
f_read0 = []
f_read2 = []
with open('activity.csv','r') as f:
    f_read = csv.reader(f)
    
    for row in f_read:
        if row[1] != 'date':
            f_read0.append(row[0])
            f_read2.append(row[2])
for i in range(len(f_read0)):
    if f_read0[i] == 'NA':
        f_read0[i] = 0

for i in range(len(year)):
    if weekcheck(int(year[i]),int(month[i]),int(date[i])) < 5:
        new_dict_week['weekday'].append([f_read0[i],str(year[i])+'-'+str(month[i])+'-'+str(date[i]),f_read2[i]])
    else:
        new_dict_week['weekend'].append([f_read0[i],str(year[i])+'-'+str(month[i])+'-'+str(date[i]),f_read2[i]])

print(new_dict_week)

# i have no idea how to do number 4b ...
    
    
