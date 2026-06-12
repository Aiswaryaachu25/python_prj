print("\n\tEnter your choice\n\n1.➕ ADD \t2. 🗑️ DELETE \t3. 🪟 VIEW\n\n")
list_of_task=[]
try:
    with open("tasks.txt","r") as f:
        for i in f:
            list_of_task.append(i.strip())
except:
    pass
while(True):
    choice=int(input("\nenter your choice\t"))
    if(choice==1):
        task=input("\nenter your task\t")
        list_of_task.append(task)
    elif(choice==2):
        print(list_of_task)
        removed=input("\nenter the task to be removed\t")
        list_of_task.remove(removed)
    elif(choice==3):
        for i,task in enumerate(list_of_task):
            print(i+1,task)
    else:
        print("INVALID ENTRY")
    y=input("\n\tdo you want to continue(y/n)\t")
    if(y=='n'):
        with open('tasks.txt',"w") as f:
            for i in list_of_task:
                f.write(i+"\n")
        break
