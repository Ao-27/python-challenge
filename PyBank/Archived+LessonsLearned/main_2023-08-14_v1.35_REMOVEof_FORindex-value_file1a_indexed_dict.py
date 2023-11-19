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

#VIA URL => https://docs.python.org/3/library/csv.html#csv.DictReader
#Try 2 using csv.DictWriter

with open(file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a: #with open("myfile.csv") as f:
    #csv1_headerA = [header.strip() for header in next(csv_file1a).split(",")[1:]]  #next(f).split(",")[1:]] #REPALCED with my own syntax for personal readability.
     readerA = csv.DictReader(csv_file1a)     #WRONG_0starter => readerA = csv.DictReader(file_path1) #NOTE => This has to be "csv_file1a" ... 
     #dict_list_readerA = list(readerA) #dict(list(readerA)) #list(readerA)  #tuple(list(readerA)) #tuple() ADDED HERE for observation in => https://rollbar.com/blog/python-typeerror-unhashable-type-dict-exception/   #... HOWEVER ... note it "didn't enable what I wanted" ... 
     #print(dict_list_readerA)
     for rowA1 in readerA:
         # print(rowA1['Date'],['Profit/Losses'])
         #print(readerA)
         print(rowA1)
# via URL => https://stackoverflow.com/questions/23190074/python-dictionary-error-attributeerror-list-object-has-no-attribute-keys
#CREATE Dict separately to CSV extract above ... 


#Create VARs for dict_list_ReaderA as Keys + Values
file1a_keys = [rowA1.keys()]
file1a_values =  [rowA1.values()]
print(file1a_keys)
print(file1a_values)

#Append/Create INDEX for the List of Dicts produced for the .csv.
#Below via URL => https://stackoverflow.com/questions/36395127/how-to-add-index-into-a-dict




#Initialize Variables for Module 3 Assignment Asks. Loops to provide "+1s" into these as "containers" (conceptually. etc. etc.) ..
total_months = 0
total_net_amount = 0
previous_profit_loss = 0
changes = [0]
greatest_increase = [' ', 0]
greatest_decrease = [' ', 0]