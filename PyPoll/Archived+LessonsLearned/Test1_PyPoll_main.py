import csv
import os

# Change directory to the directory of the current python script.
script_abs_path = os.path.abspath(__file__)
script_dir_name = os.path.dirname(script_abs_path)
os.chdir(script_dir_name)

# Confirm actual Current Directory for Building out Path.
validated_current_dir = os.getcwd()

# Validate location of current_dir in relation to Resources "Source Data" files.
print(f"The .py script's current location is:\n{validated_current_dir}")
print("-+-+-+-+-+-")

# Create VARs for File Paths for code simplicity.
source1_csv_name = "election_data.csv"
input_file_path1 = os.path.join("Resources", source1_csv_name)

# Create VAR for Output File Name.
output_folder_name = "Analysis"
output1_file_name = "Candidates_Analysis_PyPoll.txt"
output_folder_path1 = os.path.join(script_dir_name, output_folder_name,output1_file_name)

# Opening and reading the .csv file.
with open(input_file_path1, 'r', encoding='utf-8-sig', newline='') as csv_file1:
    csv_reader = csv.reader(csv_file1, delimiter=",")
    
    # Create Exploratory analysis for the Header Row to assess the .csv file width.
    header1a = next(csv_file1).strip().split(",")
    csv1a_width = len(header1a)
    print(f"Test - Data Check - CSV reader headers are: {header1a}")
    print(f"The width of the CSV is: {csv1a_width}")
    print("+-------+")

# Initialize Variables

    candidates = {}
    total_votes = 0
    winner = ""

 #Extract the candidates names from the row
    for row in csv_reader:
        candidate = row[2]

        #Count the total number of votes
        total_votes += 1

        #track the number of votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Determining the winner based on popular vote
winner = max(candidates, key=candidates.get)

#Calculate the percentage of of vote for each candidate
percentages = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes)
    percentages[candidate] = (percentage * 100)

#insert analysis here in future fix ..

#Printing results to .txt file
with open(output_folder_path1, "w") as file:
    file.write("Election Results\n")
    file.write("\n")
    file.write("---------------------\n")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("\n")
    file.write("---------------------\n")
    file.write("\n")

    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        file.write("\n")
        file.write("\n")
    file.write("---------------------\n")
    file.write("\n")
    file.write(f"Winner: {winner}\n")
    file.write("\n")
    file.write("---------------------\n")

with open(output_folder_path1,'r') as file:
    ouput_content = file.read()
    print(ouput_content)