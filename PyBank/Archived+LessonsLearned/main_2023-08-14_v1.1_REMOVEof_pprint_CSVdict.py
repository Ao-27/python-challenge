#Import Dependencies for loading Started Data/Code.
import os
import csv

#Confirm actual Current Directory for Building out Path.
current_dir = os.getcwd()
#Validate location of current_dir in relation to Resources "Source Data" files.
print(current_dir)

#Create VARs for File Paths for code simplicity.
source1_csv_file = "budget_data.csv" #Title of File for Fetch.
#output1_file = ".txt" #Commented OUT until I actually need it.

#Use OS module to Fetch CSV data and read Source Data into Python for manipulation.
file_path1 = os.path.join("Resources",source1_csv_file) #NOTE: I'm not in an "Unsolved" folder like in class. So no ".." should be necessary.
print(file_path1)

#Convert to dict to show data via URL => https://stackoverflow.com/questions/35829360/python-read-csv-file-with-row-and-column-headers-into-dictionary-with-two-keys

from pprint import pprint

path1_dict = {}
with open(file_path1, 'r') as csv_file1: #with open("myfile.csv") as f:
    csv1_header = [header.strip() for header in next(csv_file1).split(",")[1:]]  #next(f).split(",")[1:]] #REPALCED with my own syntax for personal readability.

    for csv1_row in csv_file1: #for line in f: #REPLACED same as above... #NOTE don't forget the ":" ... 
        csv1_row_values = [value.strip() for value in csv1_row.split(",")]  # line.split(",")] #REPLACED same as above.
        path1_dict[csv1_row_values[0]] = dict(zip(csv1_header,csv1_row_values[1:]))  #d[values[0]] = dict(zip(headers, values[1:])) #REPLACED same as above.

pprint(path1_dict)  #pprint(d)

#VIA URL => https://docs.python.org/3/library/csv.html#csv.DictReader
#Try 2 using csv.DictWriter

with open(file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a: #with open("myfile.csv") as f:
    #csv1_headerA = [header.strip() for header in next(csv_file1a).split(",")[1:]]  #next(f).split(",")[1:]] #REPALCED with my own syntax for personal readability.
     readerA = csv.DictReader(csv_file1a)     #WRONG_0starter => readerA = csv.DictReader(file_path1) #NOTE => This has to be "csv_file1a" ... 
     dict_list_readerA = list(readerA)
     for rowA1 in readerA:
         # print(rowA1['Date'],['Profit/Losses'])
         #print(readerA)
         print(rowA1)
         print(dict_list_readerA)














#Initialize Variables for Module 3 Assignment Asks. Loops to provide "+1s" into these as "containers" (conceptually. etc. etc.) ..
total_months = 0
total_net_amount = 0
previous_profit_loss = 0
changes = [0]
greatest_increase = [' ', 0]
greatest_decrease = [' ', 0]