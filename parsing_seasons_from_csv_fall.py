import csv

#collect county average data
infile= r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2016.csv'
outfile= r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2016_fall.csv'

#create the spring csv file
with open(infile, 'r') as i, open(outfile, 'wb') as o:
   r = csv.reader(i, delimiter=',')
   header = r.next()
   w = csv.writer(o, delimiter=',')
   w.writerow(header)
   for row in r:
      if row[1] == 'September':
          w.writerow(row)
      elif row[1] == 'October':
          w.writerow(row)
      elif row[1] == 'November':
          w.writerow(row)



