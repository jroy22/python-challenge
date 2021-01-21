#This challenge is to create a Python script to analyze the financial records, Profit/Losses of a company.

#Importing modules

import os
import csv

#Path to Resources

budgetData = os.path.join("Resources","budget_data.csv")

#Opening budget_data.csv

with open(budgetData) as csvfile:
    
    #Reading the CSV

    readBudgetData = csv.reader(csvfile, delimiter= ",")
    dataheader = next(readBudgetData)

    #Setting up variables
    
    totalMonths = 0
    netTotal = 0
    greatIncrease = 0
    greatDecrease = 0

    #For loop going through each row of data
   
    for row in readBudgetData:

        #Variables based on the CSV header

        date = row[0]
        profitLoss = int(row[1])

        #The number of months in the entire period

        totalMonths += 1

        #Sum of the net total amount of Profit/Losses of the entire period

        netTotal += profitLoss

        #Getting the Greatest Increase in Profits

        if profitLoss > greatIncrease:
            greatIncrease = profitLoss
            increaseDate = date
        
        #Getting the Greatest Decrease in Profits

        if profitLoss < greatDecrease:
            greatDecrease = profitLoss
            decreaseDate = date

    #Calculating Average Change

    avgChange = round((netTotal / totalMonths), 2)

    #Printing Summary Table

    def summary():
        print(f'Financial Analysis')
        print("-" * 28)
        print(f'Total Months: {totalMonths}')
        print(f'Total: ${netTotal}')
        print(f'Average Change: ${avgChange}')
        print(f'Greatest Increase in Profits: {increaseDate} (${greatIncrease})')
        print(f'Greatest Decrease in Profits: {decreaseDate} (${greatDecrease})')
    
    summary()

#Path for Analysis

budgetAnalysis = os.path.join("Analysis","budget_analysis.txt")

#Opening budget_analysis.txt

with open(budgetAnalysis, 'w', newline="") as textfile:
    print(f'Financial Analysis', file = textfile)
    print("-" * 28, file = textfile)
    print(f'Total Months: {totalMonths}', file = textfile)
    print(f'Total: ${netTotal}', file = textfile)
    print(f'Average Change: ${avgChange}', file = textfile)
    print(f'Greatest Increase in Profits: {increaseDate} (${greatIncrease})', file = textfile)
    print(f'Greatest Decrease in Profits: {decreaseDate} (${greatDecrease})', file = textfile)
