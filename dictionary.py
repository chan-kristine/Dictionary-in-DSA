# Write a python program for contact tracing:


# Dictionary   
info  = {}

# Display a menu
print('\n \n')
print("                                      ===================== CONTACT TRACING MENU ========================")
print()
print("                                                         [1] Add and Informantions")
print("                                                         [2] Search an Informations")
print("                                                         [3] Exit Program")
print()
print("                                      ===================================================================")



# Ask User for input 
while True:
    print('\n \n')
    user_in = int(input("                                          Annyeonghaseyo, Dear User! What do you want to do? [1-3] : "))
    print('\n \n')

    
# Option 1 - Add an Item from user
    if user_in == 1:
        add_in= int(input("                                                    How Many Infos do you want to Add?: "))  
        print('\n \n')
        u_name= input("   Kindly input your Full Name: ").title()
        print("")
        u_age=str(input("   Kindly input your Age: "))
        print()
        u_gender= str(input("   Kindly input your Gender (F/M): ")).title()
        print()
        u_status=input("   Kindly input your Status: ").title()
        print()
        u_num = str(input("   Kindly input your Phone Number:")).title()
        print()
        u_add = input("   Kindly input your Address: ").title()
        print()
        u_occu = (input("   Kindly input your Occupation:" )).title()
        print ('\n')
        print ("                                                       Your Information has been saved!")
        print('\n')
        print("=======================================================================================================================================================================")
        print ('\n \n')

        info[u_name]= [u_age,  u_gender, u_status, u_num, u_add, u_occu]
        new_info = info
        
             
# Option 2
    elif user_in == 2:
        print("                                                    Information you want to search?: ")  
        search= input().title()
        resp=info.get(search)
        print("                                                      Information of" , search)
        for info1 in resp, new_info:
            print(str("Age:" ) + info1[0])
            print()
            print(str("Gender: ") + info1[1])
            print()
            print(str("Status: ") + info1[2])
            print()
            print(str("Phone Number: ") + info1[3])
            print()
            print(str("Address: ") + info1[4])
            print()
            print(str("Occupation: ") + info1[5])
            print
            break
        
        

# Option 3
    elif user_in == 3 :
        print("Thank You for your Participation")
        print("Have a Great Day!")
    
    else:
        print("You must choose between 1-3 only")
        
        


