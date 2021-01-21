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

#For loop printing the csv

    for row in readBudgetData:
        print(row)
