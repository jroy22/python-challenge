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
    candidateNames= []
    candidateVotes = []
    candidatePercent = []

    #Create a dictionary for Election Results
    electionResults = {}    
    electionResults["Name"] = []
    electionResults["NumberofVotes"] = []
    electionResults["Percentage"] = []

    #For loop going through each row of data
   
    for row in readElectionData:

        #Variables based on the CSV header

        voterId = row[0]
        county = row[1]
        name =row[2]
       
        #The total number of votes
        totalVotes += 1

        #Assigning a list to the Key Name to Dictionary

        electionResults["Name"] = candidateNames
        
        #Assigning values in the list candidateNames

        if name not in candidateNames:
            candidateNames.append(name)

        #Getting the total votes per candidate

        if name == electionResults["Name"][0]:
                voteOne += 1
        elif name == electionResults["Name"][1]:
                voteTwo += 1
        elif name == electionResults["Name"][2]:
                voteThree += 1    
        elif name == electionResults["Name"][3]:
                voteFour += 1
    
    #End of For Loop 

    #Assigning values in the List candidateVotes
    
    candidateVotes = [voteOne,voteTwo,voteThree,voteFour]
   
    #Calculating Vote percentages per candidate

    percentOne = "{:.3%}".format(voteOne / totalVotes)
    percentTwo = "{:.3%}".format(voteTwo / totalVotes)
    percentThree = "{:.3%}".format(voteThree / totalVotes)
    percentFour = "{:.3%}".format(voteFour / totalVotes)

    #Assigning values in the List candidatePercent

    candidatePercent = [percentOne, percentTwo, percentThree, percentFour]

    #Assigning a list to the Keys NumberofVotes and Percent to Dictionary
    electionResults["NumberofVotes"] = candidateVotes
    electionResults["Percentage"] = candidatePercent

    #Find the Winner

    winVotes = max(candidateVotes)
    winIndex = int(candidateVotes.index(winVotes))
    winner = candidateNames[winIndex]

    #Printing Summary Table

    print("Election Results")
    print("-" * 25)
    print(f'Total Votes: {totalVotes}')
    print("-" * 25)
    print(f'{electionResults["Name"][0]}: {electionResults["Percentage"][0]} ({electionResults["NumberofVotes"][0]})')
    print(f'{electionResults["Name"][1]}: {electionResults["Percentage"][1]} ({electionResults["NumberofVotes"][1]})')
    print(f'{electionResults["Name"][2]}: {electionResults["Percentage"][2]} ({electionResults["NumberofVotes"][2]})')
    print(f'{electionResults["Name"][3]}: {electionResults["Percentage"][3]} ({electionResults["NumberofVotes"][3]})')
    print("-" * 25)
    print(f'Winner: {winner}')