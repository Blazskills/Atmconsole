import uuid

def print_menu_start():
     print("""
           Welcome To Temmy's Bank:
           Choose an option:
           1. Login
           2. Register
           """
           )
def print_menu_grant():
     print("""
           Welcome To Temmy's Bank:
           Choose an option:
           1. View Balance
           2. Withdraw
           3. Deposit Cash
           4. Exit
           """
           )



granted = False
def grant():
    global granted
    granted = True
    


def  grant_user(name,password,balance,accountNumber):
        useroption = input("Enter your option: ")
        if useroption == "1":
            print(f"Dear {name} your account balance is {balance}")
            print_menu_grant()
            grant_user(name,password,balance,accountNumber)
        if useroption == '2':
            userdraw = input("Enter the amount you want to withdraw : ")
            if userdraw.strip().isdigit():
                if userdraw < balance:
                    userdraw=int(userdraw)
                    balance = int(balance)
                    response= balance-userdraw
                    print(f'Kindly take your cash. Your balance is {response}')
                else:
                    print('Insufficient balance. Kindly fund your account')
                    grant_user(name,password,balance,accountNumber) 
            elif not userdraw.strip().isdigit():
                print('something went wrong, kindly ensure you inputted a valid integer (0-9)')
                print_menu_grant()
                grant_user(name,password,balance,accountNumber)   
        if useroption == '3':
                userdeport = input("Enter the amount you want to withdraw : ")
                if userdeport.strip().isdigit():
                        userdeport=int(userdeport)
                        if userdeport < 1:
                            print(f'oop {name}, you can not add zero to your account nah')
                            grant_user(name,password,balance,accountNumber) 
                        newbalance=userdeport + int(balance)
                        print(f' Successful Deposited {userdeport}. Your new balance is {newbalance}')
        if useroption == '4':
            exit()
                            
                
                
        #            for i in file:
        #  name,password,balance,accountNumber = i.split(",")
        #  password = password.strip()
                
                
                #                  for idx, item in enumerate(alist):
#    if 123 in item:
#        alist[idx] = 2014
        
                
                
                
        # if useroption == '3':
        #         userdeport = input("Enter the amount you want to withdraw : ")
        #         if userdeport.strip().isdigit():
        #              if userdeport < 1: 
        #                  print('you can not add zero to your account')
        #                  grant_user(name,password,balance,accountNumber) 
                         
                
                
                
                
                
                
                
            # if userdraw > balance:     
            #     userdraw=int(userdraw)
            #     balance = int(balance)
            #     print(userdraw)
            #     print(balance)
            #     print(balance-userdraw)
            # print('something went wrong, kindly ensure you inputted a valid integer (0-9)')
                
            # successdraw= int(userdraw - balance)
            # print(successdraw)
            # print('something went wrong, kindly ensure you inputted a valid integer (0-9)')
            

    # print('Insufficient balance. Kindly fund your account') 
# if userdraw.strip().isdigit() and 
# def  grant_user(name,password,balance,accountNumber):
#         print_menu_grant()
#         try: 
#             useroption = input("Enter your option: ")
#             if useroption == "1":
#                 print(f"Dear {name} your account balance is {balance}")
#             if useroption == '2':
#                 userdraw = input("Enter the amount you want to withdraw : ")
#                 userdraw=int(userdraw)
#                 if userdraw > balance:
#                     print('Insufficient balance. Kindly fund your account')    
#                 userdraw=int(userdraw)
#                 balance = int(balance)
#                 print(userdraw)
#                 print(balance)
#                 print(balance-userdraw)
#                 # successdraw= int(userdraw - balance)
#                 # print(successdraw)
#         except:
#                 print('something went wrong, kindly ensure you inputted a valid integer (0-9)')
#                 grant_user(name,password,balance,accountNumber)


   
def login(name,password):
    success = False
    file = open("user_detail.txt","r")
    for i in file:
         name,password,balance,accountNumber = i.split(",")
         password = password.strip()
         if(name==name and password==password):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        print_menu_grant()
        print("\nYour account number is:",accountNumber)
        print("Your account balance is: #.",balance)
        grant_user(name,password,balance,accountNumber)
    else:
        print("wrong user name or password")
        grant_user(name,password,balance,accountNumber)
        
    #   Balzskills,Temitope001@@,2000,cfef4235ce4641008e4ce793d7ad238c
      
# """
#            Welcome To Temmy's Bank:
#            Choose an option:
#            1. View Balance
#            2. Withdraw
#            3. Close Account
#            4. Deposit Cash
#            """
           
           
#                  for idx, item in enumerate(alist):
#    if 123 in item:
#        alist[idx] = 2014
        
        
def register(name,password,accountNumber,balance):
    file = open("user_detail.txt","a")
    file.write("\n"+name+","+password+","+balance+","+accountNumber)
    grant()
    

    
# check if username and password is correct also check the number of login
def access(option):
    global name,password,accountNumber
    if(option=="1"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        name = input("Enter your name: ")
        balance = (input("fund your account: "))
        password = input("Enter your password: ")
        accountNumber = uuid.uuid4().hex
        register(name,password,accountNumber,balance)
        

def begin():
    global option
    print_menu_start()
    option = input("Press 1 to login or Press 2 to Register (1 for Login,2 for Reg): ")
    if(option!="1" and option!="2"):
        begin()
        
begin()
access(option)

if(granted):
    print_menu_grant()
    useroption = input("Enter your option: ")
    if useroption == "1":
        print(f"Dear {name}")


# """
#            Welcome To Temmy's Bank:
#            Choose an option:
#            1. View Balance
#            2. Deposit Cash
#            3. Close Account
#            4. Withdraw
#            """
           
           
           
           
           
           
        #     file = open("user_detail.txt","r")
        # for data in file:
        #     a,b,c,d = data.split(",")
        #     b = b.strip()
        #     if(a==name and b==password):
        #      success = True
        
        
        
