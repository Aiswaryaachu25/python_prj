while(True):
    num1=float(input("enter first number\t"))
    num2=float(input("enter the next number\t"))

    choose=input("enter a symbol( + , - , / , * , ** , %\n)")

    if(choose=="+"):
            print("result is --",num1+num2)
    elif(choose=="-"):
            print("result is --",num1-num2)
    elif(choose=="/"):
            print("result is --",num1/num2)
    elif(choose=="*"):
            print("result is --",num1*num2)
    elif(choose=="**"):
            print("result is --",num1**num2)
    elif(choose=="%"):
            print("result is --",num1%num2)
    else:
           print("INVALID ENTRY")
    
    y=input("\ndo u want to continue(y/n)\n")
    if(y=="n"):
       break