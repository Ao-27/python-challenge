#Import Dependencies for loading Started Data/Code.
import os 
#+New OS Remove BP URL => https://python-forum.io/thread-24158.html
#ChgDIR URL => https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
#TRY BLOCK Suggestion for OR Remove URL => https://www.reddit.com/r/learnpython/comments/8ynsin/help_with_shutilmove_and_overwrite_if_it_exists/
#+Nre BP => https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
import csv
import shutil 
#+New BP URL => https://9to5answer.com/move-and-replace-if-same-file-name-already-exists
#+oldBP URL - Move + Rename File => https://pynative.com/python-move-files/
#+KnowHow URL -Shutil needs Full Path for Overwrite => https://stackoverflow.com/questions/31813504/move-and-replace-if-same-file-name-already-exists
     #shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
#Tutorial URL => https://note.nkmk.me/en/python-shutil-move/
from pathlib import Path #+new my_file.exists() URL => https://stackoverflow.com/questions/45134102/shutil-move-if-directory-already-exists

# Change directory to the directory of current python script. via URL => https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory
print("++Script_START++")
print("+-+-+-+")
script_abs_path = os.path.abspath(__file__)   #FINDS => Full FILEPATH to this EXACT ".py" or ".ipynb" file .... 
print(script_abs_path)
script_dir_name = os.path.dirname(script_abs_path)  #FINDS => PARENT FOLDER ... this EXACT ".py" or ".ipynb" file ....
print(script_dir_name)
print("-----")
os.chdir(script_dir_name)

#Confirm actual Current Directory for Building out Path.
validated_current_dir = os.getcwd()

#Validate location of current_dir in relation to Resources "Source Data" files.
print(f"The now Validated .py script's current location is:\n{validated_current_dir}")
print("\n-+-+-+-+-+-")
#below via URL => https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
print("Prior to Folder Creations - Listing out the directories in current script_dir_name -")
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir))) #NOTE ... using my VARs produces a "str" "TypeError" ...  #list(filter(script_dir_name, os.listdir(os.curdir))) #
print(directories_in_curdir) 
print("-+-+-+-+-+-")

#Create VAR for Output File Name.
output_folder_name  =  "Analysis"
output_folder_dir = str(script_dir_name + "\\" + output_folder_name)

for output_dir in directories_in_curdir:   #Break+Continue Logic URL => https://www.programiz.com/python-programming/break-continue
     if (directories_in_curdir.index(output_folder_name)+1) >= 1: #FOUND somehwere in the list ... because first position is "0" ... it will give us "1" ... 
          print(f"The Output Directory folder Titled {output_folder_name} already exists.")
          break #continue#break via URL => https://www.programiz.com/python-programming/break-continue
     elif [i for i in directories_in_curdir if output_dir == output_folder_dir].count() >= 0:     
     #directories_in_curdir.index(output_folder_name) <= 0: #NOT FOUND anywhere in the list ... because index() function produces "-1" as it's "N/A" ...  #wrong ...it produces a "ValueError" see URL => https://docs.python.org/3/tutorial/datastructures.html
          #CREATE FOLDER.... since .... "no dir with the output_folder_name  ... was found producing "0" ... 
          os.mkdir(output_folder_name)
          print(f"The Output Directory folder Titled {output_folder_name} was created.")
print("-+-For Loop End-+-\n")
#if os.path.exists(output_folder_dir):
#     continue
#else 
#Create Output Directory.
#DO IF EXISTS ... 
output1_file_name = "Financial_Analysis_PyBank.txt"
print(f"The intended output file titled:\n{output1_file_name}\n\nWill have a directory of:\n{output_folder_dir}")
print("-+-+-+-+-+-")
#+
#LIKELY NEED TO ADD OUTPUT FILE PATH HERE ....  ... to get to "2_" ... 
#+
#
#LOOKS LIKE ... my error is to not call it .... "output0all_dir_name" = "/Analysis/" (or whatever it accepts without error...)
#
#Use OS module to establish .txt output location for saving.
#
#output_file_path1 = os.path.join("Analysis")   #,output1_file_name)    #NOTE this is "destination" ... in G for Geeks URL.
#print(output_file_path1)
#print("-+-+-+-+-+-")
##

#Create VARs for File Paths for code simplicity.
input1_file_name = "budget_data.csv" #Title of File for Fetch.
     #via Module 3 => The dataset is composed of two columns: "Date" and "Profit/Losses".
input1_title = str(input1_file_name).split(".")[0]
input1_file_type = str(input1_file_name).split(".")[1]
input1_file_ext = "." + str(input1_file_name).split(".")[1]
print(f"Test Extension Concat is: {input1_file_ext}")
print("-+-+-+-+-+-")

#Use OS module to Fetch CSV data and read Source Data into Python for manipulation.

inputfiles_folder_name = "Resources"
input_folder_dir = str(script_dir_name + "\\" + inputfiles_folder_name)

#Create the path for Python's native programming from current_dir.
csv_input_file_path1 = os.path.join(inputfiles_folder_name,input1_file_name)
     #persNOTE: I'm not in an "Unsolved" folder like in class. So no ".." should be necessary.

#file_path2 = os.path.join("..","Resources",source1_csv_name) 
     #persNOTE: this is for when I work from the "archived+lessonslearned" folder.

print(f"The intended input file titled:\n{input1_title}\nWith the file extension type of:\n{input1_file_type}\n\nWill be accessed via:\n\nThe csv_reader Path is:\n{csv_input_file_path1}\n\nAnd the Input FullPath/Pandas file path is:\n{input_folder_dir}")
#print("-------")
#print(file_path2)
print("-+-+-+-+-+-")

#Opening and reading the .csv file.
with open(csv_input_file_path1, 'r',encoding='utf-8-sig',newline='') as csv_file1:
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


#GREAT LIST COMP BP URL for Syntax => https://stackoverflow.com/questions/13717463/find-the-indices-of-elements-greater-than-x
#Note I found the above ... AFTER ... scripting the information below ... 

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
print("--------\n")
Avg_Mthly_Chg_2ndRowOn = sum([d["ChangeOf_Value_Difference"] for d in Loop_PlaceHolder][1:]) / (Max_Months - 1)
print(round(Avg_Mthly_Chg_2ndRowOn,2)) #via URL => https://www.freecodecamp.org/news/how-to-round-to-2-decimal-places-in-python/
print("--------\n")
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
print(f"Greatest Decrease in Profits: {str(Greatest_Decrease_Date[0])} (${Greatest_Decrease})\n\n")
#
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

print(f"Before py.script moving file - open + write created file within the directory of:\n{script_dir_name}\n\nAnalysis file has been created as:{output1_file_name}")
print("-+-+-+-+-+-\n")


#Move create file to "Analysis" folder directory. via URL => https://datatofish.com/move-file-python/ & https://pynative.com/python-move-files/ & https://www.techbeamers.com/string-concatenation-in-python/
#
#List file being processed in the move. via URL => https://www.geeksforgeeks.org/python-move-and-overwrite-files-and-folders/
#

#Use OS module to establish .txt output location for saving.
print(f"Preparing file to move location to the output directory of:\n{output_folder_dir}")
#print("-------")
#output_file_path1 = os.path.join(output_folder_name)   #,output1_file_name)    #NOTE this is "destination" ... in G for Geeks URL.
#print(output_file_path1)
print("-+-+-+-+-+-\n")
print(f"Prior to moving files the following list is the content of the original path/directory:\n{os.listdir(validated_current_dir)}")
print("-----\n")

print(os.path.join(script_dir_name,output1_file_name)) #ORIGINAL Location ... 
print(os.path.join(output_folder_dir)) #,output1_file_name)) #TARGET Location ... 
print("\n")

#### NEXT STEPS TO FINALIZE APPROACH ... BELOW ... WITHIN THE " #### " ...
print("insert SHUTIL.MOVE() IF_EXISTS() LOGIC BELOW HERE ...\n")
#
#KEY REF... on wrapping in "str()" below ... from above ... 
#
####Create VAR for Output File Name.
#output_folder_name  =  "Analysis"
#output_folder_dir = str(script_dir_name + "\\" + output_folder_name)
####
#
#Create VARs to Enable Shutil Module's next steps. #Raw Strings via URL => https://www.codevscolor.com/python-raw-string

original_location_premove = os.path.join(script_dir_name,output1_file_name)
target_location_premove = os.path.join(output_folder_dir)
archive_folder_name = "Auto_Archived"
archive_location_str = str(output_folder_dir + "\\" + archive_folder_name + "\\") # Note the "output_folder_dir" ... contains the "fetch py script" location ... at the start of it's OWN VAR ... making this more or less "dynamic" ... 
archive_location_postmove = os.path.join(Path(archive_location_str)) ### Needs the wrap in "str()" approach...   ### <<<= FixNote #SOMETHING WRONG ... to investigate ... it's going "c:" then my folder ..
#
#DOESN'T WORK ... #
print(os.path.join(archive_location_postmove))
#WORKS ... #print(target_location_premove) #os.path.join(output_folder_dir))

#via URL => https://stackoverflow.com/questions/45134102/shutil-move-if-directory-already-exists
my_file_test1 = Path(original_location_premove)
print(f"\n{my_file_test1}\nAbove is Target File Test 1 flag.\n")
print(f"Path Module applied to trgt_premove VAR produces:\n{Path(target_location_premove+ '/' + output1_file_name)}\n")
#print(f"{if my_file_test1.exists():}") # LOOKS LIKE .... f-string limitation ... is that it can only use > or < to do "if" calcs ... via List/Dict Comprehensions ... 

##
#
# if (directories_in_curdir.index(output_folder_name)+1) >= 1: #FOUND somehwere in the list ... because first position is "0" ... it will give us "1" ... 
# elif [i for i in directories_in_curdir if output_dir == output_folder_dir].count() >= 0:  
#
##

#Use VARs to emable "if exists" logical checkpoints ... 
#
if not os.path.exists(target_location_premove + output1_file_name):# != True and/& os.path.exists(original_location_premove) == True:
     print(f"Source File Folder Contents - Before File Move:\n{os.listdir(script_dir_name)}") #via URL => https://www.geeksforgeeks.org/python-move-and-overwrite-files-and-folders/    
     try:
          shutil.move(original_location_premove,target_location_premove)
          print(f"Newly created {output1_file_name} moved to:\n{output_folder_dir}\n")
     except shutil.SameFileError:
          print("Newly Created File Not Moved - Logic Error - Source and destination represents the same file.")
     except PermissionError:
          print("Newly Created File Not Moved - System Error - Permission Denied") 
     if os.path.exists(Path(target_location_premove + '/' + output1_file_name)):  #via URL => https://stackoverflow.com/questions/45134102/shutil-move-if-directory-already-exists
     #OLD CODE => #(target_location_premove + output1_file_name):# == True and/& os.path.exists(original_location_premove) == True:
          print(f"Source File Folder Contents - Before File Move:\n{os.listdir(script_dir_name)}") #via URL => https://www.geeksforgeeks.org/python-move-and-overwrite-files-and-folders/    
          try_source = Path(target_location_premove + '/' + output1_file_name) #target_location_premove + output1_file_name    
          try: 
               shutil.copy2(try_source,archive_location_postmove) #via URL => https://www.geeksforgeeks.org/python-shutil-copy2-method/
               print(f"Existing {output1_file_name} found in {target_location_premove}\nNow Moved to {archive_location_postmove}\n")
               os.remove(Path(target_location_premove + '/' + output1_file_name))   #target_location_premove+output1_file_name)     #"/"+output1_file_name)
               print(f"The Existing {target_location_premove + output1_file_name} has now been removed from {target_location_premove}\n")
     #0strat => "crate var for tag" ... to file name ... future plan is to use "date as txt" ... #    new_name = os.path.join(target_location, new_base)
     #nxt stp =>#  move file
     #    shutil.move(src_folder + file_name, new_name)
               shutil.move(original_location_premove,target_location_premove)
               print(f"The Updated {output1_file_name} was moved from original location of:\n{script_dir_name}\nTo new location of:\n{target_location_premove}\n")
          except shutil.SameFileError:
               print("Existing File Not Moved - Logic Error - Source and destination represents the same file.")
          except PermissionError:
               print("Existing File Not Moved - System Error - Permission Denied")
          except ValueError:
               print("ValueError - Try Source Level - Check VARs Processing by functions.")

#
#
print("insert SHUTIL.MOVE() IF_EXISTS() LOGIC ABOVE HERE ...\n")
print(output1_file_name, "has been relocated!\n")
print("+-+-+-+\n")
print(f"Analysis file name: {output1_file_name}\n----\nHas now been placed in the path/directory of:\n{output_folder_dir}\n") # #target_location}")
print("+-+-+-+\n")
print("++Script_END++")