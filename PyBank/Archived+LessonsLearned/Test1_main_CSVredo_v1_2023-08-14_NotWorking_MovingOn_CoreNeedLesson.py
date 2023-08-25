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
#1#+++++ SPACER ...
#NEW BP for Loading CSV as Dict via URL => https://stackoverflow.com/questions/21566437/iterating-through-dictreader

with open(file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a: #with open("myfile.csv") as f:
     #restval = blank columns = - /// restkey = extra columns +
     csv1a_dict = csv.DictReader(csv_file1a, fieldnames=None, restkey='+', restval='-', delimiter=',', quotechar='"')     
     csv1a_data = list(csv1a_dict)
     print(csv1a_data)
     print(type(csv1a_data))

     for rowA1 in csv1a_data:
         for key,val in rowA1.items():
              print(key)
              print(val)
         
         # print(rowA1['Date'],['Profit/Losses'])
         #print(readerA)
        #print(rowA1)

#via URL => https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python?noredirect=1&lq=1
#PRINT csv1a_dict for VALIDATION.
#z#=> DIDN'T WORK as expected ... #print(*rowA1.items(), sep='\n')

#SORT approach 1 ... #via URL => https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python?noredirect=1&lq=1
import collections
for k,v in collections.OrderedDict(sorted(list(csv1a_data).items())).items:
     print(k,v)

#via URL => https://www.delftstack.com/howto/python/how-to-sort-a-dictionary-by-value/
#CREATE OrderedDict of Imported CSV Values.