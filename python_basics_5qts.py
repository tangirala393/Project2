

def python_basics():
    
    print('''\n***********************************************************************************************************************
    The quiz contains 5 questions and there is no time limit. You’ll get 5 points for each correct answer.
    At the end of the quiz, you’ll receive a total score. The maximum score is 100%. Good luck!

***********************************************************************************************************************''')
    print('''\nHere you have two patterns to go:
          1 : Multiple choice pattern
          2 : fill in the blanks ''')
    
    pattern_ip = int(input("Select Choice of pattern:"))
    if pattern_ip==1:
        print("\nSelected Multiple Choice Pattern")
        import python_basics_5qts as YY
        print(YY.python_basics_5que())
    elif pattern_ip==2:
        print("Selected fill in the Blanks Pattern")
        import python_basics_5qts as YY
        print(YY.python_basics_blanks())






def python_basics_5que():
    dict_Pybasics = {"question1": {"question":"What is a correct syntax to output 'Hello World' in Python?",
                      "options":["a)p('Hello World;')","b)print('Hello World')","c)Print('Hello World')","d)None"]},
        "question2": {"question":"Which one is NOT a legal variable name?",
                      "options":["a)my-var","b)my_var","c)Myvar","d)_myvar"]},
        "question3": {"question":"What is the correct file extension for Python files?",
                      "options":["a) .py","b) .python","c) .pt","d) .pty"]},
        "question4": {"question":"How do you create a variable with the floating number 2.8?",
                      "options":['a) x = float(2.8)','b) x = 2.8','c) Both answers are correct']},
        "question5": {"question":"What is the correct way to create a function in Python?",
                      "options":['a) function myfunction():','b)def Myfunction():','c)create Myfunction']}}

    num_of_que=5
    L1 = list()
    L2 = list()
    while True:       
        for i in dict_Pybasics:
            #print(i)
            

            if i=="question1":
                print(dict_Pybasics[i])
                result1 = input("\nans:")
                if result1 == "b":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i=="question2":
                print(dict_Pybasics[i])
                result1 = input("\nans:")
                if result1 == "b":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i=="question3":
                print(dict_Pybasics[i])
                result1 = input("\nans:")
                if result1 == "a":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i=="question4":
                print(dict_Pybasics[i])
                result1 = input("\nans:")
                if result1 == "b":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i=="question5":
                print(dict_Pybasics[i])
                result1 = input("\nans:")
                if result1 == "b":
                    L1.append(i)
                else:
                    L2.append(i)
    
       
        break
    
            
    print("\nNumber of correct answers:",L1)
    print("\nNumber of in-correct answers:",L2)
    k=len(L1)*5
    print('Congratulations Your Score is {} out of {}'.format(k,25))

    


def python_basics_blanks():
    num_of_que=5
    L1 = list()

    L2 = list()
    while True:
        for i in range(1,num_of_que+1):
            if i==1:
                print("\n1)What is the Symbol for Comparision Operator in Python   _______")
                result1 = input("\nans:")
                if result1 == "==":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i==2:
                print('''\n2)Check if "apple" is present in the fruits set.
        \nfruits = {"apple", "banana", "cherry"}
        if "apple" ____ fruits:
        print("Yes, apple is a fruit!")   ''')

                result1 = input("\nans:")
                if result1 == "in":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i==3:
                
                print('''\n3)Print i as long as i is less than 6.
        \ni = 1
        _____ i < 6 :
        print(i)
        i += 1''')
                result1 = input("\nans:")
                if result1 == "while":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i==4:
                print('''\n4)What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
        \nclass  _______________:''')
                result1 = input("\nans:")
                if result1 == "Student(person)":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i==5:
                print('''\n5)What is the correct syntax to import a module named "mymodule"?
        \n _______ mymodule''')
                result1 = input("\nans:")
                if result1 == "import":
                    L1.append(i)
                else:
                    L2.append(i)

        break
    print("\nNumber of correct answers:",L1)
    print("\nNumber of in-correct answers:",L2)
    k=len(L1)*5
    print('Congratulations Your Score is {} out of {}'.format(k,25))

     

                
    


























