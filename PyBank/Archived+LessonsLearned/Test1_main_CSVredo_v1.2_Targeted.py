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

with open(file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a: #,newline='') as csv_file1a: 
     unclean1a_header = csv_file1a.readline().split(",")   #TRY 2 via URL NYCeyes comment => https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file   #next(csv.reader(csv_file1a)) # Via URL => https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file
     csv_header_dict = {}
     for Hkey,Hvalue in enumerate(list(unclean1a_header)):
          

     
     print("Test - csv reader headers are:")
     print(unclean1a_header)
     print(csv1a_header)
     header_dict_1a1 = dict(enumerate(list(unclean1a_header)))

     print(header_dict_1a1)
     print("-------")
     csv1a_dictread = csv.DictReader(csv_file1a, delimiter=",") #, fieldnames=) #, fieldnames=None, restkey='+', restval='-', delimiter=',', quotechar='"')   
#ADD2#     for data_1a in map(dict,csv1a_dictread):
#add2#          print("The targeted v1.2 output is:")
#add2#          print(data_1a)
#add2#          print("+-------+")
    # csv1a_dictheader = csv1a_dictread.fieldnames  #Solution via URL => https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file ....  #next(csv1a_dict) #NOTE: this was via class from Carlos as a "lift+shift"...
     print("The csv1a_dict output is:")
     print(csv1a_dictread)

#START FROM HERE .... MOVING ON TO "VAR DEV" => https://stackoverflow.com/questions/29432912/convert-a-csv-dictreader-object-to-a-list-of-dictionaries
     print("-+-+-+-+-+-")
#add1#     csv1a_data = list(data_1a)   #EDIT TO TEST v1.2   # list(csv1a_dictread)
     print("The list of dictionaries is:") # Via URL => https://www.pythonforbeginners.com/basics/read-csv-into-list-of-dictionaries-in-python
#ADD1#     #print(csv1a_data)
#add1#     print(type(csv1a_data))
#SEEMS 100% good to here .... 
     print("-+-+-+-+-+-")
#ABOVE = NEW TRY from =>  https://stackoverflow.com/questions/32238196/how-does-the-key-argument-in-pythons-sorted-function-work 
#1     for rowA1 in csv1a_data:
#1         for key,val in rowA1.items():
#1              print(key)
#1              print("+++")
#1              print(val)
#1              print("===")
#1     for keys in dict(csv1a_data).keys():
#1          print("The Keys in the Dictionary are:")
#1          print(keys)
#1          print("+++")
#1          print("The sorted keys are:")
#1          print(sorted(csv1a_data))
         
#via URL => https://www.delftstack.com/howto/python/how-to-sort-a-dictionary-by-value/
#CREATE OrderedDict of Imported CSV Values.