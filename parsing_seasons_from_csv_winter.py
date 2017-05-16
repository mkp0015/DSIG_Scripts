import csv


#collect county average data
infile= r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2014.csv'
infile2 = r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2013.csv'
outfile= r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2014_winter.csv'

#create the spring csv file
with open(infile, 'r') as i, open(outfile, 'wb') as o, open(infile2, 'r') as i2:
   r = csv.reader(i, delimiter=',')
   header = r.next()
   w = csv.writer(o, delimiter=',')
   w.writerow(header)
   for row in r:
      if row[1] == 'January':
          w.writerow(row)
      elif row[1] == 'February':
          w.writerow(row)
   r2 = csv.reader(i2, delimiter=',')
   for row in r2:
      if row[1] == 'December':
         w.writerow(row)

#collect county average data
infile= r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2015.csv'
infile2 = r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2014.csv'
outfile= r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2015_winter.csv'

#create the spring csv file
with open(infile, 'r') as i, open(outfile, 'wb') as o, open(infile2, 'r') as i2:
   r = csv.reader(i, delimiter=',')
   header = r.next()
   w = csv.writer(o, delimiter=',')
   w.writerow(header)
   for row in r:
      if row[1] == 'January':
          w.writerow(row)
      elif row[1] == 'February':
          w.writerow(row)
   r2 = csv.reader(i2, delimiter=',')
   for row in r2:
      if row[1] == 'December':
         w.writerow(row)

#collect county average data
infile= r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2016.csv'
infile2 = r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2015.csv'
outfile= r'C:\Users\mpullman\Desktop\seasons_w_utc_time\storm_events_2016_winter.csv'

#create the spring csv file
with open(infile, 'r') as i, open(outfile, 'wb') as o, open(infile2, 'r') as i2:
   r = csv.reader(i, delimiter=',')
   header = r.next()
   w = csv.writer(o, delimiter=',')
   w.writerow(header)
   for row in r:
      if row[1] == 'January':
          w.writerow(row)
      elif row[1] == 'February':
          w.writerow(row)
   r2 = csv.reader(i2, delimiter=',')
   for row in r2:
      if row[1] == 'December':
         w.writerow(row)
