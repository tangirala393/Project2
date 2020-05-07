
############-------------------------------------------------------Module for Python_Basics--------------------------------------------@@@@@@@@@@@@
def python_basics():
    
    print('''\n***********************************************************************************************************************
    The quiz contains 10 questions and there is no time limit. You’ll get 5 points for each correct answer.
    At the end of the quiz, you’ll receive a total score. The maximum score is 100%. Good luck!

***********************************************************************************************************************''')
    print('''\nHere you have two patterns to go:
          1 : Multiple choice pattern
          2 : fill in the blanks ''')
    
    pattern_ip = int(input("Select Choice of pattern:"))
    if pattern_ip==1:
        print("\nSelected Multiple Choice Pattern")
        import python_basics_10qts as YY
        print(YY.python_basics_mul())
    elif pattern_ip==2:
        print("Selected fill in the Blanks Pattern")
        import python_basics_10qts as YY
        print(YY.python_basics_blanks())



############-----------------------------------------------Module for Python_Basics_Multiple choice pattern-------------------------------@@@@@@@@@@@@
def python_basics_mul():
    

    dict_Pybasics= {"question1": {"question":"\n1)What is a correct syntax to output 'Hello World' in Python?",
                                  "options":["a)p('Hello World;')","b)print('Hello World')","c)Print('Hello World')","d)None"],"answer":"b"},
                    
                    "question2": {"question":"\n2)Which one is NOT a legal variable name?",
                                  "options":["a)my-var","b)my_var","c)Myvar","d)_myvar"],"answer":"b"},
                    "question3": {"question":"\n3)What is the correct file extension for Python files?",
                                  "options":["a) .py","b) .python","c) .pt","d) .pty"],"answer":"a"},
                    "question4": {"question":"\n4)How do you create a variable with the floating number 2.8?",
                                  "options":['a) x = float(2.8)','b) x = 2.8','c) Both answers are correct'],"answer":"b"},
                    "question5": {"question":"\n5)What is the correct way to create a function in Python?",
                                  "options":['a) function myfunction():','b)def Myfunction():','c)create Myfunction'],"answer":"b"},
                    "question6": {"question":"\n6)Bitwise _________ gives 1 if either of the bits is 1 and 0 when both of the bits are 1",
                                  "options":["a) OR ","b)AND ", "c) XOR ","d)NOT"],"answer":"a"},
                    "question7": {"question":"\n7)What will be the output of the following Python expression?  4^12 ",
                                  "options":["a) 2 ","b)4 ", "c) 8 ","d)12"],"answer":"c"},
                    "question8": {"question":"\n8)What will be the output of the following Python expression?   ~100?  ",
                                  "options":["a)101 ","b)-101  ", "c) 100 ","d)-100"],"answer":"b"},
                    "question9": {"question":"\n9)The one’s complement of 110010101 is: ?  ",
                                  "options":["a)001101010 ","b)110010101  ", "c)001101011","d) 110010100"],"answer":"a"},
                    "question10": {"question":"\n10)What will be the value of the following Python expression?   bin(10-2)+bin(12^4)",
                                  "options":["a)0b10000 ","b) 0b10001000  ", "c)0b1000b1000","d)0b10000b1000"],"answer":"c"}}






    num_of_que=10
    L1 = list()
    L2 = list()
    while True:       
        for i in dict_Pybasics:

            if i=="question1":
                print(dict_Pybasics["question1"]["question"])
                for j in dict_Pybasics["question1"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question1"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question2":
                print(dict_Pybasics["question2"]["question"])
                for j in dict_Pybasics["question2"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question2"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)

            elif i=="question3":
                print(dict_Pybasics["question3"]["question"])
                for j in dict_Pybasics["question3"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question3"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question4":
                print(dict_Pybasics["question4"]["question"])
                for j in dict_Pybasics["question4"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question4"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question5":
                print(dict_Pybasics["question5"]["question"])
                for j in dict_Pybasics["question5"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question5"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question6":
                print(dict_Pybasics["question6"]["question"])
                for j in dict_Pybasics["question6"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question6"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question7":
                print(dict_Pybasics["question7"]["question"])
                for j in dict_Pybasics["question7"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question7"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question8":
                print(dict_Pybasics["question8"]["question"])
                for j in dict_Pybasics["question8"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question8"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(j)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question9":
                print(dict_Pybasics["question9"]["question"])
                for j in dict_Pybasics["question3"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question9"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question10":
                print(dict_Pybasics["question10"]["question"])
                for j in dict_Pybasics["question10"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Pybasics["question10"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)  
               
            
            
        break            
    print("\nNumber of correct answers:",L1)
    print("\nNumber of in-correct answers:",L2)
    k=len(L1)*5
    print("\nCongratulations Your Score is {} out of {}".format(k,50))
############-------------------------------------------------------End of the Module --------------------------------------------------------@@@@@@@@@@@@

        

############-------------------------------------------------------Module for Python_Basics_blanks--------------------------------------------@@@@@@@@@@@@
def python_basics_blanks():
    

    dict1_fill_blanks = {"question1":{"question":"\n1)What is the Symbol for Comparision Operator in Python   _______","answer":"=="},
                     "question2":{"question":'''\n2)Check if "apple" is present in the fruits set.
\nfruits = {"apple", "banana", "cherry"}
if "apple" ____ fruits:
    print("Yes, apple is a fruit!")''',"answer":"in"},
                     "question3":{"question":'''\n3)Print i as long as i is less than 6.
        i = 1
        _____ i < 6 :
             print(i)
             i += 1''',"answer":"while"},
                     "question4":{"question":"\n4)What is the correct syntax to create a class named 'Student' that will inherit properties and methods from a class named 'Person'?","answer":"Student(Person)"},
                     "question5":{"question":'''\n5)What is the correct syntax to import a module named "mymodule"?
_______ mymodule''',"answer":"import"}}





    num_of_que=5
    L1 = list()
    L2 = list()
    while True:
             
        for i in  dict1_fill_blanks:
            if i== "question1":
                print(dict1_fill_blanks["question1"]["question"])

                user_ans = input("\nans:")

                if user_ans == dict1_fill_blanks["question1"]["answer"]:
                    
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i== "question2":
                print(dict1_fill_blanks["question2"]["question"])

                user_ans = input("\nans:")

                if user_ans == dict1_fill_blanks["question2"]["answer"]:
                    
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i== "question3":
                print(dict1_fill_blanks["question3"]["question"])

                user_ans = input("\nans:")

                if user_ans == dict1_fill_blanks["question3"]["answer"]:
                    
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i== "question4":
                print(dict1_fill_blanks["question4"]["question"])

                user_ans = input("\nans:")

                if user_ans == dict1_fill_blanks["question4"]["answer"]:
                    
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i== "question5":
                print(dict1_fill_blanks["question5"]["question"])

                user_ans = input("\nans:")

                if user_ans == dict1_fill_blanks["question5"]["answer"]:
                    
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)

        break
    print("\nNumber of correct answers:",L1)
    print("\nNumber of in-correct answers:",L2)
    k=len(L1)*5
    print('Congratulations Your Score is {} out of {}'.format(k,25))
############-------------------------------------------------------End of the Module --------------------------------------------------------@@@@@@@@@@@@

     

                
    


























