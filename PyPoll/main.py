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
    candidateList= []
    

    #For loop going through each row of data
   
    for row in readElectionData:

        #Variables based on the CSV header

        voterId = row[0]
        county = row[1]
        candidate = row[2]
       
        #The total number of votes
        totalVotes += 1

        #List of candidates
        
        for name in candidate:
            if name not in candidateList:
                candidateList.append(name)


    #Create a dictionary for Candidate names

    Candidates = {}       
    Candidates["Name"] = candidateList
    print(Candidates)

    #Printing Summary Table

    print("Election Results")
    print("-" * 25)
    print(f'Total Votes: {totalVotes}')
    print("-" * 25)
    # print(f'{candidate[0]}: {percentage}, {numberofvotes}')
    # print(f'{candidate[1]}: {percentage}, {numberofvotes}')
    # print(f'{candidate[2]}: {percentage}, {numberofvotes}')
    # print(f'{candidate[3]}: {percentage}, {numberofvotes}')
    print("-" * 25)
    #  print(f'Winner: {winner}')