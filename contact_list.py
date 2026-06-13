import csv

contact_list=[]
try:
    with open("contact_list.csv","r") as f:
        reader=csv.DictReader(f)
        for i in reader:
            contact_list.append(i)
except:
    pass

while(True):
    print("\n\t1.ADD\t2.VIEW\t3.SEARCH\t4.DELETE\t5.QUIT\t\n")
    choice=int(input("\nenter your choice no.  "))

    if(choice==1):
        name=input("\nenter the name\t")
        phone=int(input("\nenter the phone no.\t"))
        email=input("\nenter the email id\t")
        contact={"name":name,"phone":phone,"email":email}
        contact_list.append(contact)

    elif(choice==2):
        for i  in contact_list:
            print("name : ",i["name"],"\nphone : ",i["phone"],"\nemail : ",i["email"])
            print("\n\n")

    elif(choice==3):

            find=input("\nenter the name of contact to be searched\t")
            for i in contact_list:
                if(find==i["name"]):
                    print("name : ",i["name"],"\nphone : ",i["phone"],"\nemail : ",i["email"])
                    break
    elif(choice==4):
        for i,name in enumerate(contact_list):
                print(i+1,name["name"])
        removed=input("\nenter the name to be removed\t")
        for i in contact_list:
            if(removed == i["name"]):
                contact_list.remove(i)
                print("\n\tDELETED\n")
                break

    elif(choice==5):
        print("\nEXITING...\n")
        break
    else:
        print("\nINVALID ENTRY\n")
    
    y=input("\t\nDo you want to continuet(y/n)\t")
    if(y=="n"):
        with open("contact_list.csv","w") as f:
            writer=csv.writer(f)
            writer.writerow(["name","phone","email"])
            for i in contact_list:
                writer.writerow([i["name"],i["phone"],i["email"]])
        break
