#import packages
import numpy as np
import csv

#collect county average data
infile= r'C:\Users\mpullman\Desktop\New folder\DATA\StormEvents_details-ftp_v1.0_d2016_c20170419.csv'
outfile= r'C:\Users\mpullman\Desktop\New folder\DATA\storm_events_2016.csv'

#create the spring csv file
with open(infile, 'r') as i, open(outfile, 'wb') as o:
   r = csv.reader(i, delimiter=',')
   w = csv.writer(o, delimiter=',')
   for col in r:
       if col[44] != '':
           w.writerow([col[10], col[11], col[12], col[17], col[18],\
                       col[44], col[45]])
    

