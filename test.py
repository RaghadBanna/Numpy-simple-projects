




import numpy as np 
import pandas as pd
from datetime import date


Goods_or_service = []
Prices = []
Dates = []
Expense_type = []



def add_expence(goods_or_prices , prices , dates , expense_type):
	Goods_or_service.append(goods_or_prices)
	Prices.append(prices)
	Dates.append(dates)
	Expense_type.append(expense_type)

#Main Programm


option = -1
while (option != 0):
	print("Welcome to the simple Expense Tracker...")
	print('1. Add food Expense: ')
	print('2. Add Household Expense: ')
	print('3. Add Transportation Expense: ')
	print('4. Show & Save Transportation Report:')
	print('0. Exit')
	option = int(input("choose an option:\n"))

# printing new line
print()

# if checks metrics

if option == 0:
	print('Exiting Loop')
	break

elif option == 1:
	print('Adding food')
	expense_type = "FOOD"

elif option == 2:
	print('Adding Household')
	expense_type = "HOUSEHOLD"

elif option == 3:
	print('Adding Transportation')
	expense_type = "TRANSPORTATION"

elif option == 4:
	#creating a dataframe for option 4
	

else:

























































































































