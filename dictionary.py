# Write a python program for contact tracing:


# Display a menu
print('\n \n')
print("                                      ===================== \033[01mCONTACT TRACING MENU\33[0m ========================")
print()
print("                                                         [1] Add and Informantions")
print("                                                         [2] Search an Informations")
print("                                                         [3] Exit Program")
print()
print("                                      ===================================================================")

# Dictionary   
info  = {}

# Ask User for input 
while True:
    print('\n \n')
    user_in = int(input("                                          \033[32mAnnyeonghaseyo, Dear User! What do you want to do? [1-3] :\33[0m "))
    print('\n \n')

    
# Option 1 - Add an Item from user
    if user_in == 1:
        add_in= int(input("                                                  \033[32m \033[01m How Many Infos do you want to Add?:\33[0m "))  
        print('\n \n')
        u_name= input("   \033[01mKindly input your Full Name:\33[0m ").title()
        print("")
        u_age=str(input("   \033[01mKindly input your Age:\33[0m "))
        print()
        u_gender= str(input("   \033[01mKindly input your Gender (F/M):\33[0m ")).title()
        print()
        u_status=input("  \033[01m Kindly input your Status:\33[0m ").title()
        print()
        u_num = str(input("   \033[01mKindly input your Phone Number:\33[0m ")).title()
        print()
        u_add = input("   \033[01mKindly input your Address:\33[0m ").title()
        print()
        u_occu = (input("   \033[01mKindly input your Occupation:\33[0m " )).title()
        print ('\n')
        print("=======================================================================================================================================================================")
        print('\n')
        print ("                                                       \033[01mYour Information has been saved!\33[0m ")
        print('\n')
        print("=======================================================================================================================================================================")
        print ('\n \n')

        info[u_name]= [u_age,  u_gender, u_status, u_num, u_add, u_occu]
        new_info = info
        
        
             
# Option 2
    elif user_in == 2:
        print("                                                    \033[32m \033[01m Information you want to search?:\33[0m ")  
        search= input().title()
        resp=info.get(search)
        for info1 in resp, new_info:
            print()
            print(str("\033[01m\033[92mAge:\33[0m" ) + info1[0])
            print()
            print(str("\033[01m\033[92mGender:\33[0m ") + info1[1])
            print()
            print(str("\033[01m\033[92mStatus:\33[0m ") + info1[2])
            print()
            print(str("\033[01m\033[92mPhone Number:\33[0m ") + info1[3])
            print()
            print(str("\033[01m\033[92mAddress: \33[0m") + info1[4])
            print()
            print(str("\033[01m\033[92mOccupation:\33[0m ") + info1[5])
            print
            break
        
        

# Option 3
    elif user_in == 3 :
        user_in= input("Do you wish to exit? (y/n) : ")
        print()
        if user_in == "y":
            print("Thank You for your Participation")  
            print()         
            print("Have a Great Day!")
            print
            break
        elif user_in == "n" :
            print()
            continue
    else:
        print("\033[31m                                                         You must choose between 1-3 only\33[0m")
        
        

