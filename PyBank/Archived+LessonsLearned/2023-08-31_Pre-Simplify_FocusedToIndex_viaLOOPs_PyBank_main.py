#Import Dependencies for loading Started Data/Code.
import os
import csv

#Confirm actual Current Directory for Building out Path.
current_dir = os.getcwd()
#Validate location of current_dir in relation to Resources "Source Data" files.
print("The .py script's current location is: ")
print(current_dir)
print("-+-+-+-+-+-")

#Create VARs for File Paths for code simplicity.
source1_csv_name = "budget_data.csv" #Title of File for Fetch.
     #via Module 3 => The dataset is composed of two columns: "Date" and "Profit/Losses".

#Create VAR for Output File Name.
output1_file_name = "PyBank_Analysis.txt"

#Use OS module to Fetch CSV data and read Source Data into Python for manipulation.
input_file_path1 = os.path.join("Resources",source1_csv_name) 
     #persNOTE: I'm not in an "Unsolved" folder like in class. So no ".." should be necessary.
print(input_file_path1)
print("-+-+-+-+-+-")

#Use OS module to establish .txt output location for saving.
output_file_path1 = os.path.join("Analysis",output1_file_name)
print(output_file_path1)
print("-+-+-+-+-+-")

#Outcome/Result Set GOAL via Module 3:
     # Your task is to create a Python script that analyzes the records to calculate each of the following values:
     #1# The total number of months included in the dataset
     #2# The net total amount of "Profit/Losses" over the entire period
     #3# The changes in "Profit/Losses" over the entire period, and then the average of those changes
     #4# The greatest increase in profits (date and amount) over the entire period
     #5# The greatest decrease in profits (date and amount) over the entire period

#CSV fetch goal ... is to access the 2 columns and loop through to populate the data associated to asks #1 to #5 above.
     #1# Code Approach => Dictionary of the Dates Column + Count total values.
     #2# Code Approach => Dictionary of the Prof+Loss Column + Sum total values.
     #3# Greatest increase in profits (assumed to prior month) ... as (a) within the Prof+Loss column and (b) the date of occurence of said change within it's Date Column.
     #4# Greatest decrease in profits (assumed to prior month) ... as (a) within the Prof+Loss column and (b) the date of occurence of said change within it's Date Column.
     #5# PRINT the Analysis to a ".txt" file with the results.

Csv_Dates = {} # #1 above
Csv_ProfLoss = {} # #2 above

# Read CSV to fetch the data and provide to Dict for Counts+Sums.
with open(input_file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a:
     header1a = next(csv_file1a).strip().split(",")
     csv1a_width = len(header1a)
     print("Test - Data Check - CSV reader headers are:")
     print(header1a)
     print(f"The width of the CSV is : {csv1a_width}") #via => https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
     print("-+-+-+-+-+-")

#Append values to Csv_Dates DICT and Csv_ProfLoss DICT:
#via (+pers Trial and Error) => https://stackoverflow.com/questions/28283647/convert-csv-column-to-list

     for i,j in csv.DictReader(csv_file1a):
          print(dict(j)) #via => https://stackoverflow.com/questions/2387697/best-way-to-convert-csv-data-to-dict

     #for col_data in csv_file1a:
     #     col_data = col_data.strip().split(",")
     #     print(col_data)
     #          for k,val in col_data[0]:
     #          k = "Date"            
     print("-+-+-+-+-+-")
