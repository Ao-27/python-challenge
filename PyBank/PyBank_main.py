#See Archived+LessonsLearned file titled => "2023-11-17_ChatGPT_PreSimplified_PyBank_main"

# Import Dependencies
import os
import csv

# Change directory to the directory of the current python script.
script_abs_path = os.path.abspath(__file__)
script_dir_name = os.path.dirname(script_abs_path)
os.chdir(script_dir_name)

# Confirm actual Current Directory for Building out Path.
validated_current_dir = os.getcwd()

# Validate location of the current_dir in relation to Resources "Source Data" files.
print(f"The now Validated .py script's current location is:\n{validated_current_dir}")
print("-+-+-+-+-+-")

# Create VAR for Output File Name.
output_folder_name = "Analysis"
output_folder_dir = os.path.join(script_dir_name, output_folder_name)

# Check if the Output Directory folder exists, if not, create it.
if not os.path.exists(output_folder_dir):
    os.mkdir(output_folder_dir)
    print(f"The Output Directory folder Titled {output_folder_name} was created.")
else:
    print(f"The Output Directory folder Titled {output_folder_name} already exists.")

print("-+-For Loop End-+-\n")

# Create VAR for Output File Name.
output1_file_name = "Financial_Analysis_PyBank.txt"
output_file_path1 = os.path.join(output_folder_dir, output1_file_name)

# Create VARs for File Paths for code simplicity.
input1_file_name = "budget_data.csv"
inputfiles_folder_name = "Resources"
input_folder_dir = os.path.join(script_dir_name, inputfiles_folder_name)
csv_input_file_path1 = os.path.join(input_folder_dir, input1_file_name)

# Opening and reading the .csv file.
with open(csv_input_file_path1, 'r', encoding='utf-8-sig', newline='') as csv_file1:
    csv_reader = csv.reader(csv_file1, delimiter=",")
    header1a = next(csv_file1).strip().split(",")
    csv1a_width = len(header1a)
    print("Test - Data Check - CSV reader headers are:")
    print(header1a) #PRODUCES a list ... which can be a VAR[0] or VAR[1] to leverage ... 
    print(f"The width of the CSV is : {csv1a_width}") #via => https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
    print("+-------+")
    
    # Initialize Variables
    Loop_PlaceHolder = []
    total_row_months = 0
    net_rowsum_prof_loss = 0
    curr_row_prof_loss = 0
    prior_row_prof_loss = 0

    # Iterate through rows in the .csv source data.
    for count, row_1a in enumerate(csv_reader, 1):
        Records_forAnalysis = {}
        num_rows = count
        Records_forAnalysis.update({"Row_ID": num_rows})

        date_col = str(row_1a[0])
        Records_forAnalysis.update({str(header1a[0]): date_col})

        prior_row_prof_loss = float(curr_row_prof_loss)
        Records_forAnalysis.update({"Prior_Row_Profit_Loss": prior_row_prof_loss})

        total_row_months += 1
        Records_forAnalysis.update({"Total_Months_Calculated": total_row_months})

        curr_row_prof_loss = 0 + int(row_1a[1])
        Records_forAnalysis.update({str(header1a[1]): curr_row_prof_loss})

        net_rowsum_prof_loss += float(curr_row_prof_loss)
        Records_forAnalysis.update({"Net_Profit_Loss_RollingTotal": net_rowsum_prof_loss})

        if count == 1:
            calc_prof_loss_change = 0 + curr_row_prof_loss
            Records_forAnalysis.update({"ChangeOf_Value_Difference": float(calc_prof_loss_change)})
        elif count > 1:
            calc_prof_loss_change = curr_row_prof_loss - prior_row_prof_loss
            Records_forAnalysis.update({"ChangeOf_Value_Difference": float(calc_prof_loss_change)})

        Loop_PlaceHolder.append(Records_forAnalysis)

    print(Loop_PlaceHolder)
    print("+-+-+-+")

# Calculate Greatest Increase, Greatest Decrease, and Average Monthly Change
Greatest_Increase = max([d["ChangeOf_Value_Difference"] for d in Loop_PlaceHolder])
Greatest_Increase_Date = [d[header1a[0]] for d in Loop_PlaceHolder if d["ChangeOf_Value_Difference"] == Greatest_Increase]
Greatest_Decrease = min([d["ChangeOf_Value_Difference"] for d in Loop_PlaceHolder])
Greatest_Decrease_Date = [d[header1a[0]] for d in Loop_PlaceHolder if d["ChangeOf_Value_Difference"] == Greatest_Decrease]
Max_Months = max([d["Total_Months_Calculated"] for d in Loop_PlaceHolder])
Avg_Mthly_Chg_2ndRowOn = sum([d["ChangeOf_Value_Difference"] for d in Loop_PlaceHolder][1:]) / (Max_Months - 1)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_row_months)}")
print(f"Total: ${net_rowsum_prof_loss:.2f}")
print(f"Average Change: ${Avg_Mthly_Chg_2ndRowOn:.2f}")
print(f"Greatest Increase in Profits: {str(Greatest_Increase_Date[0])} (${Greatest_Increase:.2f})")
print(f"Greatest Decrease in Profits: {str(Greatest_Decrease_Date[0])} (${Greatest_Decrease:.2f})\n\n")

# Export the analysis to a text file
with open(output_file_path1, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {str(total_row_months)}\n")
    file.write(f"Total: ${net_rowsum_prof_loss:.2f}\n")
    file.write(f"Average Change: ${Avg_Mthly_Chg_2ndRowOn:.2f}\n")
    file.write(f"Greatest Increase in Profits: {str(Greatest_Increase_Date[0])} (${Greatest_Increase:.2f})\n")
    file.write(f"Greatest Decrease in Profits: {str(Greatest_Decrease_Date[0])} (${Greatest_Decrease:.2f})\n")
    file.close()

print(f"Analysis file has been created as:\n{output1_file_name}\n\nBefore py.script moving file - open + write created file within the directory of:\n{script_dir_name}\n")
print(f"The file has been placed within:\n{output_folder_dir}\n-+-+-+-+-+-\n")
print("++Script_END++\n\n")