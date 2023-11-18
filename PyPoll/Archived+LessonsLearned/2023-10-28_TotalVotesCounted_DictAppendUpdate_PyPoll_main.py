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

#Capture Each Column in String to preserve original Data Source Info.
          Ballot_IDs = str(row_1a[0])
          Records_forAnalysis.update({str(header1a[0]):Ballot_IDs})

          County = str(row_1a[1])
          Records_forAnalysis.update({str(header1a[1]):County})

          Candidates = str(row_1a[2])
          Records_forAnalysis.update({str(header1a[2]):Candidates})

     ## WAS previously ... missing this "counter" ... which made it difficult for me to use list_comp for the "winner" calculation ... 
     #Add 1 to each row observed to count the total months of data within the .csv. 
          total_votes += 1
          Vote_Counted = str("Each_VoteCounted")
          Records_forAnalysis.update({str(Vote_Counted):total_votes})

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

#Print to console to validate observations. ##TOO MANY ROWS in this csv_reader!#
#print(Loop_PlaceHolder)
print("+-+-+-+")

#for prev , curr in [d[header1a[2]] for d in Loop_PlaceHolder if d[header1a[2][:]] != d[header1a[2][1:]]]

total_votes = max(d["Row_ID"] for d in Loop_PlaceHolder)
print(f"The total votes casted via the Maximum Number of Rows Read from CSV is: \n{total_votes}")
print("\nConsider This as maximum amount of submissions ... via the .csv import's 'unique ID' ... ")
#print(f"Test for len of Row_ID:\n{len(total_votes)}") CANNOT WORK ... because it's an "int" ... likely only acheivable on the "set".
print("+-+-+-+")

#ALMOST# Candidates_List = [d[header1a[2]] for d in Loop_PlaceHolder if row_1a[2][:] == row_1a[2][1:]]

Candidates_List = [d["Candidate"] for d in Loop_PlaceHolder]     ###  if d["Candidate"][:] != d["Candidate"][1:]] #WON't WORK ... basically I'm saying only do this on the "first to second row" .... then bring me everything ELSE ... which isn't the goal here ... 

#for prev , curr in zip(d[header1a[2][:]],d[header1a[2][1:]]):

#UNIQUE ONLY via URL => https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python

print(f"The number of Total Votes via Candidate_list is:\n{len(Candidates_List)}")

Unique_Candiates_Set = set(Candidates_List)
#print(f"The number of Total Votes via Set list is:\n{len(Unique_Candiates_Set)}") # SORRY ... this is only "3" as per the URL above ...
Unique_Candidates_List = (list(Unique_Candiates_Set))
print(f"The unique elements of the input list using set():\n{Unique_Candidates_List}")
print(f"The number of Candiates receiving votes is:\n{len(Unique_Candidates_List)}")
print(f"\n-+-+-+-+-")

#Create VARs to tally votes by each observation in Candidates_List:
Votes_Placeholder = []
Candidate_1_Votes = 0
Candidate_2_Votes = 0
Candidate_3_Votes = 0

for candidate in Candidates_List:
     Dict_key1 = str("Candidate")
     Dict_key2 = str("Total_Votes")
     Dict_key3 = str("Percent_of_Total_Votes")
     Candidate_1_Dict = {}
     Candidate_2_Dict = {}
     Candidate_3_Dict = {}

     Candidate_Votes_Max = {{str(Unique_Candidates_List[0]):Candidate_1_Dict},{str(Unique_Candidates_List[1]):Candidate_2_Dict}, {str(Unique_Candidates_List[2]):Candidate_3_Dict}} #{"Candidates_Votes_Looped":{{Dict_key1:[]},{Dict_key2:[]},{Dict_key3:[]}}}}
     #I'm getting the feeling that what I have to do ... is structure the Dict for each Candidate Name .... so .... 
     #{
          #str(Unique_Candidates_List[0]):
          #{

          #}
     # }
     if candidate == Unique_Candidates_List[0]:
          #Candidate_1_Dict = {}
          Candidate_1_Votes += 1
          #for votes in Candidate_1_Votes:
          #Candidate_Votes_Max.update({"Candidate_1_Max":Candidate_1_Votes})
          Candidate_1_Dict.update({Dict_key1:Unique_Candidates_List[0]})
          Candidate_1_Dict.update({Dict_key2:Candidate_1_Votes})
          Candidate_1_Dict.update({Dict_key3: round((Candidate_1_Votes / total_votes) * 100,2)})
          Candidate_Votes_Max.update({str(Unique_Candidates_List[0]):Candidate_1_Dict})    
     #Candidate_Votes.update({str(Unique_Candidates_List[0]):Candidate_1_Votes})
     if candidate == Unique_Candidates_List[1]:
          #Candidate_2_Dict = {}
          Candidate_2_Votes += 1
          #for votes in Candidate_2_Votes:
          #Candidate_Votes_Max.update({"Candidate_2_Max":Candidate_2_Votes})
          Candidate_2_Dict.update({Dict_key1:Unique_Candidates_List[1]})
          Candidate_2_Dict.update({Dict_key2:Candidate_2_Votes})
          Candidate_2_Dict.update({Dict_key3: round((Candidate_2_Votes / total_votes) * 100,2)})
          Candidate_Votes_Max.update({str(Unique_Candidates_List[1]):Candidate_2_Dict})         
     #Candidate_Votes.update({str(Unique_Candidates_List[1]):Candidate_2_Votes})
     if candidate == Unique_Candidates_List[2]:
          #Candidate_3_Dict = {}
          Candidate_3_Votes += 1
          #for votes in Candidate_3_Votes:
          #Candidate_Votes_Max.update({"Candidate_3_Max":Candidate_3_Votes})
          Candidate_3_Dict.update({Dict_key1:Unique_Candidates_List[2]})
          Candidate_3_Dict.update({Dict_key2:Candidate_3_Votes})
          Candidate_3_Dict.update({Dict_key3: round((Candidate_3_Votes / total_votes) * 100,2)})
          Candidate_Votes_Max.update({str(Unique_Candidates_List[2]):Candidate_3_Dict})      
     #Candidate_Votes.update({str(Unique_Candidates_List[2]):Candidate_3_Votes})
     Votes_Placeholder.append(Candidate_Votes_Max)

#Print Max Votes: WAY TOO LONG NOW ... but I can use List Comp on this Votes_Placeholder ... 
#print(Votes_Placeholder)
print(Candidate_Votes_Max)
print("+-+-+-+")

#Confirm Percentages for each Candidate: NOTE => in future I wil use a loop/append to list to enable List Comprehension to calculate for all at once.
Candidate_1_Percentage = round((Candidate_1_Votes / total_votes) * 100,2)
Candidate_2_Percentage = round((Candidate_2_Votes / total_votes) * 100,2)
Candidate_3_Percentage = round((Candidate_3_Votes / total_votes) * 100,2)

print(f"Candidate {Unique_Candidates_List[0]}\nTotaled {Candidate_1_Votes} votes and had {Candidate_1_Percentage} percent of the total votes.")
print(f"Candidate {Unique_Candidates_List[1]}\nTotaled {Candidate_2_Votes} votes and had {Candidate_2_Percentage} percent of the total votes.")
print(f"Candidate {Unique_Candidates_List[2]}\nTotaled {Candidate_3_Votes} votes and had {Candidate_3_Percentage} percent of the total votes.")