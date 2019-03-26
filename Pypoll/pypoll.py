# PyPoll
import csv
import os
import sys
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
    for row in csvreader:
        total=total+1
        candidate.append(row[2])
        if row[2]=="Khan":
            Khan=Khan+1
        elif row[2]=="Correy":
            Correy=Correy+1
        elif row[2]=="Li":
            Li=Li+1
        elif row[2]=="O'Tooley":
            OTooley=OTooley+1
myset=set(candidate)
unique_candidates=list(myset)
print(unique_candidates)
propKhan=round(Khan/total*100,0)
propCorrey=round(Correy/total*100,0)
propLi=round(Li*100/total,0)
propOTooley=round(OTooley*100/total,0)
totals_list=[Khan,Correy,Li,OTooley]
filler_candidatelist=["Khan","Correy","Li","O'Tooley"]
results=[(x,y)for x,y in zip(filler_candidatelist,totals_list)]
winner=[x for x, y in results if y==max(totals_list)]
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
sys.stdout = open('pypolllog.txt', 'w')
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
sys.stdout.close()