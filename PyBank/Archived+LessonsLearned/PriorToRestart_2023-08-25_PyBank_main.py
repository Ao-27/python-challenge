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
     print(f"The width of the CSV is : {csv1a_width}") #via => https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
     print("-+-+-+-+-+-")
     header_dict_1a1 = dict(enumerate(list(header1a)))
     print("The Header Column Indexes as Keys Dictionary:")
     print(header_dict_1a1)
     print("-------")
     print("The Header Column as Keys Dictionary:") #via => DIDN'T work ... but via Medium somewhere.
     Dict1a_fromkeys = dict.fromkeys(list(header1a))
     print(Dict1a_fromkeys)
     print("-+-+-+-+-+-")
     for col_data in csv_file1a:
          col_data = col_data.strip().split(",")
          csv1a_dict[header1a[0]].append(col_data[0])
          csv1a_dict[header1a[1]].append(col_data[1])
print("-+-+-+-+-+-")
print("The Appended csv1a_dict output is:")
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
#1> (find/confirm) Total # of Months in DataSet - LINE 92
#2> (find/calculate) Net Total of Prof/Loss over entire period. - LINE ??
#3> Changes to Prof/Loss over the same. (?? - a little vague here). - LINE ??
#4> (calculate) Average rate of change over the same. - LINE ??
#5> (calculate/assess) greatest ("a Max??") ... increase in profits during that time period. 
     #Ask 1a> The date of the occurence. - LINE ??
     #Ask1b> The amount of increase observed on said date. - LINE ??
#6> (calculate/assess) greatest DECREASE ("a Min??") ... in profits during that time period. 
     #Ask1a+1b > SEE ABOVE. - LINE ??
#7> PRINT Analysis when complete to the terminal and export to a ".txt" document/file. - LINE ??

#Convert csv DATE data into proper data type (via Dict key)...
from datetime import datetime as dt

#via URL1 => https://stackoverflow.com/questions/2265357/parse-date-string-and-change-format and URL2 => https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
#Code Approach via URL3 => https://stackoverflow.com/questions/36753868/python-convert-dictionary-of-string-times-to-date-times#:~:text=You%20can%20use%20a%20dictionary%20comprehension%3A%20new_dict%20%3D,val%20for%20key%2C%20val%20in%20alerts%20%5B%27alert_date%27%5D.items%20%28%29%7D

csv1a_DateFix = csv1a_dict['Date']
date_format_1a = "%b-%y"
print("-------")
print("Test 1 ... validate DateFix VAR has correct KEY:")
print(csv1a_DateFix)
print("-+-+-+-+-+-")

#Establish For Loop to correct date format for Analysis.
cleaned_date_list = []
     #via => combination of URL3 above and URL4 => https://stackoverflow.com/questions/59110236/how-to-solve-datetime-datetime-object-is-not-iterable-typeerror 
for date1a in csv1a_DateFix:
     if date1a != None: #via => https://pytutorial.com/check-if-variable-is-not-null-in-python/?expand_article=1
          cleaned_date_list.append(dt.strptime(date1a, date_format_1a).date())

print(cleaned_date_list)
print("----")
print(f"The Earliest Date within the Dataset is: {min(cleaned_date_list)}")
print(f"The Total Months within the List Dataset is: {len(cleaned_date_list)}")
print(f"The Dict Key has {len(csv1a_DateFix)} within it's Dataset.")
#via => https://theprogrammingexpert.com/count-number-of-keys-in-dictionary-python/
print(f"The Lastest Date within the Dataset is: {max(cleaned_date_list)}")
print("-+-+-+-+-+-")

#Initialize Variables for Module 3 Assignment Asks. Loops to provide "+1s" into these as "containers" (conceptually. etc. etc.) ..
#1# Use FUNCTION URL => https://www.programiz.com/python-programming/function
#1# TO Calculate CLient "Asks" ... 
#1A# Use URL => https://www.programiz.com/python-programming/methods/dictionary/get
#1B# Use URL => https://tutorialdeep.com/knowhow/key-maximum-value-dictionary-python/

#Max
csv1a_FloatFix = csv1a_dict['Profit/Losses']
print("-------")
print("Test 1 ... validate FLoatFix VAR has correct KEY:")
print(csv1a_FloatFix)
print("-+-+-+-+-+-")

#Establish For Loop to enable Float Analysis. URL7 => https://stackoverflow.com/questions/50433794/how-to-convert-dict-value-to-a-float
##LESSON LEARNED for the List object error =>##  cleaned_ProfLoss_List = [float(row) for row in list(csv1a_FloatFix.values())]
#Key Note URL8 has cleanest piece of code for all of this approach I took URL8 => https://bytes.com/topic/python/answers/737202-converting-dictionary-value-string-float
cleaned_ProfLoss_List = [float(row) for row in csv1a_FloatFix]

##LESSON LEARNED =>## BELOW Errored in the result being duplicated using this URL7 above to go directly to list comp.
#for ProfLoss in csv1a_FloatFix:
#     for row in csv1a_FloatFix:
#          cleaned_ProfLoss_List.append(float(row))
#SPACER##
print("The list comprehension float fix result is:")
print (cleaned_ProfLoss_List)
print("----")
print(f"The Lowest Value within the Dataset is: {min(cleaned_ProfLoss_List)}") 
print(f"The rows within the List Dataset is: {len(cleaned_ProfLoss_List)}") # 
print(f"The Dict Key has {len(csv1a_FloatFix)} within it's Dataset.")
print(f"The Largest Value within the Dataset is: {max(cleaned_ProfLoss_List)}") 
print("-+-+-+-+-+-")

#prepare output file for client ask.
#URL9 => https://learnpython.com/blog/write-to-file-python/ #USE PATHLIB to write to file ... seems to be the "BP" ... shows how to find where you are ... then you can add "output" folder .. etc.
#URL10 => https://realpython.com/read-write-files-python/#tips-and-tricks

#BELOW VIA MARIA ... really clean approach to print out via f-strings ... 
#1#with open(output_file, 'w') as file:
#1#    file.write("Financial Analysis\n")
#1#    file.write("----------------------------\n")
#1#    file.write(f"Total Months: {total_months}\n")
#1#    file.write(f"Total: ${net_profit_losses}\n")
#1#    file.write(f"Average Change: ${average_change:.2f}\n")
#1#    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
#1#    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
#1#print("Analysis has been exported to financial_analysis.txt")
