#This challenge is to help a rural town modernize the counting of their elections.

#Importing modules

import os
import csv

#Path to Resources

electionData = os.path.join("Resources","election_data.csv")

#Opening election_data.csv

with open(electionData) as csvfile:
  
   #Reading the CSV

    readElectionData = csv.reader(csvfile, delimiter= ",")
    dataheader = next(readElectionData) 

    print(readElectionData)
    print(dataheader)
