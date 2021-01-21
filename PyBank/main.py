#This challenge is to create a Python script to analyze the financial records, Profit/Losses of a company.

#Importing modules

import os
import csv

#Path to Resources

budgetData = os.path.join("Resources","budget_data.csv")

#Reading the CSV

with open(budgetData) as csvfile:
    readBudgetData = csv.reader(csvfile, delimiter= ",")
    print(readBudgetData)
    
    dataheader = next(readBudgetData)
    print(dataheader)

#Setting up variables

    netTotal = 0

    #For loop printing the csv
   
    for row in readBudgetData:
        profitLoss = int(row[1])
        print(row)



        #Sum of the net total amount of Profit/Losses of the entire period

        netTotal += profitLoss
    
    #Printing Summary Table
    print(f'Financial Analysis')
    print("-" * 28)
    print(f'Total: ${netTotal}')