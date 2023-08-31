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
input_file_path1 = os.path.join("..","Resources",source1_csv_name) 
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

#replaced with Total_Months List as 0 #csv_Dates = {} # #1 above
#replace with net_profit_losses as 0 + monthly_changes as [] #Csv_ProfLoss = {} # #2 above
#Added greatest increase + decrease as 0.
#Added greatest_inc_mth and greatest_decrease_mth as  empty strings.
#VERY uncomfortable accepting above ... but with the understanding on how For Loops iterate ... I suppose the "best practice" ... is to focus the effort on cleaning to ... enable the iterator's dependence on "simple data" ... #

# Read CSV to fetch the data and provide to Dict for Counts+Sums.
with open(input_file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a:
     csv_reader = csv.reader(csv_file1a,delimiter=",")
     
     #Create Exploratory analysis for the Header Row.
     header1a = next(csv_reader).strip().split(",") #test4 ANSWER => See Error Below ... the file is not a "list" .. but csv_reader converts to list ... HENCE why the "simply use the index[0 or 1]" ... becomes the core functional need for the iterator ... (IE: for Loops).

     csv1a_width = len(header1a)
     print("Test - Data Check - CSV reader headers are:")
     print(header1a)
     print(f"The width of the CSV is : {csv1a_width}") #via => https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
     
     #Return to csv_reader to prepare to fetch the data by passing through VARs as it iterates.
     #next(csv_reader) #Skip the Header Row while Iterating ...
#REMOVED ABOVE .... b/c ... it may be pushing the code "down an extra row.." ...
#PRIOR RUN .. confirmed the code produced ... as month 1 ... pro+loss of "-384534" ... The CSV has that as "row 3" ...
#KEY OBSERVATION ... my first usage of "next" ... has functions applied to it ... PRODUCING the header analysis data ... we don't need to "skip anything again after that.." ... CORE NEED TO REMEMBER ..

     #Create VARs for the iterator to populate during For Loops.
     total_months_1a = 0
     net_prof_losses_1a  = 0
     Monthly_Changes_1a  = []
     greatest_increase_1a  = 0
     greatest_decrease_1a  = 0
     greatest_increase_date_1a  = ""
     greatest_decrease_date_1a  = ""         
     print("-+-+-+-+-+-")

     #Esblish the For Loops to iterate through each row in the data set to populate the VARs for future calculations.
     for row_1a in csv_reader:
          date_col = row_1a[0] # Index 0 for column 1
          profit_losses_col = int(row_1a[1]) #Index 1 for column 2 #NOTE ... have to wrap in INT ... to enable operator of "+=".
# prior_profit_losses_col = if a_total_months:
#      >1 row_1a
#NEED TO FIGURE OUT ABOVE ... #

          #Iterative calculations/counters for each row assessed by For Loop.
          total_months_1a +=1
          net_prof_losses_1a += profit_losses_col
          
          print("-----")
          print(f"The total_months contained within the CSV are : {total_months_1a}")
          print(f"The net_profit_loss contained within the CSV are : {net_prof_losses_1a}")

          #Monthly Changes Data Capture via Iteration:
#          if total_months_1a >1:
#               each_change = profit_losses_col - prior_profit_losses_col
print("-+-+-+-+-+-")
