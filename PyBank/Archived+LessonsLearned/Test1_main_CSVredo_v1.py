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

#VIA URL => NEW POTENTIAL BP the "Tania" respons ...  => https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file
#with open('myfile.csv') as csvfile:

#    rest = []
#    with open("myfile.csv", "rb") as f:
#        reader = csv.reader(f)
#        i = reader.next()
#        i=i[1:]
#        re=csv.DictReader(csvfile)
#        for row in re:
#            for x in i:
#                print row[x]
#SPACER +++++ 
#VIA URL => https://docs.python.org/3/library/csv.html#csv.DictReader
#Try 2 using csv.DictWriter
#1#+++++ SPACER ...
#NEW BP for Loading CSV as Dict via URL => https://stackoverflow.com/questions/21566437/iterating-through-dictreader

with open(file_path1, 'r',encoding='utf-8-sig') as csv_file1a: #,newline='') as csv_file1a: #with open("myfile.csv") as f:
     #restval = blank columns = - /// restkey = extra columns +
     csv1a_header = csv_file1a.readline()   #TRY 2 via URL NYCeyes comment => https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file   #next(csv.reader(csv_file1a)) # Via URL => https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file
     print("Test - csv reader headers are:")
     print(csv1a_header)
     print("-------")
     #csv1a_header_list = csv1a_header.split(',')
     #print("Test2 - Col Names Listed are:")
     #print(csv1a_header_list)
     #print("-------")
     csv1a_dictread = csv.DictReader(csv_file1a) #, fieldnames=) #, fieldnames=None, restkey='+', restval='-', delimiter=',', quotechar='"')   
     csv1a_dictheader = csv1a_dictread.fieldnames  #Solution via URL => https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file ....  #next(csv1a_dict) #NOTE: this was via class from Carlos as a "lift+shift"...
     print("The csv1a_dict output is:")
     print(csv1a_dictread)
#START FROM HERE .... MOVING ON TO "VAR DEV" => https://stackoverflow.com/questions/29432912/convert-a-csv-dictreader-object-to-a-list-of-dictionaries
     print("-+-+-+-+-+-")
     print("The header row of the CSV file contains:")
     print(csv1a_dictheader) #Produces List. See URL for eventual Manipulation Needs => https://www.thegeekstuff.com/2013/06/python-list/?utm_source=feedly
     print("-------")
     #csv1a_header_index = 
     csv1a_data = list(csv1a_dictread)
     print("The list of dictionaries is:") # Via URL => https://www.pythonforbeginners.com/basics/read-csv-into-list-of-dictionaries-in-python
     print(csv1a_data)
     print(type(csv1a_data))
#SEEMS 100% good to here .... 
     print("-------")
     csv1a_data_items = csv1a_data.items()
     print("The data listed as Items is:")
     print(csv1a_data_items)
     print(type(csv1a_data_items))
     print("-+-+-+-+-+-")
#ABOVE = NEW TRY from =>  https://stackoverflow.com/questions/32238196/how-does-the-key-argument-in-pythons-sorted-function-work 
     for rowA1 in csv1a_data:
         for key,val in rowA1.items():
              print(key)
              print("+++")
              print(val)
              print("===")
     for keys in dict(csv1a_data).keys():
          print("The Keys in the Dictionary are:")
          print(keys)
          print("+++")
          print("The sorted keys are:")
          print(sorted(csv1a_data))
         
#via URL => https://www.delftstack.com/howto/python/how-to-sort-a-dictionary-by-value/
#CREATE OrderedDict of Imported CSV Values.


#BELOW will be deleted ... it's now added above ... 
#csv1a_SortedKeys = list(key) #sorted(key)
#print(csv1a_SortedKeys)
#print(type(csv1a_SortedKeys))

#csv1a_SortedValues = sorted(list(val)) #sorted(key)
#print(csv1a_SortedValues)
#print(type(csv1a_SortedValues))
