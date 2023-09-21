     #Import Dependencies for loading Started Data/Code.
import os
import csv

     #Confirm actual Current Directory for Building out Path.
current_dir = os.getcwd()
     #Validate location of current_dir in relation to Resources "Source Data" files.
     #print("The .py script's current location is: ")
     #print(current_dir)
print(f"The .py script's current location is:\n{current_dir}")
print("-+-+-+-+-+-")

     #Create VARs for File Paths for code simplicity.
source1_csv_name = "budget_data.csv" #Title of File for Fetch.
          #via Module 3 => The dataset is composed of two columns: "Date" and "Profit/Losses".

     #Create VAR for Output File Name.
output1_file_name = "PyBank_Analysis.txt"

     #Use OS module to Fetch CSV data and read Source Data into Python for manipulation.
input_file_path1 = os.path.join("Resources",source1_csv_name) 
          #persNOTE: I'm not in an "Unsolved" folder like in class. So no ".." should be necessary.
file_path2 = os.path.join("..","Resources",source1_csv_name) 
          #persNOTE: this is for when I work from the "archived+lessonslearned" folder.
print(input_file_path1)
print("-------")
print(file_path2)
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
          #3-NEW# Create Function for that AVERAGE .... 
          #
          #3-NEW#_#FUNCTION BELOW:#
          #def average(list_of_numbers):
          #    length_of_List = len(list_of_numbers)
          #    total_from_listed_numbers = 0.0
          #    for index,number in enumerate(list_of_numbers,1):
          #         total += number
          #    return total / length
          #
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
     #with open(input_file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1a:
     #     csv_reader = csv.reader(csv_file1a,delimiter=",")

          #Create Exploratory analysis for the Header Row.
          #header1a = next(csv_file2).strip().split(",")
          #persNOTE: REGULAR Path Above .... commenting out for being in "Archived+LessonsLearned"
with open(file_path2, 'r',encoding='utf-8-sig',newline='') as csv_file2:
     csv_reader = csv.reader(csv_file2,delimiter=",")
          #persNOTE: ALTERNATIVE path ... for being in "Archived+LessonsLearned"

          #Create Exploratory analysis for the Header Row.
     header1a = next(csv_file2).strip().split(",")
     csv1a_width = len(header1a)
     print("Test - Data Check - CSV reader headers are:")
     print(header1a) #PRODUCES a list ... which can be a VAR[0] or VAR[1] to leverage ... 
     print(f"The width of the CSV is : {csv1a_width}") #via => https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
     print("+-------+")
          #csv1a_width => Produces an INT ... can be a "range" participant ... if lookling at "columns" ... However, I've "determined" (by feel + SQL exp ... not python exp) ... that I need this to be in a dict ... for the many different "functional questions" from Staff ... that I tend to work with (IE: high level + lacking tech literacy ... etc. etc.).
          
          

          #Return to csv_reader to prepare to fetch the data by passing through VARs as it iterates.
          #next(csv_reader) #Skip the Header Row while Iterating ...
     #REMOVED ABOVE .... b/c ... it may be pushing the code "down an extra row.." ...
     #PRIOR RUN .. confirmed the code produced ... as month 1 ... pro+loss of "-384534" ... The CSV has that as "row 3" ...
     #KEY OBSERVATION ... my first usage of "next" ... has functions applied to it ... PRODUCING the header analysis data ... we don't need to "skip anything again after that.." ... CORE NEED TO REMEMBER ..

     #URL of key "for loop to dict append to list" ... approach => https://stackoverflow.com/questions/10715965/create-a-pandas-dataframe-by-appending-one-row-at-a-time?noredirect=1&lq=1
     #
     #SUMMARY OF NOTES ABOVE ... to ensure alignment below.
     #
     #Note1> Don't use "next(csv_reader)" if I am producing the ColNames + File_Width VARs.
     #Note2> the "first usage of next" ... comment above suggests that csv_reader ... is being like a DF with "no names" ... and the TOP ROW to "csv_reader" ... is the indexes ... of 0,1,2,3,4.... etc. etc.
     #Note3> SAFE TO START ... once the "header VARs are considered for how to leverage them ... within the " 

     Loop_PlaceHolder = []
     total_row_months = 0 #initial 0 for iteration to capture observation through each row.
     net_rows_prof_loss = 0 #initialize 0 for iteration to capture observation through each row
     prior_rows_prof_loss = 0
     calc_prof_loss_change = []
     for count,row_1a in enumerate(csv_reader,1):  #via URL => https://stackoverflow.com/questions/28973207/get-length-of-csv-file-without-ruining-reader
          Records_forAnalysis = {}
          num_rows = count
          Records_forAnalysis.update({"Row_ID":num_rows})
          date_col = str(row_1a[0])
          Records_forAnalysis.update({str(header1a[0]):date_col})
          profit_loss_col = int(row_1a[1])
          Records_forAnalysis.update({str(header1a[1]):profit_loss_col})
          total_row_months += 1
          Records_forAnalysis.update({str("Total_Months_Calculated"):total_row_months})
          net_rows_prof_loss += profit_loss_col
          Records_forAnalysis.update({str("Net_Profit_Loss_RollingTotal"):net_rows_prof_loss})
     #          if total_row_months >1:
     #               calc_change = 
                    #START HERE the "If Statement Stuff" .... to Loop_OUT_KeyStep Below.


               #LOOP_OUT_KeyStep = "capture the difference here" ...
          Loop_PlaceHolder.append(Records_forAnalysis)
               #print(Records_forAnalysis)

     print(Loop_PlaceHolder)

     #FIX1 => Need to "capture the Keys from the Dict ... within VAR of header1a.."
     #FIX2 => Need to "adjust" the CSV WIDTH ... via NEW VAR ... (updated_width) ... of how many keys created by the (for loop ... via csv_reader) ...

     #HIGH LEVEL Ideations ... figure out how to use/access the Dict Keys ... apply the "if" statement below to them ... 


     #FIX-x1 => #Approach for "change" calculation  ... 
     #GOAL => To capture the "value" difference within the profit_loss column ... based on the prior row's (n-1 ...) .. "value" ... (when) .... "Row_ID" = (prior Row_ID) "n+1" ... 
          #0start => If Row_ID "not null" = True AND ... Row_ID = "0" (title row) ... not within the CSV data ... (key reminder for my processing...)
          #1start_nxt =>  if "Row_ID" key greater than 0 .... AND curr.Row_ID  MINUS prior.Row_ID = "1" ... AND (need to ensure it's ONLY on the specific row ... so if "change" = 0.00 ... )
          #THEN => Calculate and populate "change column ... "
          #ELIF (ELSE1) => 

     #Key URL for List Comp => https://stackoverflow.com/questions/22394783/how-to-access-dictionary-elements-in-a-list-in-python

     print("+-+-+-+")
     #print(Loop_PlaceHolder.items())  #ERROR NOTE => AttributeError: 'list' object has no attribute 'items'
     #

     #CREATING TUPLE first ... before Calc Loop ... of the Cols to participate in the "If Statement" ... 
     #via URL => https://stackoverflow.com/questions/17117912/how-to-access-the-values-in-a-list-of-dictionaries
     #

Calculation_RollTotal_Tuple = [(d["Row_ID"],d["Net_Profit_Loss_RollingTotal"]) for d in Loop_PlaceHolder] 

Calculation_Date_Tuple = [(d["Row_ID"],d[header1a[0]]) for d in Loop_PlaceHolder]

print(Calculation_RollTotal_Tuple) #WORKs ... 
print(Calculation_Date_Tuple) #WORKs ... 
print("+-+-+-+")

Calc_Range = int(len(Calculation_RollTotal_Tuple))
print(Calc_Range)
print("+-+-+-+")

     #via URL => https://stackoverflow.com/questions/323750/how-to-access-the-previous-next-element-in-a-for-loop/324273#324273

     #Prev_Curr_Nxt_RollTotal_v1 = [None,*Loop_PlaceHolder,None]
Prev_Curr_Nxt_RollTotal_v2 = [None,*Calculation_RollTotal_Tuple] # ,None]
     #print(Prev_Curr_Nxt_RollTotal_v1) #v1 UNSUCCESSFUL based on the values still being a "List of Dicts" ... I need to "extract out" ... first from the List of Dicts ... for the solution proposed in the URL...
print(Prev_Curr_Nxt_RollTotal_v2)

print("--------")
for prev,curr in zip(Prev_Curr_Nxt_RollTotal_v2, Prev_Curr_Nxt_RollTotal_v2[1:]):
     changed_difference = {}
     monthly_change = 0
     if prev[0] == None:
          monthly_change = int(monthly_change + 0)
          changed_difference.update({str("Net_Monthly_Change_RollingTotal"):monthly_change})
     if prev[0] != None and prev[1] > 0 and  curr[1] > 0:
          monthly_change = int(0 + prev[1] - curr[1])
          changed_difference.update({str("Net_Monthly_Change_RollingTotal"):monthly_change})
          #if prev[1] < 0 and curr[1] > 0:
          #if prev[0] != None and prev[1] > 0 and  curr[1] > 0:
          Loop_PlaceHolder.append(changed_difference)
               #print(Records_forAnalysis)

     print(Loop_PlaceHolder)
print("+-+-+-+")


#RUNNING the above just to "test the bad outcome ...  for my learning ... "
#
#KEY NOTE ....  I feel the need to use "ABS" ... and do a literal calculation ... I believe this is what we're supposed to AVOID ...
     #I'LL need to use the office hours or ask BCS ... to review the for loop functionality ... and what the nested loops are providing ... I cannot continue to "go it alone" .. 
                    
                    
                    
print("--------") #ABOVE WORKS ... but I don't truly understand "why" ... via the [1:] and [2:]

     #via URL => https://stackoverflow.com/questions/5434891/how-can-i-iterate-over-overlapping-current-next-pairs-of-values-from-a-list?noredirect=1&lq=1
     #NOTES in above URL ...  that the zip approach above is actually ... copying the list 3 times!!! once per prev, curr, nxt ... 

     #Via URL on Flattening a List => http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
     #First create Empty DICT .... Calculations_For_Analysis = {} .. 
     #2nd ... 

     #Via URL => https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
     # Given a list of lists l,
     #
     # flat_list = [item for sublist in l for item in sublist]
     #
     # which means:
     #
     # flat_list = []
     # for sublist in l:
     #    for item in sublist:
     #        flat_list.append(item)
     #
     # is faster than the shortcuts posted so far. (l is the list to flatten.)