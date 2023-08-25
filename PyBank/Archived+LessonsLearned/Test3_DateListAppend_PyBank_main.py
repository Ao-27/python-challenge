#Import Dependencies for loading Started Data/Code.
import os
import csv

#Confirm actual Current Directory for Building out Path.
current_dir = os.getcwd()
#Validate location of current_dir in relation to Resources "Source Data" files.
print(current_dir)
print("-------")

#Create VARs for File Paths for code simplicity.
source1_csv_file = "budget_data.csv" #Title of File for Fetch.
#output1_file = ".txt" #Commented OUT until I actually need it.

#Use OS module to Fetch CSV data and read Source Data into Python for manipulation.
file_path1 = os.path.join("Resources",source1_csv_file) #NOTE: I'm not in an "Unsolved" folder like in class. So no ".." should be necessary.
print(file_path1)
print("-------")

#new v1.2 target => https://stackoverflow.com/questions/29432912/convert-a-csv-dictreader-object-to-a-list-of-dictionaries

import collections  #via => https://stackoverflow.com/questions/28283647/convert-csv-column-to-list
csv1a_dict = collections.defaultdict(list)
with open(file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a: #,newline='') as csv_file1a: 
     header1a = next(csv_file1a).strip().split(",")
     csv1a_width = len(header1a)
     print("Test - csv reader headers are:")
     print(header1a)
     print("-+-+-+-+-+-")
     print(f"The width of the CSV is : {csv1a_width}") #via => https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
     print("-+-+-+-+-+-")
     header_dict_1a1 = dict(enumerate(list(header1a)))
     print("The Header Column Indexes as Keys Dictionary:")
     print(header_dict_1a1)
     print("-------")
     print("The Header Column as Keys Dictionary:") #via => DIDN'T work ... but via Medium somewhere.
     Dict1a_fromkeys = dict.fromkeys(list(header1a))
     print(Dict1a_fromkeys)
     #print("-+-+-+-+-+-")

     for col_data in csv_file1a:
          col_data = col_data.strip().split(",")
          csv1a_dict[header1a[0]].append(col_data[0])
          csv1a_dict[header1a[1]].append(col_data[1])

     print("-+-+-+-+-+-")
     print("The csv1a_dict output is:")
     print(csv1a_dict) #KEY NOTE the Collections Default Dict has transformed the KEY's ... "values" into a List ... since that's what I passed it to the function as.

     for i, (key,val) in enumerate(csv1a_dict.items()): #via => https://www.delftstack.com/howto/python/enumerate-dictionary-python/
          print("-+-+-+-+-+-")
          print("FOR LOOP - Enumerated to Insert a (IE: csv position) Index as Dict_Key:")
          print(i,key,val)
          print("-------")
          #NOTE ... I needed to break the index because the PRINTS BELOW also got produced twice.
     print("Test print of 'For Loops 'in' clause' to see if I can VAR it in next steps:")
     print(csv1a_dict.items()) #Actually now ... REMOVED Enumerate ... looks like the DICT is in Tuples ... locked in place for my analysis by the "key" (column header value) ... 
     print("-+-+-+-+-+-")

#Next read up on creating VARs for Calculation as 1> empty lists or 2> "=0"  to enable Module Analysis.
#Empty List ref => https://www.geeksforgeeks.org/python-read-csv-columns-into-list/
#Initialize 0 ref => https://realpython.com/python-enumerate/
#Summary of ASKS/CHallenge Requirements:
#1> (find/confirm) Total # of Months in DataSet
#2> (find/calculate) Net Total of Prof/Loss over entire period.
#3> Changes to Prof/Loss over the same. (?? - a little vague here).
#4> (calculate) Average rate of change over the same.
#5> (calculate/assess) greatest ("a Max??") ... increase in profits during that time period. Ask 1a> The date of the occurence. Ask1b> The amount of increase observed on said date.
#6> (calculate/assess) greatest DECREASE ("a Min??") ... in profits during that time period. Ask1a+1b > SEE ABOVE.
#7> PRINT Analysis when complete to the terminal and export to a ".txt" document/file.

#Convert csv DATE data into proper data type (via Dict key)...
from datetime import datetime as dt
#via URL1 => https://stackoverflow.com/questions/2265357/parse-date-string-and-change-format and URL2 => https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
#Code Approach via URL3 => https://stackoverflow.com/questions/36753868/python-convert-dictionary-of-string-times-to-date-times#:~:text=You%20can%20use%20a%20dictionary%20comprehension%3A%20new_dict%20%3D,val%20for%20key%2C%20val%20in%20alerts%20%5B%27alert_date%27%5D.items%20%28%29%7D

csv1a_DateFix = csv1a_dict['Date']
date_format_1a = "%b-%y"

#CANNOT DO BELOW ... because it's in a list ... using above to return to normal approach... 
#csv1a_DateFix = (csv1a_dict['Date'] == dt.strptime(csv1a_dict['Date'], date_format_1a).date())  #via => https://www.tutorialspoint.com/How-to-print-all-the-values-of-a-dictionary-in-Python & https://www.tutorialspoint.com/accessing-values-of-dictionary-in-python

#csv1a_DateList = list(csv1a_DateFix.values()) #KEY NOTE ... the output above is already in a list ... likely from out Collcections.DefaultDict(List) code above ... 
print("-------")
print("Test 1 ... validate DateFix VAR has correct KEY:")
print(csv1a_DateFix)
print("-+-+-+-+-+-")
#For Loop to correct date format. via => URL3 above (using url4 approach below)

cleaned_date_list = []

for date1a in csv1a_DateFix:
     if date1a != None: #via => https://pytutorial.com/check-if-variable-is-not-null-in-python/?expand_article=1
          cleaned_date_list.append(dt.strptime(date1a, date_format_1a).date())

print(cleaned_date_list)
print("----")
print(f"The Earliest Date within the Dataset is: {min(cleaned_date_list)}") #{min(csv1a_DateFix)}"
print(f"The Total Months within the Dataset is: {len(cleaned_date_list)}") # {len(csv1a_DateFix)}")
print(f"The Lastest Date within the Dataset is: {max(cleaned_date_list)}") # {max(csv1a_DateFix)}") 





###BELOW IS WRONG ... because of PYTHON's Native "datetime.datetime" object is not iterable ... 
#via url4 => https://stackoverflow.com/questions/59110236/how-to-solve-datetime-datetime-object-is-not-iterable-typeerror
#+
#+=> WE CANNOT simply iterate over the dates via the For Loop... we "must" ... create the list of dates within a list ... 

#x1#for date1a in csv1a_DateFix:
     #convert from string to datetime
     #and only request for the date portion of the datetime data format.
#x1#     date1a = dt.strptime(date1a, date_format_1a).date() #Format code via => https://www.geeksforgeeks.org/python-datetime-strptime-function/
#x1#     print(date1a)
#x1#     print("----")
#x1#     print(f"The Earliest Date within the Dataset is: {min(list(date1a))}") #{min(csv1a_DateFix)}"
#x1#     print(f"The Total Months within the Dataset is: {len(list(date1a))}") # {len(csv1a_DateFix)}")
#x1#     print(f"The Lastest Date within the Dataset is: {max(list(date1a))}") # {max(csv1a_DateFix)}") 
      #via => https://theprogrammingexpert.com/count-number-of-keys-in-dictionary-python/
#     print(f"The Total Months within the Dataset is: {len(date)}") #NOT WORKING ... cannot be run simply and with list() it returns not ... operable (or something) ....
#x1#     print("-+-+-+-+-+-")
#Print Separately to produce one list.     
#print("-------")
#print("Test 2 ... Verify Output as List:")
#print(date_cleaned)
#print("-+-+-+-+-+-")


#Initialize Variables for Module 3 Assignment Asks. Loops to provide "+1s" into these as "containers" (conceptually. etc. etc.) ..

