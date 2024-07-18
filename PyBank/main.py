import os 
import csv

# Define the path to the CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Print the path to verify
print(f"CSV Path: {csvpath}")

# Initialize variables
total_months = 0
net_total = 0
changes = []
previous_profit = None
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Print initial values to verify
print(f"Initial values:\nTotal Months: {total_months}\nNet Total: {net_total}\nChanges: {changes}\nPrevious Profit: {previous_profit}\nGreatest Increase: {greatest_increase}\nGreatest Decrease: {greatest_decrease}")

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Read the header

    # Verify the header
    print(f"Header: {header}")

    for row in csvreader:
        # Verify the content of each row
        print(f"Row: {row}")

        # Count total months
        total_months += 1
        
        # Calculate net total
        current_profit = int(row[1])
        net_total += current_profit

        # Calculate changes and track greatest increase and decrease
        if previous_profit is not None:
            change = current_profit - previous_profit
            changes.append(change)
            
            # Check for greatest increase
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = change
            
            # Check for greatest decrease
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = change
        
        # Update previous profit
        previous_profit = current_profit

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Print the results
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

print(results)

# Write the results to a text file
output_path = os.path.join('analysis', 'results.txt')
with open(output_path, 'w') as textfile:
    textfile.write(results)

# Verify the results were written to the file
print(f"Results written to {output_path}")









