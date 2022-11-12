# Write a python program for contact tracing:
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
print('\n \n')
user_in = int(input("                                          Annyeonghaseyo, Dear User! What do you want to do? [1-3] : "))
print('\n \n')


info= {}

# Option 1 - Add an Item 
if user_in == 1:
    add_in= int(input("                                                    How Many Infos do you want to Add?: "))  
    for i in range (add_in):
        key=input("                                                        What do you want to add: ")
        value=input("                                                      Enter your Information: ")
        info[key]= value
        print ('\n')
        print ("                                                       Your Information has been saved!")
        print ('\n')
        print(info)
        print('\n')
        print("==========================================================================================================================================")
        print ('\n \n')
    
# Option 2
# Option 3

