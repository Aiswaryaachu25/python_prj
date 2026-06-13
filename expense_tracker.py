import csv

expense=[]

try:
    with open("expense.csv","r") as f:
        reader=csv.DictReader(f)
        for i in reader:
         expense.append([i["item"],i["amount"]])
except:
   pass

while(True):
    print("\n\tEnter your choice\n\n1.➕ ADD \t2.🪟 VIEW \t3.🗑️ remove \t 4.💸Total expense\n\n")
    choice = int(input("enther your choice number\t"))

    if(choice==1):
       item=input("\nenter the item\t")
       amt=float(input("\nenter the amount\t"))
       expense.append([item,amt])
    elif(choice==2):
       for i,item in enumerate(expense):
            print(i+1,item)
    elif(choice==3):
        print(expense)
        removed=input("enter the item to be removed\t")
        for i in expense:
            if i[0] == removed:
                expense.remove(i)
                break
    elif(choice==4):
        total=0
        for i in expense:
            total=total+float(i[1])
        print("total expense is ",total)
    else:
        print("INVALID ENTRY")
    
    y=input("\t\ndo you want to continue(y/n)\t")
    if(y=='n'):
        with open("expense.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["item", "amount"])  
            for i in expense:
                writer.writerow(i)
        print("\nEXITING\n")
        break