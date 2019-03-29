#PyBank
#Import Dependencies
import csv
import os
import sys
#Create necessary variables
csvpath=os.path.join("..","PyBank.csv")
months=[]
profit_loss=[]
profit_loss_one_forward=[]
month_change=[]
total=0
with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csvheader=next(csvfile)
    for row in csvreader:
        #python reads thr profit/loss column as a string so I am changing it to an integer
        destring_value=int(row[1])
        #populating the lists I created
        months.append(row[0])
        month_change.append(row[0])
        profit_loss.append(destring_value)
        profit_loss_one_forward.append(destring_value)
        #Caluclating total profit
        total= total + destring_value
    #Deleting the first entry of this list to do a pseudo first differences opperation
    del(profit_loss_one_forward[0])
    #Deleting the last entry of this list to do a pseudo first differences opperation
    del(profit_loss[len(months)-1])
    #Deleting the first entry of this list to beable to zip it together with the changes of profit/loss
    del(month_change[0])
    #populating the list for changes in profit/loss
    change=[x - y for x, y in zip(profit_loss_one_forward,profit_loss)]
    #summing the values in the list to be able to take the average
    change_total=sum(change)
    #combining the altered month list and the change list into a list of tuples so they are linked
    change_month_list=[(x,y) for x,y in zip (month_change,change)]
    #using a list comprehension to find the date of the greatest profit
    maxdate=[x for x,y in change_month_list if y==max(change)]
    #using a list comprehension to find the date of the greatest loss
    mindate=[x for x,y in change_month_list if y==min(change)]
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(len(months)))
    print("Total: "+"$"+str(total))
    print("Average Change: "+"$"+str(round(change_total/(len(months)-1),2)))
    print("Greatest Increase in profits: "+str(maxdate)+"$"+str(max(change)))
    print("Greatest Decrease in profits: "+str(mindate)+"$"+str(min(change)))
    #Print to text file
    sys.stdout = open('pybanklog.txt', 'w+')
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(len(months)))
    print("Total: "+"$"+str(total))
    print("Average Change: "+"$"+str(round(change_total/(len(months)-1),2)))
    print("Greatest Increase in profits: "+str(maxdate)+"$"+str(max(change)))
    print("Greatest Decrease in profits: "+str(mindate)+"$"+str(min(change)))
    sys.stdout.close()
    sys.stdout=sys.__stdout__
    #IDE needs to be restarted after running code



    
    
