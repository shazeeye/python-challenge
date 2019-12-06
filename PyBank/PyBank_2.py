import os
import csv

total_months=0
total_net=0
total_profit_loss=0
greatest_increase=0
greatest_decrease=0
date_greatest_increase=0
budget_greatest_increase=0
date_greatest_decrease=0
budget_greatest_decrease=0

#reading csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')
date=[]
total_profit_loss=[]
average_change=[]
change_net=0
maximum_increase=0
maximum_decrease=0
# got help from my tutor Donish Cushing to define this
maximum_increase = ["", 0]
maximum_decrease = ["", 99999999999]
with open(budget_csv, newline="")as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    first_values = next(csvreader)
    total_months = total_months + 1 # adding for total months
    total_net = total_net + int(first_values[1]) # total revenue is calculated by adding revenue values to total_net
    prev_net = int(first_values[1])#saving previous month's revenue in prev_net

    previous_revenue=int(first_values[1])
    for row in csvreader:
        total_months = total_months + 1
        current_revenue = int(row[1])
        total_net = total_net + current_revenue
        change=current_revenue-previous_revenue # calculates revenue change 
        change_net=change_net+change #calculates the average revenue change 
    
        
        previous_revenue=current_revenue #have to swap columns to calculate next revenue change before going to next row
    # finding max and min values
        if change > maximum_increase[1]: 
            maximum_increase[1] = change
            maximum_increase[0]=row[0]
        if change < maximum_decrease[1]:
            maximum_decrease[1] = change  
            maximum_decrease[0]=row[0] 
    # printing output
    print(f"Total months:{total_months}")
    print(f"Total:{total_net}")
    print(f"Average Change:{change_net/(total_months-1)}")
    print(f"Maximum decrease and month:{maximum_decrease}")
    print(f"Maximum increase and month:{maximum_increase}")
    
   
   #writing to output file     
outputfile=os.path.join("output.csv")
with open(outputfile, "w", newline="")as csvfile:
    writer=csv.writer(csvfile, delimiter=" ")
    writer.writerow({'Financial Analysis'})
    writer.writerow({'Total months'})
    writer.writerow([total_months])
    writer.writerow({'Total Net in Dollars'})
    writer.writerow([total_net])
    writer.writerow({'Average change in Dollars'})
    writer.writerow([(change_net/(total_months-1))])
    writer.writerow({'Maximum increase in profits($) and month'})
    writer.writerow([maximum_increase])
    writer.writerow({'Maximum decrease in profits($) and month'})
    writer.writerow([maximum_decrease])