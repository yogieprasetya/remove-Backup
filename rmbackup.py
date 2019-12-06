#!/usr/bin/python

import datetime, os, shutil
from datetime import timedelta, date
from subprocess import call

DIR  = "[backup directory]"
CURR_DATE = datetime.datetime.now()
CURR_YEAR = CURR_DATE.year
CURR_MONTH = CURR_DATE.month
LAST_3DAYS = CURR_DATE.day - 2

print CURR_DATE
print CURR_YEAR
print CURR_MONTH
print LAST_3DAYS

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(CURR_YEAR, CURR_MONTH, 1)
end_date = date(CURR_YEAR, CURR_MONTH, LAST_3DAYS)
for single_date in daterange(start_date, end_date):
    try:	
	os.chdir(DIR)
    	shutil.rmtree(single_date.strftime("%Y-%m-%d")) 
    	date =  single_date.strftime("%Y-%m-%d")
    	print "Removed "+ str(date)
		print end_date
    except Exception as e: print(e)
    continue	
