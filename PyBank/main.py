import os
import csv

# Data Path
budget_csv = os.path.join('Resources','budget_data.csv')

# Read in CSV
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

# Initialize variables
    month_count = 0
    net_total = 0
    total_change = 0
    greatest_inc = 0
    greatest_dec = 0

# Iterate through rows
    for row in csvreader:

# Count months
        month_count += 1

# Determine net total
        net_total = net_total + int(row[1])

# Determine total change
        if month_count == 1:
            x = int(row[1])
        else:
            y = int(row[1])
            change = y-x
            total_change = total_change + (y-x)
            x=y

# Determine greatest increase and decrease in profit        
            if change > greatest_inc:
                greatest_inc = change
                greatest_inc_date = row[0]
            if change < greatest_dec:
                greatest_dec = change
                greatest_dec_date = row[0]

# Calculate average change        
    average_change = round(total_change/(month_count-1),2)

# Store print lines in list
    print_list = ["Financial Analysis","------------------------",\
        (f'Total Months: {month_count}'),\
        (f'Total: ${net_total}'),\
        (f'Average Change: {average_change}'),\
        (f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})'),\
        (f'Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})')]

    for z in print_list:
        print(z)

# Write text file
analysis_txt = os.path.join('Analysis','analysis.txt')
with open(analysis_txt, 'w') as f:
    for z in print_list:
        f.write(f'{z}\n')