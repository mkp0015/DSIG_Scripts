import numpy as np
from datetime import datetime
import csv
from itertools import izip
import os

infile = r'C:\Users\mpullman\Desktop\desired_columns\DATA\storm_events_2016.csv'
outfile = r'C:\Users\mpullman\Desktop\desired_columns\DATA\storm_events_2016a.csv'
infile2 = r'C:\Users\mpullman\Desktop\desired_columns\DATA\storm_events_2016a.csv'
outfile2 = r'C:\Users\mpullman\Desktop\desired_columns\DATA\storm_events_2016b.csv'

with open(infile, 'r') as f:
    lines = f.readlines()

header = lines[0]
data = lines[1:]

x_dim = len(lines[0].split(','))
y_dim = len(lines)

#create arrays from data
year = []
month_name = []
event_type = []
date_time = []
time_zone = []
begin_lat = []
begin_lon = []

for i in range(0, y_dim-1):
    year.append(data[i].split(',')[0])
    month_name.append(data[i].split(',')[1])
    event_type.append(data[i].split(',')[2])
    date_time.append(data[i].split(',')[3])
    time_zone.append(int(data[i].split(',')[4][-1]))
    begin_lat.append(data[i].split(',')[5])
    begin_lon.append(data[i].split(',')[6])
   
#extract time variables
times = []
hours = []
minutes = []

for i in range(0, y_dim-1):
    times.append(date_time[i].split(' ')[1])

for i in range(0, y_dim-1):
    hours.append(int(times[i].split(':')[0]))

for i in range(0, y_dim-1):
    minutes.append(times[i].split(':')[1])  

#convert lists of data to arrays then concatenate arrays 
hours_arr = np.array(hours)
timez_arr = np.array(time_zone)
utc_hour = hours_arr + timez_arr
for index, item in enumerate(utc_hour):
    if not (item < 24):
        utc_hour[index] = utc_hour[index]-24

#create final utc_time list
utc_time = []
for i in range(0, y_dim-1):
    utc_time.append(str(utc_hour[i])+ ':' + minutes[i])

#write data arrays to output csv file
with open(outfile, 'wb') as o:
    wr = csv.writer(o, delimiter = ',')
    wr.writerow(year)
    wr.writerow(month_name)
    wr.writerow(event_type)
    wr.writerow(date_time)
    wr.writerow(time_zone)
    wr.writerow(utc_time)
    wr.writerow(begin_lat)
    wr.writerow(begin_lon)


a = izip(*csv.reader(open(infile2, 'rb')))
csv.writer(open(outfile2, 'wb')).writerows(a)

#os.remove(outfile)
#os.remove(infile2)
