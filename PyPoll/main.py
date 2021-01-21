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

    #Setting up variables
    totalVotes = 0

    #For loop going through each row of data
   
    for row in readElectionData:

        #Variables based on the CSV header

        voterId = row[0]
        county = row[1]
        candidate = row[2]

        #The total number of votes
        totalVotes += 1

        #Sum of the net total amount of Profit/Losses of the entire period

    print(totalVotes)