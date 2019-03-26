#PyBank
import csv
import os
import sys
csvpath=os.path.join("..","PyBank.csv")
months=[]
profit_loss=[]
profit_loss_one_forward=[]
total=0
month_change=[]
with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csvheader=next(csvfile)
    for row in csvreader:
        destring_value=int(row[1])
        months.append(row[0])
        month_change.append(row[0])
        total= total + destring_value
        profit_loss.append(destring_value)
        profit_loss_one_forward.append(destring_value)
    del(profit_loss_one_forward[0])
    del(profit_loss[len(months)-1])
    del(month_change[0])
    change=[x - y for x, y in zip(profit_loss_one_forward,profit_loss)]
    change_total=sum(change)
    change_month_list=[(x,y) for x,y in zip (month_change,change)]
    maxdate=[x for x,y in change_month_list if y==max(change)]
    mindate=[x for x,y in change_month_list if y==min(change)]
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(len(months)))
    print("Total: "+"$"+str(total))
    print("Average Change: "+"$"+str(round(change_total/(len(months)-1),2)))
    print("Greatest Increase in profits: "+str(maxdate)+"$"+str(max(change)))
    print("Greatest Decrease in profits: "+str(mindate)+"$"+str(min(change)))
sys.stdout = open('pybanklog.txt', 'w')
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(len(months)))
print("Total: "+"$"+str(total))
print("Average Change: "+"$"+str(round(change_total/(len(months)-1),2)))
print("Greatest Increase in profits: "+str(maxdate)+"$"+str(max(change)))
print("Greatest Decrease in profits: "+str(mindate)+"$"+str(min(change)))
sys.stdout.close()
