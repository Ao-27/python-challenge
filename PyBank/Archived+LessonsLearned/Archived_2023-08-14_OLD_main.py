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
#1#with open(file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a: #with open("myfile.csv") as f:
    #csv1_headerA = [header.strip() for header in next(csv_file1a).split(",")[1:]]  #next(f).split(",")[1:]] #REPALCED with my own syntax for personal readability.
#1#     readerA = csv.DictReader(csv_file1a)     #WRONG_0starter => readerA = csv.DictReader(file_path1) #NOTE => This has to be "csv_file1a" ... 
     #dict_list_readerA = list(readerA) #dict(list(readerA)) #list(readerA)  #tuple(list(readerA)) #tuple() ADDED HERE for observation in => https://rollbar.com/blog/python-typeerror-unhashable-type-dict-exception/   #... HOWEVER ... note it "didn't enable what I wanted" ... 
     #print(dict_list_readerA)
#1#     for rowA1 in readerA:
         # print(rowA1['Date'],['Profit/Losses'])
         #print(readerA)
#1#         print(rowA1)

#1#+++++ SPACER ...
#NEW BP for Loading CSV as Dict via URL => https://stackoverflow.com/questions/21566437/iterating-through-dictreader

with open(file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a: #with open("myfile.csv") as f:
     #restval = blank columns = - /// restkey = extra columns +
     csv1a_dict = csv.DictReader(csv_file1a, fieldnames=None, restkey='+', restval='-', delimiter=',', quotechar='"')     
     csv1a_data = list(csv1a_dict)
     print(csv1a_data)
     print(type(csv1a_data))

     for rowA1 in readerA:
         # print(rowA1['Date'],['Profit/Losses'])
         #print(readerA)
         print(rowA1)

#via URL => https://www.delftstack.com/howto/python/how-to-sort-a-dictionary-by-value/
#CREATE OrderedDict of Imported CSV Values.

from collections import OrderedDict

file1a_datekey_sortedDict = OrderedDict(sorted(readerA.items(), key=lambda x: x[0])) #OrderedDict(sorted(exampleDict.items(), key=lambda x: x[1]))
file1a_ProfLossVAL_sortedDict = OrderedDict(sorted(readerA.items(), key=lambda x: x[1]))
print(file1a_datekey_sortedDict)
print(type(file1a_datekey_sortedDict))
print(file1a_ProfLossVAL_sortedDict)
print(type(file1a_ProfLossVAL_sortedDict))

# via URL => https://stackoverflow.com/questions/23190074/python-dictionary-error-attributeerror-list-object-has-no-attribute-keys
#CREATE Dict separately to CSV extract above ... 

#Create VARs for dict_list_ReaderA as Keys + Values
file1a_keys = dict([rowA1.keys()])
file1a_values =  dict([rowA1.values()]) #ADDED dict ... once seeing the type was "list" otherwise .
print(file1a_keys)
print(type(file1a_keys))
print(file1a_values)
print(type(file1a_values))

#via URL => https://www.freecodecamp.org/news/the-zip-function-in-python-explained-with-examples/
#ZIP_LONGEST to create a "dataset" that can participate within the FOR LOOP (see last example in URL for "context/in theory")

from itertools import zip_longest

file1a_zip_long = zip_longest(file1a_keys,file1a_values)   #RAW APPROACH to eval/debug above after here => zip_longest(list(rowA1.keys()),list(rowA1.values()))
print(type(file1a_zip_long))
print(list(file1a_zip_long))
#print(dict(file1a_zip_long)) #PRODUCED EMPTY DICT ... 

#Append/Create INDEX for the List of Dicts produced for the .csv.
#URLz1-Index to Dict => https://stackoverflow.com/questions/36395127/how-to-add-index-into-a-dict
#!! BELOW feels close ... but pivoting to add in concepts from URLz2 => https://stackoverflow.com/questions/23190074/python-dictionary-error-attributeerror-list-object-has-no-attribute-keys
#mydict = {}
#for idx, item in enumerate(file1a_values):
#     indexes = mydict.setdefault(item,[])      #([],item)# (item,[])
#     indexes.append(idx)
#print(mydict)

#+++++
#BELOW "is close but far away ... "
#csv_index_colname = 'Date' #See URL => https://stackoverflow.com/questions/23190074/python-dictionary-error-attributeerror-list-object-has-no-attribute-keys
#Analysis_dict1a = dict()
#for row in rowA1: #REPLACE "row" here with INDEX later on... after test ... 
#    Analysis_dict1a[row.pop(csv_index_colname)] = row
#print(Analysis_dict1a)
#print(type(Analysis_dict1a))
#+++++
#DIFFICULT TO FOLLOW BELOW ... but massive lessons learned when I "have the time" ... to decrompress below ... 
#
#Below via URL1-REF => https://stackoverflow.com/questions/36395127/how-to-add-index-into-a-dict
#URL0-newACTUAL => https://stackoverflow.com/questions/1747817/create-a-dictionary-with-comprehension

#URL-0 solution "looks good" as LESSON LEARNED ... but isn't exactly printing what I'd expect ... 
#dictnew_index_file1a = {index:file1a_values[index] for index in range(0,len(file1a_values))}
#print(dictnew_index_file1a)


#Initialize Variables for Module 3 Assignment Asks. Loops to provide "+1s" into these as "containers" (conceptually. etc. etc.) ..
total_months = 0
total_net_amount = 0
previous_profit_loss = 0
changes = [0]
greatest_increase = [' ', 0]
greatest_decrease = [' ', 0]