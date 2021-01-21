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
    
    totalMonths = 0
    netTotal = 0
    greatIncrease = 0
    greatDecrease = 0

    

    #For loop going through each row of data
   
    for row in readBudgetData:

        
        date = row[0]
        profitLoss = int(row[1])
        print(row)

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
    print(f'Financial Analysis')
    print("-" * 28)
    print(f'Total Months: {totalMonths}')
    print(f'Total: ${netTotal}')
    print(f'Average Change: ${avgChange}')
    print(f'Greatest Increase in Profits: {increaseDate} (${greatIncrease})')
    print(f'Greatest Decrease in Profits: {decreaseDate} (${greatDecrease})')
