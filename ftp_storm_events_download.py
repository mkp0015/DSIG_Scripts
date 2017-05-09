#********************************************************
# FILE: homework4.py
# AUTHOR: Melinda Pullman 
# EMAIL: mkp0015@uah.edu
# MODIFIED BY: n/a
# ORGANIZATION: UAH/ATS Dept.
# CREATION DATE: 04/20/2017
# LAST MOD DATE: n/a
# PURPOSE: This script downloads a storm events CSV file from
#          the storm events database FTP site, extracts the CSV
#          file from the zipped file, then makes an XY event layer
#          from the csv file data.
# DEPENDENCIES: os, ftplib, gzip, arcpy
#********************************************************

#import dependencies 
import os, ftplib
import gzip
import arcpy

#declare variables
destdir = r'C:\Users\mpullman\Desktop\test2'
filename = 'StormEvents_locations-ftp_v1.0_d2016_c20170419.csv.gz'

#login to FTP
ftp = ftplib.FTP('ftp.ncdc.noaa.gov', 'anonymous')

#change directory in FTP
ftp.cwd('pub/data/swdi/stormevents/csvfiles/')

#save file to local directory
local_file = os.path.join(destdir, filename)
ftp.retrbinary('RETR %s' % filename, open(local_file, 'wb').write)

#close connection to FTP
ftp.quit()

#extract csv from zipped file
infile = gzip.GzipFile(local_file, 'rb')
s = infile.read()
infile.close

#save csv file in same destination directory
outfile = file(local_file[0:-2], 'wb')
outfile.write(s)
outfile.close()

