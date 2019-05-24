'''
Programmer name: Kee Hwan Kim
Description: 
  - This program simulate a banking application.
Date: 12/4/2018
'''

def ReadingFile():      #Function for reading a file
    global Customers, Balances    #Declare these lists global
    Customers = []          #Initializing it to update 
    Balances = []           #Initializing it to update
    fileRead = open("UserInformation.txt", 'r')    #To open the file named 'UserInformation.txt' as reading
    fileRead.readline()      #The first line in the file is skipped
    fileRead.readline()      #The second line in the file is skipped
    for row in fileRead:     
       cols = row.split()
       Customers.append(cols[0])
       Balances.append(cols[1])
    fileRead.close()   

def WritingFile():      #Function for writing a file
    fileWrite =  open("UserInformation.txt", 'w')        #To open the file named 'UserInformation.txt' as writing
    fileWrite.write("userName   Balance \n")
    fileWrite.write("==========================\n")
    for i in range(len(Customers)):
        fileWrite.write(Customers[i] + '\t\t' + str(Balances[i]) + '\n' )
    fileWrite.close()    
    

def displayMenu():    #Function for displaying the menu
    print("Type D to diposit money\n")
    print("Type W to withdraw money\n")
    print("Type B to display Balance\n")
    print("Type C to change user, display user name\n")
    print("Type E to exit\n")
    
def validatingSelection():    #Function for validating the user's choice
    global selection       #To declare this variable global
    while (selection.upper() != 'D' and selection.upper() != 'W' and selection.upper() != 'B' and selection.upper() != 'C' and selection.upper() != 'E'):
        selection = input("Invalid choice! Please choose it again: ")
   
def Depositing(depAmount):    #Function for the user to deposit
    Balances[indexNumber] = int(Balances[indexNumber]) + depAmount
    WritingFile()           #To update the user's balance in the file
    print("Your new balance is $" + str(Balances[indexNumber]) + '\n')

def Balancing():    #Function for the user to see the balance
    ReadingFile()
    return Balances[indexNumber]
    
def Withdrawing(wdAmount):    #Function for the user to withdraw
    Balances[indexNumber] = int(Balances[indexNumber]) - wdAmount
    WritingFile()   #To update the user's balance in the file
    return Balances[indexNumber]
    
def vldAmount(amt):
    while amt <= 0 :
        amt = int(input("Please enter the positive amount: "))
    return amt    
    

Customers = []    #Initializing this list
Balances = []     #Initializing this list

ReadingFile()

userName = input("Please enter a user name: ")
while userName not in Customers:     #Validating the user name which the user have input using while loop
    userName = input("The user name is not correct. Please enter it again: ")

indexNumber = Customers.index(userName)    #To save the customer's index which the user have input
print('\n')     #To make one line space

displayMenu()
selection = input("Please choose one of these choices: ")
validatingSelection()

while (selection.upper() != 'E'):       #To iterate while loop until the user have choiced 'E' option
    if selection.upper() == 'D':        #In case the user have choiced a deposit option
        depositAmount = vldAmount(int(input("How much do you want to deposit? $")))
        
        ReadingFile()
        Depositing(depositAmount)
    
    elif selection.upper() == 'W':      #In case the user have choiced a withdraw option
        withdrawAmount = vldAmount(int(input("How much do you want to withdraw? $")))
        while withdrawAmount > int(Balancing()):    #To check the current balance is enough for withdrawing using while loopb
            withdrawAmount = vldAmount(int(input("Your balance is not enough. Please enter it again. $")))
        ReadingFile()    
        print("Your new balance is $" + str(Withdrawing(withdrawAmount)) + '\n') 
    
    elif selection.upper() == 'B':     #In case the user have choiced a balance option
        print("Your current balance is $" + Balancing() + '\n')
    
    elif selection.upper() == 'C':    #In case the user have choiced a change user name
        userName = input("Please enter another user name: ")
        while userName not in Customers:
            userName = input("The user name is not correct. Please enter it again: ")
        indexNumber = Customers.index(userName)
        print('\n')
        
    displayMenu()
    selection = input("Please choose one of these choices: ")
    validatingSelection()
    
 
    