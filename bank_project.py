print("=============================================")


CustomerNames =['kiran','renuka','krishna','sagar','amruth']
Customerpins =['1234','2345','3456','4567','5678']
Customerbalances =[10000,23000,34000,44000,15000]
Deposition=0
Withdrawl=0
balance=0
counter_1=0
counter_2=6
i=0

#this statement below helpsthe program to run continuosly
while True:
    #os.system("class")
    print("====================================")
    print("===welcome to  andhra  bank=========")
    print("************************************")
    print("=<<< 1.open anew account  >>>>>++++=")
    print("=<<< 2.with draw money   >>>>>>=====")
    print("=<<<< 3.deposit money >>>>>>>>>======")
    print("=<<<< 4.check customer& balance>>>>>=")
    print("=<<<<5.exit&quit>>>>>>>>>>>>>>>=====")
    print("************************************")
    # the below number takes the choice number from the user 
    choiceNumber = input("select choice from the above numbers")
    if choiceNumber =="1":
        print("choice number 1 selected by the customer ")
        # the line below will take the no of  customers from the user 
        NOC = eval(input("number of customers :"))
        i = i + NOC
        # this if condition will shows the number of new account should be 5
        if i > 5:
            print("\n")
            print(" customer registration exceed reached or customer ")
            i=i-NOC
        else:
        # the while loop will run according to the no of students
            while counter_1 <= i:
                #these few lines will take the information and append the list
                name = input("please enter your full name:")  
                CustomerNames.append(name)
                pin = str(input("please enter your full password"))
                Customerpins.append(pin)
                balance = 0
                Deposition = eval(input("enter the amount of deposition :"))
                balance = balance + Deposition
                Customerbalances.append(balance)
                print("\nName",end=" ")
                print(CustomerNames[counter_2])
                print("pin",end=" ")
                print(Customerpins[counter_2])
                print("balances",end=" ")
                print(Customerbalances[counter_2],end=" ")
                print(" -/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 2
                print("your name is added to the customer system ")
                print("your pin is added to the customer pins")
                print(" your balnces is added to the customer balances")
                print("--- new account is created succcesfully---")
                print("\n")
                print("your name is available on the customer list ")
                print(CustomerNames)
                print("\n")
                print(" please remeber the name and pin")
                print("===============================")
                # this statement helps the user to get back the starting of program
        mainMenu = input("please press the enter key to go back and perform the operation")        
    elif choiceNumber == 2:
        j = 0   
        print("chpice number 2 is selected by the customer ")  
        # the while loop will prevent the using the user ,password ,crct or incrct      
        while j < 1:
            k = -1
            name = input("please enter the name :")
            pin = input(" please enter the pin ")
            # the while loop will keep the function running when the variable less than the customer s list 
            while k < len(CustomerNames)  - 1:
                k = k + 1
                # the two if condition matches the user  ame and password 
                if name == CustomerNames[k]:
                    if pin == Customerpins[k]:
                        j = j + 1
                        # these few statements will show the balance of the list
                        print(" your current balance :",end=" ")
                        print(Customerbalances[k],end="")
                        print("-/Rs\n")
                        balance = (Customerbalances[k])
                        # statement below should take the amount with draw from the user
                        withdrawl = eval(input("enter the with drawl amount : "))
                        # the if condition would look the wheater the withdrawn amount is present or not in the account 
                        if withdrawl > balance: 
                            # this statement would take adeposition from customer 
                            deposition = eval(input("please deposit a higher value because your balance mentioned is not enough "))
                            # will update the user credintals and the user 
                            balance = balance + deposition
                            print("your current balance",end=" ")
                            print(balance,end=" ")
                            print('\n')
                            print("------ with drawl succcessfull -------")
                            Customerbalances[k] == balance
                            print("your new balance:",balance,end=" ")
                            print("-/Rs\n\n")
                        else:
                            # customer entered if the  withdrawl amount should be greater than balancce present in the acoount
                            balance= balance- withdrawl
                            
                            print("\n")
                            print("with drawl succcessfull")
                            Customerbalances[k]=balance
                            print("your new balance:",balance,end=" ")
                            print("-/Rs\n\n")
            if j <1 :
                # the if condition would work on the user name and password                 
                print("your name and pin doesnt match ")
                break
            # helps the user to restart the program 
        mainMenu=input("please press the enter key to go back and perform the operation") 
    elif choiceNumber== "3" :
        print("choice number 3 is selected by the customer  ")
        n = 0
        # below while loop will work when the user name and pi n is wrong 
        while n < 1:
            k = -1
            name=input("enter the name")
            pin=input("enter the pin ") 
            # the while loop below will keep the function running to find the correct user
            while k < len(CustomerNames) - 1:
                k=k+1
                # the two if conditions will find the user and pin is correct    
                if name == CustomerNames[k]:
                    if pin == Customerpins[k]:
                        n = n + 1
                        # these statements below will show the customer list values and update depositin values 
                        print("your current balance",end ="")
                        print(Customerbalances[k],end=" ")
                        print("\n")
                        print("-/Rs")
                        balance = (Customerbalances[k])
                        # This statement below takes the depositionn from the customer.
                        Deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition # 1000+500=1500
                        Customerbalances[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("choice number 4 is selected by the customer ")
        k = 0
        print("cusromer names and list names mentioned below ")
        print("\n")
        while k <= len(CustomerNames) - 1:
            print("->.Customer =", CustomerNames[k])
            print("->.Balance =", Customerbalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choiceNumber == "5":
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")


























































