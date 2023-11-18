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


##KEY NOTE ... we're "recreating" (re-aligning/transforming ... the "data" to a "counter" ...)
#The "true" ... working data from this loop is the ... total_votes VAR ... and candidate list being "appended" by the For_Loop ... 
#My data would become ... > "vote 1" = "Robert Munch" ... "vote 2" = "XYZ" ... etc. etc ... as a list ... 
          
          #create VAR ... to separate from the "Loop_Placeholder" ... (unsure "why" ... but tagging it in seems redundant / can only provide additional confusion ... )
          max_votes_dict = {}
          
          for casted_vote in Candidates:
               if casted_vote in max_votes_dict:
                    max_votes_dict[casted_vote] += 1
               else:
                    max_votes_dict[casted_vote] = 1

          #Establish the VAR to be a placeholder on the max_votes_dict ... 
               winning_candidate = ""
               winner_vote_total = 0
          
               for vote_row in max_votes_dict:
                    confirmed_vote = max_votes_dict[vote_row]
                    #confirmed_vote_percent = round ((vote_row / total_votes) * 100, 2)
               
               #POTENTIAL code insert for printing to console/file ...

               #confirm the Tracking VARs to represent their naming conventions ... (IE: apply consistency in the logic ...  to find the "winner" ... for real ...  )
               if confirmed_vote > winner_vote_total:
                    winner_vote_total = confirmed_vote
                    winning_candidate = vote_row

#Append Records_forAnalysis DICT to a List for List Comprehension filters (+Panda's DF conversion in future modules.)
          Loop_PlaceHolder.append(Records_forAnalysis)
          ##USE CASES for Ask:
          ##5## Enables Looped Data to be accessible via List_Comp + Panda's for future modules ... 

#Print to console to validate observations. ##TOO MANY ROWS in this csv_reader!#
#print(Loop_PlaceHolder)
print("+-+-+-+")

#for prev , curr in [d[header1a[2]] for d in Loop_PlaceHolder if d[header1a[2][:]] != d[header1a[2][1:]]]

total_votes_2 = max(d["Row_ID"] for d in Loop_PlaceHolder)
print(f"The total votes casted via the Maximum Number of Rows Read from CSV is: \n{total_votes}")
print("\nConsider This as maximum amount of submissions ... via the .csv import's 'unique ID' ... ")
#print(f"Test for len of Row_ID:\n{len(total_votes)}") CANNOT WORK ... because it's an "int" ... likely only acheivable on the "set".
total_votes_test2 = max(i[Vote_Counted] for i in Loop_PlaceHolder) #NOTE ... prefered "d" above for "pythonic" ... confirmation I placed them in "dicts" ... however ... within the "dict" ... are actually "items" ... for what the technical ask is ... (IE: it's "a push decision" ... but need to be aware of the differences in the future ... when "I come back to this code .... in 6+months or ... 2+years ... etc. etc.")
print(f"The MAXIMUM amount of votes rec'd by ANY Candidate is: \n{total_votes_test2}")
#
#PARKING BELOW (unparked via url below) ... for a future "bp" ... there's got to be a way to simply "fetch" ... a value from the corresponding "key" .... by index or something ... 
#(NOTE: above ... is my parking "bp" ... I just need to "ideate" and "document" ... which is what I previously called "brainstorming" ... too generally ... So what the bp is ... is that ... I "know I'm stuck here...." ... I just need to "leave bread crumbs" ... for the future solution ... which is ... unknown ... but I had not "imagined" ... that the index could potentially be the "anchor point" ... for my google/stackoverflow/medium reference searching ...  )
#unparked url1 => https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
#unparked url1a => https://stackoverflow.com/questions/18552001/accessing-dict-keys-element-by-index-in-python3
#unparked url1b => https://stackoverflow.com/questions/6521892/how-to-access-a-dictionary-key-value-present-inside-a-list
#moving on "after first try ... future fix will be pending in that "failed out" scenario ... 

#uparked_url1a = #next(iter()) - via 1a ... 
#1b suggests FROM this .... i[Vote_Counted] for i in Loop_PlaceHolder)  .... DO this => 
#WHICH ... leads "me to the solution of" ... i[Candidates] for i in Loop_PlaceHolder if i[Vote_Counted] = total_votes_test2
     #url1a_test1 = list(Loop_PlaceHolder)
     #
     #BELOW DIDN'T WORK ... It printed ... not just the "titles of the dict keys ... "
     #
     #print(f"url1a suggested solution to list Keys is: {url1a_test1}")
## ... REMOVED FOR TEST RUN ... ##winner_url1a = [i[Candidates] for i in Loop_PlaceHolder if i[Vote_Counted] == total_votes_test2]
#print(f"That Candidate was: \n {winner_url1a}")
#
print(f"They rec'd {float((total_votes_test2/total_votes)*100)} % of the vote_total.\nWhich is {total_votes_test2} divided by {total_votes} x100.")
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
