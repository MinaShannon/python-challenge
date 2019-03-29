# PyPoll
#Import dependencies
import csv
import os
import sys
#Create necessary variables
candidate=[]
total=0
Khan=0
Correy=0
Li=0
OTooley=0
csvpath=os.path.join("..","PyPoll.csv")
with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    #Count total votes
    for row in csvreader:
        total=total+1
        #Count votes for each candidate
        candidate.append(row[2])
        if row[2]=="Khan":
            Khan=Khan+1
        elif row[2]=="Correy":
            Correy=Correy+1
        elif row[2]=="Li":
            Li=Li+1
        elif row[2]=="O'Tooley":
            OTooley=OTooley+1
#The three following lines (32-34) of code were used to determine unique candidates 
#in the data set before analysis was performed
#myset=set(candidate)
#unique_candidates=list(myset)
#print(unique_candidates)
            
#Creating proportional measures for each candidate    
propKhan=round(Khan/total*100,0)
propCorrey=round(Correy/total*100,0)
propLi=round(Li*100/total,0)
propOTooley=round(OTooley*100/total,0)
totals_list=[Khan,Correy,Li,OTooley]
filler_candidatelist=["Khan","Correy","Li","O'Tooley"]
#List of tuple linking candidates to their vpeoportion of votes received
results=[(x,y)for x,y in zip(filler_candidatelist,totals_list)]
#List comprehension to determine the the winner
winner=[x for x, y in results if y==max(totals_list)]
#Printing results
print("Elecetion Results")
print("----------------------------")
print("Total votes: "+str(total))
print("----------------------------")
print("Khan: "+str(propKhan)+"%"+" ("+str(Khan)+")")
print("Correy: "+str(propCorrey)+"%"+" ("+str(Correy)+")")
print("Li: "+str(propLi)+"%"+" ("+str(Li)+")")
print("O'Tooley: "+str(propOTooley)+"%"+" ("+str(OTooley)+")")
print("----------------------------")
print("Winner: "+str(winner))
#Writing the output to a text file
sys.stdout = open('pypolllog.txt', 'w')
print("Election Results")
print("----------------------------")
print("Total votes: "+str(total))
print("----------------------------")
print("Khan: "+str(propKhan)+"%"+" ("+str(Khan)+")")
print("Correy: "+str(propCorrey)+"%"+" ("+str(Correy)+")")
print("Li: "+str(propLi)+"%"+" ("+str(Li)+")")
print("O'Tooley: "+str(propOTooley)+"%"+" ("+str(OTooley)+")")
print("----------------------------")
print("Winner: "+str(winner))
sys.stdout.close()
sys.stdout=sys.__stdout__