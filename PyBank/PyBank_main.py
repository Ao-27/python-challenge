#Import Dependencies for loading Started Data/Code.
import os
import csv

#Confirm actual Current Directory for Building out Path.
current_dir = os.getcwd()
#Validate location of current_dir in relation to Resources "Source Data" files.
print(current_dir)
print("-------")

#Create VARs for File Paths for code simplicity.
source1_csv_file = "budget_data.csv" #Title of File for Fetch.
#output1_file = ".txt" #Commented OUT until I actually need it.

#Use OS module to Fetch CSV data and read Source Data into Python for manipulation.
file_path1 = os.path.join("Resources",source1_csv_file) #NOTE: I'm not in an "Unsolved" folder like in class. So no ".." should be necessary.
print(file_path1)
print("-------")

