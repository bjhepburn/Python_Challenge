import os
import csv

# Data Path
budget_csv = os.path.join('Resources','budget_data.csv')

# Read in CSV
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

# Initialize variables
    data = [0,0,0,'',0,'',0]
    total_change = 0


# Iterate through rows
    for row in csvreader:

# Count months
        data[0] += 1

# Determine net total
        data[1] = data[1] + int(row[1])

# Determine total change
        if data[0] == 1:
            x = int(row[1])
        else:
            y = int(row[1])
            change = y-x
            total_change = total_change + (y-x)
            x=y

# Determine greatest increase and decrease in profit        
            if change > data[4]:
                data[4] = change
                data[3] = row[0]
            if change < data[6]:
                data[6] = change
                data[5] = row[0]

# Calculate average change        
    data[2] = round(total_change/(data[0]-1),2)

# Print data
    print("Financial Analysis")
    print("------------------------")
    print(f'Total Months: {data[0]}')
    print(f'Total: ${data[1]}')
    print(f'Average Change: {data[2]}')
    print(f'Greatest Increase in Profits: {data[3]} (${data[4]})')
    print(f'Greatest Decrease in Profits: {data[5]} (${data[6]})')