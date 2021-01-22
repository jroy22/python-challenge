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

    #Setting up variables
    totalVotes = 0
    voteOne = 0
    voteTwo = 0
    voteThree = 0
    voteFour = 0
    candidateList= []
    candidateVotes = []
    candidatePercent = []

    #Create a dictionary for Election Results
    electionResults = {}       
    electionResults["Name"] = candidateList
    electionResults["NumberofVotes"] = candidateVotes
    electionResults["Percentage"] = candidatePercent

    #For loop going through each row of data
   
    for row in readElectionData:

        #Variables based on the CSV header

        voterId = row[0]
        county = row[1]
        candidateName =row[2]
       
        #The total number of votes
        totalVotes += 1

        #Creating a list of candidates
    
        if candidateName not in candidateList:
            candidateList.append(candidateName)

        #Getting the total votes per candidate

        if candidateName == electionResults["Name"][0]:
                voteOne += 1
        elif candidateName == electionResults["Name"][1]:
                voteTwo += 1
        elif candidateName == electionResults["Name"][2]:
                voteThree += 1    
        elif candidateName == electionResults["Name"][3]:
                voteFour += 1

    
    candidateVotes = [voteOne,voteTwo,voteThree,voteFour]
    electionResults["NumberofVotes"] = candidateVotes
    print(electionResults)

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