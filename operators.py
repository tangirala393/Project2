



def py_operators():
    
    print('''\n***********************************************************************************************************************
    The quiz contains 5 questions and there is no time limit. You’ll get 5 points for each correct answer.
    At the end of the quiz, you’ll receive a total score. The maximum score is 100%. Good luck!

***********************************************************************************************************************''')

    dict_Operators = {"Q1":{"Que1)":"x=5   print(not(x > 3 and x < 10))","options":["a)True","b)False"]},
                  "Q2":{"Que2)":"x = 5   x%=3    print(x)=","options":["a)2 ","b)3.0","c=3","d)2.0"]},
                  "Q3":{"Que2)":"print(9//2) ","options":["a)4.5 ","b)3","c)4","d)None"]},
                  "Q4":{"Que2)":"Which operator is overloaded by the or() function?","options":["a)|| ","b)|","c) //","d)/"]},
                  "Q5":{"Que2)":"x = 5  then print(x > 3 and x < 10) ","options":["a)True ","b)T","c) False","d) F"]}}


    num_of_que=5
    L1 = list()
    L2 = list()
    while True:       
        for i in dict_Operators:
            if i=="Q1":
                print(dict_Operators[i])
                result1 = input("\nans:")
                if result1 == "b":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i=="Q2":
                print(dict_Operators[i])
                result1 = input("\nans:")
                if result1 == "d":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i=="Q3":
                print(dict_Operators[i])
                result1 = input("\nans:")
                if result1 == "c":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i=="Q4":
                print(dict_Operators[i])
                result1 = input("\nans:")
                if result1 == "b":
                    L1.append(i)
                else:
                    L2.append(i)
            elif i=="Q5":
                print(dict_Operators[i])
                result1 = input("\nans:")
                if result1 == "a":
                    L1.append(i)
                else:
                    L2.append(i)
        break
            
    print("\nNumber of correct answers:",L1)
    print("\nNumber of in-correct answers:",L2)
    k=len(L1)*5
    print('Congratulations Your Score is {} out of {}'.format(k,25))







