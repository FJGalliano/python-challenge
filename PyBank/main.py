import os
import csv

csv_file = open('PyBank_budget_data_1.csv')

csv_df1 = csv.reader(csv_file)

dates =[]
revenue = []
total = 0
count = 0
avg_chg = 0
rev_max = 0
rev_min = 0
revenue_last = 0
revenue_next = 0
revenue_diff = 0
sum_diff = 0
row_index = 0

for row in csv_df1:
    dates.append(row[0])
    revenue.append(row[1])
    total += int(row[1])
    #revenue_diff =  
    avg_chg = total/len(revenue)
    rev_max = max(revenue)
    rev_min = min(revenue)

        
    #revenue_last = row[1]
    #revenue_next = (row[1]+1)
    #revenue_diff = revenue_next - revenue_last
    #print(revenue_diff)


#print(total)
# below is a code to count the number of months in the dataset
#print(len(dates))
## below is a code to count the number of months of revenues in the dataset
#print(len(revenue))

print("                        ")
print("Financial Analysis")
print("-------------------------------------------")
print("Total Months:" + "  " + str(len(dates)))
print("Total Revenues:" + "  " + "$" + str(total))
print("Average Revenue Change" + " "+ "$" + str(avg_chg))
print("Greatest Increase in Revenue" +" " + "$" + str(rev_max))
print("Greatest Decrease in Revenue" +" "+ "$" + str(rev_min))

csv_file.close()
