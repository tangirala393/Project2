



print("\n**********************************************************************************************************************************")
print("*                                             Welcome to PYTHON QUIZ PROGRAM                                                     *")
print("**********************************************************************************************************************************")




####------------------------------------------------------------------------------------------------------------####

def func():

    
    
        print('''\nKindly select which module to go for Quiz
                \n
                  1 : Python Basics
                  2 : Python Operators ''')
        while True:

                select_prog = int(input("\nSelect anyone of above list:"))

                if select_prog == 1:
                    print("\nyou are selected Python Basics Quiz ")
                    import python_basics_10qts as i1
                    #########---------------------------------------------calling Python basics Questions ----------------------##################
                    print(i1.python_basics())
                    
                    
                elif select_prog == 2:
                    print("\nyou are selected Python Operators Quiz ")
                    import operators as i2
                    #########---------------------------------------------calling Python Operator Questions ----------------------##################
                    print(i2.py_operators())
                    
                else:
                    print("\nSelected wrong option kindly select Proper availability Option")
                break   
                

def main():
    func()
   
main()
####---------------------------------------------------------------Next Iteration-----------------------------------------------------####
exit_ip=input("Select option to Go for next test/Exit   Y/N:")
if exit_ip=='Y':
    func()
else:
    print("#########*******THANK YOU VISIT AGAIN-------##########")


####----------------------------------------------------------------END OF PROGRAM ----------------------------------------------------------####
    
    










