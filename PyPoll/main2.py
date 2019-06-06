import os
import csv

os.chdir(os.path.dirname(__file__))

# Set path for file
csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

    votes = 0
    candidates = []
    count_cand1 = 0
    count_cand2 = 0
    count_cand3 = 0
    count_cand4 = 0
    

    for row in csvreader:
        # Calculate the total amount of votes
        votes += 1
        new_candidate = row[2]

        # Create the complete list of candidates
        if new_candidate not in candidates:
            candidates.append(new_candidate)


        # Count the number of votes each candidate received and calculate the percentage

        if row[2] == candidates[0]:
            count_cand1+=1
        elif row[2] == candidates[1]:
            count_cand2+=1
        elif row[2] == candidates[2]:
            count_cand3+=1
        elif candidates[3]:
            count_cand4+=1

    # Determine vote percentages

    perc_cand1 = count_cand1 / votes
    perc_cand2 = count_cand2 / votes
    perc_cand3 = count_cand3 / votes
    perc_cand4 = count_cand4 / votes

    winner = max(count_cand1, count_cand2, count_cand3, count_cand4)

    # Print to the terminal 

    print("")
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(votes))
    print("----------------------------")
    print(candidates[0] + ": " + "{:.000%}".format(perc_cand1) + " (" + str(count_cand1) + ")")
    print(candidates[1] + ": " + "{:.000%}".format(perc_cand2) + " (" + str(count_cand2) + ")")
    print(candidates[2] + ": " + "{:.000%}".format(perc_cand3) + " (" + str(count_cand3) + ")")
    print(candidates[3] + ": " + "{:.000%}".format(perc_cand4) + " (" + str(count_cand4) + ")")
    print("----------------------------")
    
    # Determine the winner
    if max(count_cand1, count_cand2, count_cand3, count_cand4) == count_cand1:
        print("Winner: " + str(candidates[0]))
    elif max(count_cand1, count_cand2, count_cand3, count_cand4) == count_cand2:
        print("Winner: " + str(candidates[1]))
    elif max(count_cand1, count_cand2, count_cand3, count_cand4) == count_cand1:
        print("Winner: " + str(candidates[2]))
    elif max(count_cand1, count_cand2, count_cand3, count_cand4) == count_cand1:
        print("Winner: " + str(candidates[3]))
    
    print("----------------------------")

# Export the financial analysis to a text file

new_file = open("election_data.txt", "w")

new_file.write("Election Results \n")
new_file.write("---------------------------- \n")
new_file.write("Total Votes: " + str(votes) + "\n")
new_file.write(candidates[0] + ": " + "{:.000%}".format(perc_cand1) + " (" + str(count_cand1) + ") \n")
new_file.write(candidates[1] + ": " + "{:.000%}".format(perc_cand2) + " (" + str(count_cand2) + ") \n")
new_file.write(candidates[2] + ": " + "{:.000%}".format(perc_cand3) + " (" + str(count_cand3) + ") \n")
new_file.write(candidates[3] + ": " + "{:.000%}".format(perc_cand4) + " (" + str(count_cand4) + ") \n")
new_file.write("---------------------------- \n")
if max(count_cand1, count_cand2, count_cand3, count_cand4) == count_cand1:
    new_file.write("Winner: " + str(candidates[0]))
elif max(count_cand1, count_cand2, count_cand3, count_cand4) == count_cand2:
    new_file.write("Winner: " + str(candidates[1]))
elif max(count_cand1, count_cand2, count_cand3, count_cand4) == count_cand1:
    new_file.write("Winner: " + str(candidates[2]))
elif max(count_cand1, count_cand2, count_cand3, count_cand4) == count_cand1:
    new_file.write("Winner: " + str(candidates[3]))