#Import Dependencies for loading Started Data/Code.
import csv
import os

# Change directory to the directory of current python script. via URL => https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
#
abs_path = os.path.abspath(__file__)
print(abs_path)
dir_name = os.path.dirname(abs_path)
print(dir_name)
print("-----")
os.chdir(dir_name)

#Confirm actual Current Directory for Building out Path.
validated_current_dir = os.getcwd()

#Validate location of current_dir in relation to Resources "Source Data" files.
print(f"The .py script's current location is:\n{validated_current_dir}")
print("-+-+-+-+-+-")

#Create VARs for File Paths for code simplicity.
source1_csv_name = "election_data.csv" #Title of File for Fetch.
     #via Module 3 => The dataset is composed of two columns: "Date" and "Profit/Losses".

#Create VAR for Output File Name.
output1_file_name = "Candidates_Analysis_PyPoll.txt"

#Use OS module to Fetch CSV data and read Source Data into Python for manipulation.

input_file_path1 = os.path.join("Resources",source1_csv_name) 
     #persNOTE: I'm not in an "Unsolved" folder like in class. So no ".." should be necessary.

#file_path2 = os.path.join("..","Resources",source1_csv_name) 
     #persNOTE: this is for when I work from the "archived+lessonslearned" folder.
print(input_file_path1)
#print("-------")
#print(file_path2)
print("-+-+-+-+-+-")

#Opening and reading the .csv file.
with open(input_file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1:
     csv_reader = csv.reader(csv_file1,delimiter=",")  #persNOTE: ALTERNATIVE path ... for being in "Archived+LessonsLearned"
#Create Exploratory analysis for the Header Row to assess the .csv file width (IE: how many raw_sourcedata_columns)
     header1a = next(csv_file1).strip().split(",")
     csv1a_width = len(header1a)
     print(f"Test - Data Check - CSV reader headers are: {header1a}") #PRODUCES a list ... which can be a VAR[0] or VAR[1] to leverage ... 
     print(f"The width of the CSV is : {csv1a_width}") #via => https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
     print("+-------+")

#Initialize Variables to extract from the source file data to enable the module 3 outcomes/calculations.
     Loop_PlaceHolder = [] #List to Append Dict of each col as a "key".
     total_votes = 0

#Initialize python data fetching for each row in the .csv source data.
     for count , row_1a in enumerate(csv_reader,1):  #via URL => https://stackoverflow.com/questions/28973207/get-length-of-csv-file-without-ruining-reader
          Records_forAnalysis = {}
          
          num_rows = count #Note Enumerate is starting from "1" which ensures it's accuracy.
          Records_forAnalysis.update({"Row_ID":num_rows})
          ##USE CASES for Ask:
          ##_z1_## Data Maintenance/Traceability (functional ... for the "for loop").

#Capture Each Column in String to preserve original Data Source Info.
          Ballot_IDs = str(row_1a[0])
          Records_forAnalysis.update({str(header1a[0]):Ballot_IDs})
          ##USE CASES for Ask:
          ##_z2_## Data Maintenance/Traceability (non-functional ... for the "client data set" ... IE: it can have errors and we may need to validate that / provide the feedback to the client at "some point" ... ).

          County = str(row_1a[1])
          Records_forAnalysis.update({str(header1a[1]):County})
          ##USE CASES for Ask:
          ##_z3_## Data Maintenance (non-functional ... for the "client data set" ... IE: "future asks" ...  ).
          ##_z3_## CARDINALITY+Sanity Checks  - CODE Maintenance / Readability / Debugging+Testing .... IE: Enabling the same functions from the "known ask" ... on "candidates" ... to be ported over to "County" ... if ever "necessary" (IE: "client asks" ... can become robust ... and I wouldn't want to re-write the whole entire script ... when "data cascades" and "financial dimensions" ... are involved in the data set ...)

          Candidates = str(row_1a[2])
          Records_forAnalysis.update({str(header1a[2]):Candidates})
          ##USE CASES for Ask:
          ##1## Find "complete list" (unique??) of candidates who rec'd votes.
          ##2## Calculate % of votes each candidate won ... 
          ##4## Confirm the ELECTION WINNER ... based on the popular vote (IR: which candidate had the most total_votes "+1s") ...

     ## WAS previously ... missing this "counter" ... which made it difficult for me to use list_comp for the "winner" calculation ... 
     #Add 1 to each row observed to count the total months of data within the .csv. 
          total_votes += 1
          Vote_Counted = str("Each_VoteCounted")
          Records_forAnalysis.update({str(Vote_Counted):total_votes})
          ##USE CASES for Ask:
          ##2## Calculate % of votes each candidate won ...
          ##3## Provide SUM of total_votes associated to each CANDIDATE "won" ...
          ##4## Confirm the ELECTION WINNER ... based on the popular vote (IR: which candidate had the most total_votes "+1s") ...

#START FROM SCRATCH BELOW ... 2023-10-28 10:50am ... 

