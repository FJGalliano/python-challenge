import os
import csv



total_votes = 0
candidates = {'Seth': 0, 'Torres': 0, 'Cordin': 0, 'Vestal': 0}

with open('election_data_1.csv') as csv_voting:
    csv_votes = csv.reader(csv_voting)
    next(csv_votes)
    for row in csv_votes:    
        total_votes +=1
        candidates[row[2]]+=1
        
print(candidates)
print(total_votes)

print("Election Results")
print( " ")
print("------------------------------------------------")

print("Total Votes:" + "          " + str(total_votes))
print("------------------------------------------------")
for name, number in candidates.items():
   print(name + "  " + "received" + "    "+ str(number) + " "+ "votes"+ "   "
         + str(number/(total_votes)*100)+ "%")
print("")
print("------------------------------------------------")
print( " ")
print("Winner:" + "  " + name)
print( " ")
print("------------------------------------------------")

