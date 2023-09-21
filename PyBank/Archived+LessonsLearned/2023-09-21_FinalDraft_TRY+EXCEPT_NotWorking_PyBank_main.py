#Import Dependencies for loading Started Data/Code.
import os
import csv

# Change directory to the directory of current python script. via URL => https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
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
source1_csv_name = "budget_data.csv" #Title of File for Fetch.
     #via Module 3 => The dataset is composed of two columns: "Date" and "Profit/Losses".

#Create VAR for Output File Name.
output1_file_name = "Financial_Analysis_PyBank.txt"

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
     total_row_months = 0 #initial 0 for iteration to capture observation through each row. |#total_months += 1
     net_rowsum_prof_loss = 0 #initialize 0 for iteration to capture observation through each row. |#total_pl += int(first_row[1])
     curr_row_prof_loss = 0 #|#value = int(first_row[1])
     prior_row_prof_loss = 0 #|#change = int(row[1])-value
     calc_prof_loss_change = 0  #|# PERHAPS ... change this to a list ... and "append to it ... " ... 
     #Changes = {}
#Initialize python data fetching for each row in the .csv source data.
     for count,row_1a in enumerate(csv_reader,1):  #via URL => https://stackoverflow.com/questions/28973207/get-length-of-csv-file-without-ruining-reader
          Records_forAnalysis = {}

          num_rows = count #Note Enumerate is starting from "1" which ensures it's accuracy.
          Records_forAnalysis.update({"Row_ID":num_rows})

          date_col = str(row_1a[0])
          Records_forAnalysis.update({str(header1a[0]):date_col}) #Note ... if this was a list it would be the following => dates.append(row[0]) ... my code => date_col.append(str(header1a[0]))

#     #TEST2!! via total months ... to see if prior row prof+loss needs to be removed from INNER CODE ...
#          prior_row_total_month = 0 + total_row_months
#          Records_forAnalysis.update({str("Test1_Prior_Row_Months"):prior_row_total_month}) #Note ... if list ... => 
#
#ABOVE REMOVED ... but was a key "debug" tool for me ... 

     #STORE in Python Memory the prior rows "current prof+loss" ... to enable it to be overwritten.
          prior_row_prof_loss = float(curr_row_prof_loss)
          Records_forAnalysis.update({str("Prior_Row_Profit_Loss"):prior_row_prof_loss}) 

     #Add 1 to each row observed to count the total months of data within the .csv. 
          total_row_months += 1
          Records_forAnalysis.update({str("Total_Months_Calculated"):total_row_months})

     #Curr Row Profit loss ... to inner loop to enable prior_row to "See the result" ... 
          curr_row_prof_loss = 0 + int(row_1a[1])
     #Append curr_row ... to DICT for analysis afterwards.
          Records_forAnalysis.update({str(header1a[1]):curr_row_prof_loss})
          #Update profit loss variable ... to enable data storage to be the same for "all rows" ... (will return to clean up this comment...)     

     #Sum the current row's profit and loss to a rolling total.
          net_rowsum_prof_loss += float(curr_row_prof_loss)    #AS A TEST ... run this after the nested loop AND before ... to see if there are differing outcomes. 
          Records_forAnalysis.update({str("Net_Profit_Loss_RollingTotal"):net_rowsum_prof_loss}) #Note ... if list ... => 

          if (count == 1):
               #Records_forAnalysis.update({str("Prior_Row_Profit_Loss"):prior_row_prof_loss})
               calc_prof_loss_change = 0 + curr_row_prof_loss # prior_row_prof_loss #MIGHT want to ensure I set this as "0"..
               #Append Change as "null" ... or "0" ... for the calculations anchor point ... 
               Records_forAnalysis.update({str("ChangeOf_Value_Difference"):float(calc_prof_loss_change)}) 

          elif (count > 1):  # and prior_row_prof_loss!=0):   #prior_row_prof_loss!=0:             
               calc_prof_loss_change = curr_row_prof_loss - prior_row_prof_loss
#NOTE ... Variable name error ... I am not using the "changes dict"               #Changes.update({str("ChangeOf_Value_Difference"):calc_prof_loss_change}) 
               Records_forAnalysis.update({str("ChangeOf_Value_Difference"):float(calc_prof_loss_change)})

#APPEND the Dict to a List ... for eventual Panda's DF consumption + to enable easier column value fetching via key+value consistency.
          Loop_PlaceHolder.append(Records_forAnalysis)
#Print to console to validate observations.
     print(Loop_PlaceHolder)
     print("+-+-+-+")

Greatest_Increase =  max([d["ChangeOf_Value_Difference"] for d in Loop_PlaceHolder])    #max([[d["Date"],d["ChangeOf_Value_Difference"]] for d in Loop_PlaceHolder])
print(Greatest_Increase)
print("--------")
Greatest_Increase_Date =  [d["Date"] for d in Loop_PlaceHolder if d["ChangeOf_Value_Difference"] == Greatest_Increase]
print(Greatest_Increase_Date)
print("--------")
Greatest_Decrease =  min([d["ChangeOf_Value_Difference"] for d in Loop_PlaceHolder]) 
print(Greatest_Decrease)
print("--------")
Greatest_Decrease_Date =  [d["Date"] for d in Loop_PlaceHolder if d["ChangeOf_Value_Difference"] == Greatest_Decrease]
print(Greatest_Decrease_Date)
print("--------")
##CHECK MODULE on whether the "first row" ... should be allowed to participate within the average output ... 
#Average_Monthly_Change = sum([d["ChangeOf_Value_Difference"] for d in Loop_PlaceHolder]) / max([d["Total_Months_Calculated"] for d in Loop_PlaceHolder])
#print(Average_Monthly_Change)
#print("--------")
#
Max_Months = max([d["Total_Months_Calculated"] for d in Loop_PlaceHolder])
print(Max_Months)
print("--------")
Avg_Mthly_Chg_2ndRowOn = sum([d["ChangeOf_Value_Difference"] for d in Loop_PlaceHolder][1:]) / (Max_Months - 1)
print(round(Avg_Mthly_Chg_2ndRowOn,2)) #via URL => https://www.freecodecamp.org/news/how-to-round-to-2-decimal-places-in-python/
print("--------")
#DEFINITELY NOT THE AVG VIA ROLLING ... BUT STILL CHECK THE MODULE ...#
#DEBUG CHECK ... TAKE THE MAX AVERAGE ... AGAINST THE SUB OF THE "ROLLING TOTAL" ... to validate ... 
#
#Avg_viaRolling = sum([d["Net_Profit_Loss_RollingTotal"] for d in Loop_PlaceHolder][:]) / Max_Months
#print(Avg_viaRolling) #YEah ... this looks off ... will look into what the MODULE specifically asks for then ... 
#
#NOTE ... module 3 says the "average rate of change" ... over this time period ... I will provide 2 ... the one with "0" for month 1 ... and without "0" ... 
#
#CHECK URL => https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_row_months)}")
print(f"Total: ${net_rowsum_prof_loss:.0f}")
print(f"Average Change: ${Avg_Mthly_Chg_2ndRowOn:.2f}") #Note Convert to STR not necessary since using fstring syntax. Via URL => https://docs.python.org/3/library/string.html#formatspec
print(f"Greatest Increase in Profits: {str(Greatest_Increase_Date[0])} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {str(Greatest_Decrease_Date[0])} (${Greatest_Decrease})")

# Export the analysis to a text file

with open(output1_file_name, 'w') as file: #Using Output Name assigned above. Approach via URL => https://www.freecodecamp.org/news/python-write-to-file-open-read-append-and-other-file-handling-functions-explained/
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {str(total_row_months)}\n")
    file.write(f"Total: ${net_rowsum_prof_loss:.0f}\n")
    file.write(f"Average Change: ${Avg_Mthly_Chg_2ndRowOn:.2f}\n") #Note Convert to STR not necessary since using fstring syntax. Via URL => https://docs.python.org/3/library/string.html#formatspec
    file.write(f"Greatest Increase in Profits: {str(Greatest_Increase_Date[0])} (${Greatest_Increase})\n")
    file.write(f"Greatest Decrease in Profits: {str(Greatest_Decrease_Date[0])} (${Greatest_Decrease})\n")
    file.close()

print(f"Analysis file has been created as:{output1_file_name}")
print("-+-+-+-+-+-")
#Move create file to "Analysis" folder directory. via URL => https://datatofish.com/move-file-python/ & https://pynative.com/python-move-files/ & https://www.techbeamers.com/string-concatenation-in-python/
import shutil

#List file being processed in the move. via URL => https://www.geeksforgeeks.org/python-move-and-overwrite-files-and-folders/
print(f"Before Moving File - open + write created file in: {dir_name}")  #NOTE: this is "path" ... in G for Geeks URL.
print(f"Validated by finding the output file name of {output1_file_name}. \nWithin the files in the dir_name folder: {os.listdir(validated_current_dir)}") 
print("-+-+-+-+-+-")

#Use OS module to establish .txt output location for saving.
output_file_path1 = os.path.join("Analysis")   #,output1_file_name)    #NOTE this is "destination" ... in G for Geeks URL.
print(output_file_path1)
print("-+-+-+-+-+-")

#Create VARs to Enable Shutil Module's next steps. #Raw Strings via URL => https://www.codevscolor.com/python-raw-string
#Note ... https://www.geeksforgeeks.org/python-move-and-overwrite-files-and-folders/ ... suggests that I DO NOT need the raw strings ... commencing trial and error to debug the following error => "OSError: [Errno 22] Invalid argument: '"r + str(dir_name) + str(\'\\\') + str(output1_file_name))Financial_Analysis_PyBank.txt'"

original_location =   dir_name+'/'+output1_file_name 
#NOTE this is the "sourcePath" for G for Geeks. Where "source" is the file for us ... and "path" ... is the location ...
target_location =   dir_name+'/'+output_file_path1
#NOTE this is the "destinationPath" for G for Geeks. Where "source" AND "path" (dir_name) are "one in the same" (IE: we're not "targeting the file") ... and "destination"... is the NEW FOLDER ... That the file will be moved INTO ...

if os.path.exists(target_location + output1_file_name):
     try:
          os.remove(target_location+output1_file_name)     #"/"+output1_file_name)
          print(f"Existing {output1_file_name} file removed within:\n{target_location}")
          movedToDestination = shutil.move(original_location,target_location)
     except: 
          print("error + failed")
     else:
          movedToDestination = shutil.move(original_location,target_location)
          print(f"if not first run ... second copy created somehow ... ")

#check if the file already exists in the destination. via URL => https://pynative.com/python-move-files/
#if os.path.exists(dst_folder + file_name):
#if os.path.exists(target_location + output1_file_name):
#    print(output1_file_name, "already exists in the destination path! Deleting so that most recent copy is in destination path.")
#    #removing existing file to enable "_new" creation.
#    os.remove(target_location+"/"+output1_file_name)
#    print("-----")
#    print("Analysis output file created with '_new' tag to confirm it was removed and replaced.")

    #KEY NOTE below is tied to "isdir" ... on the G for Geeks example ... I am working on a file ... so I just need the "elif" branch to remove existing in my coding approach.

    #Confirm file exists in destination path (target_location) from prior script run. 
    #print(output1_file_name, "already exists in the destination path! Deleting so that most recent copy is in destination path.")
    #shutil.rmtree(target_location)
    
    # Split name and extension of new file replacing the existing file (likely want to remove the "_new" below for my submission)
#    data = os.path.splitext(output1_file_name)
#    only_name = data[0]
#    extension = data[1]
    # Adding the new name
#    new_base = only_name + '_new' + extension
    # construct full file path
#    new_name = os.path.join(target_location, new_base)
    # move file
#    shutil.move(src_folder + file_name, new_name)
#    destination1 = shutil.move(original_location + output1_file_name, new_name)
#else:
#    destination2 = shutil.move(original_location , target_location)        #shutil.move(original_location + output1_file_name, target_location) # + output1_file_name)
#ABOVE = IF EXISTS LOGIC via URL => https://pynative.com/python-move-files/
#shutil.move(original_location,target_location) 

print(output1_file_name, "has been relocated!")
print("-----")
print(f"The following list is the content of the original path/directory:\n {os.listdir(validated_current_dir)}")
print(f"Analysis file name: {output1_file_name} \n Has now been placed in the path/directory of:\n{target_location}")
#print("Destination Path:\n", destination1, destination2)