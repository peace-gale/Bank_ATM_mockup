import random
import getpass
import datetime

allowedUsers = ['Mary','August','Xavier']
allowedPasswords = ['mary123', 'august123', 'xavier123']


#function for intro
def Welcome():
    print ("Welcome to Bank Zion \n")
    request()
    
def request():
    print ("Do you have a Bank Zion Account")
    account = int(input("1: Yes\n2: No \n"))
    
    if account == 1:
        login()
    elif account == 2:
       register()
    else:
       print ("======INVALID SELECTION. PLEASE TRY AGAIN======= \n")
       request()

#function to generate account number
def generate_account_number():
    return random.randrange(0000000000, 9999999999)

# function to register
def register():
    print ("===========REGISTRATION===========")
    
    email = input("Enter email address? \n")
    first_name = input("Enter first name? \n")
    last_name = (input("Enter last name? \n"))
      
    try:
       password = getpass.getpass("Create  password  \n")
    except Exception as error:
       print('ERROR', error)
    else:
       pass
    
    account_number = generate_account_number()

    print ("===========CONGRATULATIONS=========== \n")
    print ("Your account has been created successfully")
    print ("Please do not disclose your account password to anyone \n")
    print ("======================================== \n")
    print ("Here is your account number: %d" %account_number)
    print ("Thank you for banking with us")


def bankOperation():
        print( "1. Withdrawal")
        print( "2. Deposit")
        print( "3. Complaint")
        selectedoption = int(input("Choose your preffered option: "))
        if(selectedoption == 1):
             Withdrawal()
        elif(selectedoption == 2):
            Deposit()
        elif(selectedoption == 3):
            Complain()
        else:
            print("Invalid selection, try again")
             
def Withdrawal():
           amount = input( "How much would you like to withdraw?  ")
           print( "\n")
        #to check if input is intger
           if(amount.isnumeric()):
               print( "Take your cash")
           else:
            print( "***INVALID INPUT***")
            Withdrawal()

def Deposit():
          amount = input( "How much would you like to desposit?  ")
          print( "\n")
          if(amount.isnumeric()):
               print( "Your current balance is $%s" %amount)
          else:
            print( "***INVALID INPUT***")
            Deposit()
            
def Complain():
            Complain = input( "What issue will you like to report? \n")
            print( "\n")
            print("Thank you for contacting us")

def login():
    name = input("Enter Username \n")

    if(name in allowedUsers):
        password = input("Enter Password \n")
        Userid = allowedUsers.index(name)

        if(password == allowedPasswords[Userid]):
            Today = datetime.datetime.now()
            print( "\n")
            print( "DATE: %s"  %Today.date())
            print( "TIME: %s" %Today.hour, ":", Today.minute, ":", Today.second )
            print( "\n")
            print( "Welcome %s" %name)
            bankOperation()
        else:
            print("Incorrect password, try again")
    else:
        print("Name not found, Try again")
        login()


