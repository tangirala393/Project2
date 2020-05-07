
###############-----------------------------------------------Module for Python_operators------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@
def py_operators():
    
    print('''\n***********************************************************************************************************************
    The quiz contains 5 questions and there is no time limit. You’ll get 5 points for each correct answer.
    At the end of the quiz, you’ll receive a total score. The maximum score is 100%. Good luck!

***********************************************************************************************************************''')

    dict_Operators = {"question1":{"question":"\n1)x=5   print(not(x > 3 and x < 10))","options":["a)True","b)False"],"answer":"b"},
                  "question2":{"question":"\n2)x = 5   x%=3    print(x)=","options":["a)2 ","b)3.0","c=3","d)2.0"],"answer":"d"},
                  "question3":{"question":"\n3)print(9//2) ","options":["a)4.5 ","b)3","c)4","d)None"],"answer":"c"},
                  "question4":{"question":"\n4)Which operator is overloaded by the or() function?","options":["a)|| ","b)|","c)//","d)/"],"answer":"b"},
                  "question5":{"question":"\n5)x = 5  then print(x > 3 and x < 10) ","options":["a)True ","b)T","c)False","d) F"],"answer":"a"}}


    num_of_que=5
    L1 = list()
    L2 = list()
    while True:       
        for i in dict_Operators:
            if i=="question1":
                print(dict_Operators["question1"]["question"])
                for j in dict_Operators["question1"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Operators["question1"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question2":
                print(dict_Operators["question2"]["question"])
                for j in dict_Operators["question2"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Operators["question2"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)

            elif i=="question3":
                print(dict_Operators["question3"]["question"])
                for j in dict_Operators["question3"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Operators["question3"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question4":
                print(dict_Operators["question4"]["question"])
                for j in dict_Operators["question4"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Operators["question4"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
            elif i=="question5":
                print(dict_Operators["question5"]["question"])
                for j in dict_Operators["question5"]["options"]:
                    print(j)
                user_answer = input("\nans:")
                if user_answer == dict_Operators["question5"]["answer"]:
                    print("\nCorrect answer")
                    L1.append(i)
                else:
                    print("\nIn-Correct answer")
                    L2.append(i)
        break
            
    print("\nNumber of correct answers:",L1)
    print("\nNumber of in-correct answers:",L2)
    k=len(L1)*5
    print("\nCongratulations Your Score is {} out of {}".format(k,25))

###############-----------------------------------------------End of the Module------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@











