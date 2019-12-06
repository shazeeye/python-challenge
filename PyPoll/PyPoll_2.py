import os
import csv
#import pandas as pd

winning_count=0
total_votes=0
totalvoteseachcandidate=0
winning_candidate=""
#opening file 
poll_csv = os.path.join('Resources', 'election_data.csv')
voterid=[]
county=[]
candidates=[]
#defining dictionary to store unique candidates and vote summary
dictname={}
summary={}


#data_new=pd.DataFrame(columns=['Name', 'Votes','Vote Percentage'])

with open(poll_csv, newline="")as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        total_votes=total_votes+1
        candidate=row[2] 
       
        #getting unique candidates
        if candidate not in candidates:
    
            dictname [candidate]=0 
            candidates.append(candidate)
           
        else:
            dictname[candidate] = dictname[candidate]+1
            

print (f"Total Votes: {total_votes}\n")



#tutor Donish Cushing told me about get(x)
for x in candidates:
    votes = dictname.get(x)
    vote_percentage = float(votes) / float(total_votes) * 100 
   

   
    #data_new = data_new.append({'Name' : x , 'Votes' : votes, 'Vote Percentage' : vote_percentage},ignore_index=True)
    #print(data_new)

   
    if votes>winning_count:
        winning_count=votes
        winning_candidate=x

    voter_output = f"{x}: {vote_percentage:.3f}% ({votes})\n"
    summary[x]=[x, vote_percentage, votes]
    print(voter_output, end="")
    

            
election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")
winning_candidate_summary=(
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# printing output file. It took me a long time to find out that output files can only be one format (table only or all rows like PyPoll)
outputfile=os.path.join("output.csv")
with open(outputfile, "w", newline="")as csvfile:
    fieldnames=['name', 'vote percentage', 'votes']
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
            'name': 'Total Votes', 
            'vote percentage': ' ', 
            'votes': total_votes
            })
    for name in summary:
        writer.writerow({
            'name': summary.get(name)[0], 
            'vote percentage': summary.get(name)[1], 
            'votes': summary.get(name)[2]
            })
    writer.writerow({
            'name': 'Winner', 
            'vote percentage': ' ', 
            'votes': winning_candidate
            })


    
#data_new.to_csv("/Users/shazeeye.kirmani/Documents/UCB-BEL-DATA-PT-11-2019-U-C/02-Homework/03-Python/Instructions/PyPoll/output.csv")
    
   
    
    