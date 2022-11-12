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
        u_name= input("Kindly input your Full Name: ")
        u_age=str(input("Kindly input your Age: "))
        u_gender= str(input("Kindly input your Gender (F/M): "))
        u_status=input("Kindly input your Status: ")
        u_num = str(input("Kindly input your Phone Number:"))
        u_add = input("Kindly Put your Address: ")
        u_occu = (input("Kindly input your Occupation:" ))
        print ('\n')
        print ("                                                       Your Information has been saved!")
        print('\n')
        print("==========================================================================================================================================")
        print ('\n \n')

        info[u_name]= [u_age,  u_gender, u_status, u_num, u_add, u_occu]
        new_info = info
        
             
# Option 2
# Option 3
