import logging
import csv
from datetime import date
from wallwriteBeta import *

eventLog = open('fb_eventLog.txt', 'r+')
eventLogList = []
for element in eventLog:
     eventLogList.append(element)
eventLogList = ''.join(eventLogList)
    

csvfile = open("fb_birthdays.csv")
dialect = csv.Sniffer().sniff(csvfile.read(1024))
csvfile.seek(0)
reader = csv.reader(csvfile, dialect)
# date variable
dRaw = date.today()
d = dRaw.strftime("%m/%d")
x = dRaw.strftime("%x")
birthdays = ['no birthdays today']



def run():

    for row in reader:
          if d in row:
            if ((', '.join(row))) in eventLogList:
                print('Action committed too recently')
                logging.info(': DID NOT WRITE '
                               + row[1] + ' : Already written')
            else:
                print('Wrote Happy Birthday too ' + row[1])
                print(', '.join(row))
                logging.info(': Wrote To '
                               + row[1])
                write(row[2], "happy birthday")
                eventLog.write(x + "--" +', '.join(row) + "\n")
                birthdays.append(row[1])


    eventLog.close()
            
            
