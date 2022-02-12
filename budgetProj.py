# Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. 
# #These objects should allow for depositing and withdrawing funds from each category, 
# as well computing category balances and transferring balance amounts between categories”



from budget import Category
list1 = list()
list2 = list()
line = ""



print("WELCOME TO THE BUDGET MONITORING APP \n")

def input_category():

    catRunning = True

    while catRunning == True:
        print("Select Option       :")
        print("1 for Food          :")
        print("2 for Entertainent  :")
        print("3 for Utilities     :")
        print("4 for Clothing      :")
        print("5 for Travel        :")
        print("6 for Savings       :")
        print("E to Exit           :\n")

        category_request = input("Enter Selection:  ")
        if category_request in ["1", "2", "3", "4", "5", "6", "E"]:
             catRunning = False
        else:
             print("Print enter the correct category")
             
    return category_request
   

def translate_category(category_request):
    budcat =""
    list1 = list()
    if category_request == "1":
         budcat = Category("Food") 
    if category_request == "2":
         budcat = Category("Entertainment")
    if category_request == "3":
         budcat = Category("Travel")
    if category_request == "4":
        budcat = Category("clothing")
    if category_request == "5":
         budcat = Category("Savings")
    if category_request == "6":
        budcat = Category("Utilities")

    return budcat


def perform_action(budcat):

    actionReq = True

    while actionReq == True:
        print("Select Option       :")
        print("1 for Deposit       :")
        print("2 for Withdrawal    :")
        print("3 for Transer       :")
        print("E for Exit          :\n")

        action_request = input("Enter Selection:  ")
        if action_request in ["1", "2", "3", "E"]:
            actionReq = False
        else:
            print("Print enter thr correct category")

        
    if action_request == "1":
         dep_amount = input("Enter amount to deposit ")
         budcat.deposit(int(dep_amount))
         list1.append(budcat.name + " Deposit " + dep_amount + "\n") 
         #print(list1)

    if action_request == "2":
        wdr_amount = input("Enter amount to withdraw ")
        budcat.withdrawal(int(wdr_amount))
        list1.append(budcat.name + " Withdraw " +  wdr_amount + "\n")
        #print(budcat) 

    if action_request == "3":
        trans_amount = input("Enter amount to trnsfer ") 
        aaa = input_category()
        bbb = translate_category(aaa)
        budcat.transfer(int(trans_amount), bbb)
        list1.append(budcat.name + " Transfer " +  trans_amount +  " to food"  + "\n")
        
        
    return list1

run_this = True

while run_this == True:
    category_request = input_category()
    if category_request == "E":
        run_this == False
        break
    list_returned = translate_category(category_request)
    list_returned2 = perform_action(list_returned)
    list2 = list_returned2 
  
#PRINT TO FILE
line = ""
with open("budget_output.txt", "r") as myfile1:
    line = myfile1.read()
print(line)
myfile1.close()



myfile = open("budget_output.txt", "w")
for c in list2:
    myfile.write(c)
myfile.write(line)

myfile.close()



