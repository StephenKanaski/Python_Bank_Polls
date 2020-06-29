import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

#set lists to store data
profit_total = []
total_months = []
monthly_change = []


with open(budget_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)

	#Loop through dataset
	for row in csvreader:

		#loop through to find total months and total net profit
		total_months.append(row[0])
		profit_total.append(int(row[1]))
		#print(total_months)
		#print(profit_total)

	#Nested loop to determine change in net profit per month
	for i in range(len(profit_total)-1):

		monthly_change.append(profit_total[i+1]-profit_total[i])
		#print(monthly_change)

#Find the greatest increase and index to proper month
greatest_increase = max(monthly_change)
#print(greatest_increase)
month_max = monthly_change.index(max(monthly_change)) + 1
#print(month_max)

#Find the greatest decrease and index to proper month
greatest_decrease = min(monthly_change)
#print(greatest_decrease)
month_min = monthly_change.index(min(monthly_change)) + 1
#print(month_min)

#Print Financial Summary#
#Total number of months in dataset
#Total net profit/loss over entire period
#The Average Change in profit/loss over entire period
#Greatest Increase in Profit (date & amount)
#Greatest Decrease in Profit (date & amount)

print("Financial Summary Statement")
print("--------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Tota Net Profit: ${sum(profit_total)}")
print(f"Average Change in Profit: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest increase in Profits: {total_months[month_max]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[month_min]} (${(str(greatest_decrease))})")
print("--------------------------------")

#Output Financial Summary to text
output_path = os.path.join("PyBank", "Financial_Summary_Statement.txt")
with open(output_path, 'w') as file:

	file.write("Financial Summary Statement")
	file.write("------------------------------")
	file.write(f"Total Months: {len(total_months)}")
	file.write(f"Tota Net Profit: ${sum(profit_total)}")
	file.write(f"Average Change in Profit: ${round(sum(monthly_change)/len(monthly_change),2)}")
	file.write(f"Greatest increase in Profits: {total_months[month_max]} (${(str(greatest_increase))})")
	file.write(f"Greatest Decrease in Profits: {total_months[month_min]} (${(str(greatest_decrease))})")
	file.write("------------------------------")
