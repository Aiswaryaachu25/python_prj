import csv

right=0
wrong=0
with open("questions.csv","r") as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i["Question"])
        ans=input("\nenter the answer\t")
        if(ans.lower()==i["Answer"].lower()):
            right=right+1
            print("\nRIGHT!!!🎉\n")
        else:
            wrong=wrong+1
            print("\nO O WRONG😔\n")

print("Total score = ",right,"/",right+wrong)