import os
import csv

# get file path
bank_csv = os.path.join(".", "Resources", "budget_data.csv")

# declare and initialize variables
total_months = 0
total_Profit_Loss = 0

# declare empty list
profit_loss_list = []

# declare empty list
profit_loss_change_list = []

with open(bank_csv) as csvfile:
    
    #hold content in a variable and specify delimiter
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    csv_header = next(csvreader)

    for row in csvreader:

        total_months = total_months + 1
        total_Profit_Loss += int(row[1])

        profit_loss_list.append([row[0], int(row[1])])

count = len(profit_loss_list)

for i in range(count):
    if i > 0:
        profit_loss_change_list.append([(profit_loss_list[i][0]),(int(profit_loss_list[i][1])-int(profit_loss_list[i-1][1]))])

total_profit_loss_change = 0

max= profit_loss_change_list[0][1]
min= profit_loss_change_list[0][1]

for item in profit_loss_change_list:
    total_profit_loss_change +=item[1]
    if item[1] > max:
        max = item[1]
        greatest_profit_increase_date=item[0]
    if item[1] < min:
        min = item[1]
        greatest_profit_decrease_date=item[0]


avg_percent_change= round(total_profit_loss_change/(len(profit_loss_change_list)),2)


# Print output to terminal
print("Financial Analysis\n")
print("-----------------------------------------------\n")
print ("Total Months: " + str(total_months)+"\n")
print ("Total: $" + str(total_Profit_Loss)+"\n")
print ("Average Change: $" + str(avg_percent_change)+"\n")
print(f'Greatest Increase in Profits: {greatest_profit_increase_date} (${max}) \n')
print(f'Greatest Decrease in Profits: {greatest_profit_decrease_date} (${min}) \n')

