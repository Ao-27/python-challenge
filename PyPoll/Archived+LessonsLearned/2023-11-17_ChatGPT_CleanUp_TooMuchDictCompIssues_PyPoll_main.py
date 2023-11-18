import csv
import os

# Change directory to the directory of the current python script.
abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)
os.chdir(dir_name)

# Confirm actual Current Directory for Building out Path.
validated_current_dir = os.getcwd()

# Validate location of current_dir in relation to Resources "Source Data" files.
print(f"The .py script's current location is:\n{validated_current_dir}")
print("-+-+-+-+-+-")

# Create VARs for File Paths for code simplicity.
source1_csv_name = "election_data.csv"
output1_file_name = "Candidates_Analysis_PyPoll.txt"
input_file_path1 = os.path.join("Resources", source1_csv_name)

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
    Loop_PlaceHolder = []
    total_votes = 0

    # Initialize python data fetching for each row in the .csv source data.
    for count, row_1a in enumerate(csv_reader, 1):
        Records_forAnalysis = {}
        num_rows = count
        Records_forAnalysis.update({"Row_ID": num_rows})

        # Capture Each Column in String to preserve original Data Source Info.
        Ballot_IDs = str(row_1a[0])
        Records_forAnalysis.update({str(header1a[0]): Ballot_IDs})

        County = str(row_1a[1])
        Records_forAnalysis.update({str(header1a[1]): County})

        Candidates = str(row_1a[2])
        Records_forAnalysis.update({str(header1a[2]): Candidates})

        # Add 1 to each row observed to count the total votes.
        total_votes += 1
        Vote_Counted = str("Each_VoteCounted")
        Records_forAnalysis.update({str(Vote_Counted): total_votes})

        Loop_PlaceHolder.append(Records_forAnalysis)

    print(Loop_PlaceHolder[0])
    print(Loop_PlaceHolder[1])
    print(Loop_PlaceHolder[99])
    print(Loop_PlaceHolder[100])
    print(Loop_PlaceHolder[1578])
    print(Loop_PlaceHolder[10000])
    print(Loop_PlaceHolder[220000]) #Key to remember/note for the list comprehensions ... the true index is "neg 1" ... to my count of votes ...
    print("+-+ .py script has completed looping to fetch data  +-+")

# Further analysis and calculations can be added here as needed. 
     #Prompted 2 times Chat GPT with the following => 
     #Prompt 1 => how can I use the "get()" function from within the "Loop_Placeholder" to fetch the maximum votes counted from the "Records_forAnalysis" dict key titled "Each_VoteCounted".
     #Prompt 2 => can you show me how to replace the lambda piece with a list comprehension if/else statement ... where if the value is less than or equal to "0" ... we would not count it?
#Please note I am differing to ChatGPT here for the time savings to meet deadlines.
#Also, I'm in agreement with the logical approach of the code below and have edited it for alignment.
     #I'm aware that the initial piece returned by GPT is "use less" for this module ask ... but it fits my logical coding approach and have maintained it for future use cases ... 

# Assuming Loop_PlaceHolder contains dictionaries with "Each_VoteCounted" as a key



#legitimate_votes = [d.get("Each_VoteCounted", 0) for d in Loop_PlaceHolder if d.get("Each_VoteCounted", 0) > 0]

## Check if there are any valid votes
#if legitimate_votes:
#    max_votes = max(legitimate_votes)
    
#    # Find the winning candidate
#    winning_vote_total = [d.get("Candidates", "Unknown Candidate") for d in Loop_PlaceHolder if d.get("Each_VoteCounted", 0) == max_votes]
#    winning_candidate = winning_vote_total[0] if winning_vote_total else "Unknown Candidate"

#    # Print the results
#    print(f"The winning candidate is {winning_candidate} with {max_votes} votes.")
#else:
#    print("No valid votes.")



    from collections import Counter

# Assuming Loop_PlaceHolder contains dictionaries with "Each_VoteCounted" and "Candidates" as keys
legitimate_votes = [d.get("Each_VoteCounted", 0) for d in Loop_PlaceHolder if d.get("Each_VoteCounted", 0) > 0]

# Check if there are any valid votes
if legitimate_votes:
    max_votes = max(legitimate_votes)
    
    # Find the winning candidate
    winning_candidates = [d.get("Candidates", "Unknown Candidate") for d in Loop_PlaceHolder if d.get("Each_VoteCounted", 0) == max_votes]
    winning_candidate = winning_candidates[0] if winning_candidates else "Unknown Candidate"

    # Count occurrences of each candidate
    candidate_counts = Counter([d.get("Candidates") for d in Loop_PlaceHolder if d.get("Each_VoteCounted", 0) > 0])

    # Print the results
    print(f"The winning candidate is {winning_candidate} with {max_votes} votes.")
    print("Candidate Vote Counts:")
    for candidate, count in candidate_counts.items():
        print(f"{candidate}: {count} votes")
else:
    print("No valid votes.")

    # Assuming Loop_PlaceHolder contains dictionaries with "Candidates" as a key
candidate_tally = {d.get("Candidates"): candidate_tally.get(d.get("Candidates"), 0) + 1 for d in Loop_PlaceHolder}

# Print the results
for candidate, count in candidate_tally.items():
    print(f"{candidate}: {count} votes")