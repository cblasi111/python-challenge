import os
import csv
import locale

os.chdir(os.path.dirname(__file__))

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Open the file
with open(csvpath, newline = "") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ",")

    header = next(csv_reader)
    first_row = next(csv_reader)

    month = 1
    profit_loss = int(first_row[1])
    previous_value = first_row[1]
    monthly_changes = []
    max_increase = 0 
    max_decrease = 0

    for row in csv_reader:
        
        # Count total number of months
        month += 1

        # Add the total P/L
        profit_loss += int(row[1])

        # Create a list of the P/L deltas and print the average of these values
        net_change = int(row[1]) - int(previous_value)
        previous_value = int(row[1])
        monthly_changes.append(net_change)
        
        # Determine the greatest increase and decrease of the P/L deltas
        if net_change > max_increase:
            max_increase = net_change
            date_time1 = row[0]
        elif net_change < max_decrease:
            max_decrease = net_change
            date_time2 = row[0]

    # Calculate the average change
    average_change = ((sum(monthly_changes))/(len(monthly_changes)))


    # Print the analysis
    print("")
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(month))
    print("Total P/L: " + " $" + str(profit_loss))
    print("Average Change: " +  " $" + str("%.2f" % round(average_change,2)))
    print("Greatest Increase in Profits: " + str(date_time1) + " ($" + str(max_increase) + ")")
    print("Greatest Decrease in Profits: " + str(date_time2) + " ($" + str(max_decrease) + ")")


# Export the financial analysis to a text file

new_file = open("budget_data.txt", "w")

new_file.write("Financial Analysis \n")
new_file.write("---------------------------- \n")
new_file.write("Total Months: " + str(month) + "\n")
new_file.write("Total P/L: " + " $" + str(profit_loss) + "\n")
new_file.write("Average Change: " +  " $" + str("%.2f" % round(average_change,2)) + "\n")
new_file.write("Greatest Increase in Profits: " + str(date_time1) + " ($" + str(max_increase) + ") \n")
new_file.write("Greatest Decrease in Profits: " + str(date_time2) + " ($" + str(max_decrease) + ") \n")