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

#Initialize Variables for Module 3 Assignment Asks. Loops to provide "+1s" into these as "containers" (conceptually. etc. etc.) ..