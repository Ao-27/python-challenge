#Import Dependencies for loading Started Data/Code.
import os
import csv

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
for count,row_1a in enumerate(csv_reader,1):  #via URL => https://stackoverflow.com/questions/28973207/get-length-of-csv-file-without-ruining-reader
     Records_forAnalysis = {}
     num_rows = count #Note Enumerate is starting from "1" which ensures it's accuracy.
     Records_forAnalysis.update({"Row_ID":num_rows})

#Capture Each Column in String to preserve original Data Source Info.
     Ballot_IDs = str(row_1a[0])
     Records_forAnalysis.update({str(header1a[0]):Ballot_IDs})

     County = str(row_1a[1])
     Records_forAnalysis.update({str(header1a[1]):Ballot_IDs})

     Candidates = str(row_1a[2])
     Records_forAnalysis.update({str(header1a[2]):Ballot_IDs})

#Use iteration to capture Counts and Calculations for PyPoll Analysis (as per Module #3 "client ask").

##Find "total votes" casted.
#     if Ballot_IDs[:] != Ballot_IDs[:]:  #NEEDS CORRECTION ... find from lessons learned in PyBank script.
#          total_votes =+ 1
#          Records_forAnalysis.update({str("Total_Votes_Accumulated"):float(total_votes)})
          #"if current row 'value' = prior row 'value' .."
##NOTE MUST APPEND ... SEE PYBANK EXAMPLE REF ... 
#     else:
#          total_votes = total_votes
#          Records_forAnalysis.update({str("Total_Votes_Accumulated"):float(total_votes)})
##NOTE must append ... see pybank example ref ...
          #Above is to keep the count "the same" as prior to seeing the "new row" ... above concept is to do "if current row 'value' = prior row 'value' .."

##Find "complete list" (unique??) of candidates who rec'd votes.

##Calculate % of votes each candidate won ... 

##Provide SUM of total_votes associated to each CANDIDATE "won" ...

##Confirm the ELECTION WINNER ... based on the popular vote (IR: which candidate had the most total_votes "+1s") ...


#Append Records_forAnalysis DICT to a List for List Comprehension filters (+Panda's DF conversion in future modules.)
     Loop_PlaceHolder.append(Records_forAnalysis)

#Print to console to validate observations.
print(Loop_PlaceHolder)
print("+-+-+-+")



#
     ##BALLOT_IDS ... PREV TO CURR ... COMPLEX LOGIC BELOW .... !!FUTURE REVIEW!!
#
# Calculation_RollTotal_Tuple = [(d["Row_ID"],d["Net_Profit_Loss_RollingTotal"]) for d in Loop_PlaceHolder] 

#Calculation_Date_Tuple = [(d["Row_ID"],d[header1a[0]]) for d in Loop_PlaceHolder]

#print(Calculation_RollTotal_Tuple) #WORKs ... 
#print(Calculation_Date_Tuple) #WORKs ... 
#print("+-+-+-+")

#Calc_Range = int(len(Calculation_RollTotal_Tuple))
#print(Calc_Range)
#print("+-+-+-+")

     #via URL => https://stackoverflow.com/questions/323750/how-to-access-the-previous-next-element-in-a-for-loop/324273#324273

     #Prev_Curr_Nxt_RollTotal_v1 = [None,*Loop_PlaceHolder,None]
#Prev_Curr_Nxt_RollTotal_v2 = [str(0), Calculation_RollTotal_Tuple]     #TRYING TO AVOID "none type error"   #[None,*Calculation_RollTotal_Tuple] # ,None]
     #print(Prev_Curr_Nxt_RollTotal_v1) #v1 UNSUCCESSFUL based on the values still being a "List of Dicts" ... I need to "extract out" ... first from the List of Dicts ... for the solution proposed in the URL...
#print(Prev_Curr_Nxt_RollTotal_v2)

#print("--------")
#for prev,curr in zip(Prev_Curr_Nxt_RollTotal_v2, Prev_Curr_Nxt_RollTotal_v2[1:]):
#     changed_difference = {}
#     monthly_change = 0
#     if int(prev[0]) > 1: #None: using NONE ... creates an error ... 