def kbc():
    print("Welcome to kaun banega crorepati , the most popular game!!!   \n")
    print("There are four questions for you to win Rs.100000")
    print("There is a lifeline for you which helps to give answer for only one question")
    print("If you use lifeline for one question then you cannot use lifeline for next questions")
    print("There is no timelimit for questions")
    print("question for Rs.10000")
    question1 = "First question : which film won the most numbers of oscar awards in the year 2017"
    options1 = "1. Batman\n2. MoonLight\n3. Newton\n4. La La Land"
    print(question1)
    print(options1)
    lres1 =int( input("if you need lifeline enter 1 else enter 0 :"))
    if lres1 == 1:
         print(4)
         print("You won Rs.10000")
         print("question for Rs.50000")
         question2 = "Second question : Who was the first woman prime minister of India\n" 
         options2 = "1. Rukmini Devi Arundale\n2. Shakuntala Paranjpye\n3. Smt Indira Gandhi\n4. FathemaIsmail"
         print(question2)
         print(options2) 
         res2  = input("enter 1 or 2 or 3 or 4 for your answer:")
         if res2 == 3:
                 print("Correct Answer")
                 print("You won Rs.50000")
                 print("question for Rs.75000")
                 question3 =  "Third question : Who is the current chief minister of Goa?"
                 options3 = "1. Naveen Patnaik\n2. Raghubar Das\n3. Manohar Parrikar\n4. Shashi Tharoor"
                 print(question3)
                 print(options3)
                 res3 = input("enter 1 or 2 or 3 or 4 for your answer:")
                 if res3 == 3:
                    print("Correct Answer")
                    print("You Won Rs75000")
                    print("question for Rs.100000")
                    question4 = "Fourth question : On the reverse of which newly launched Indian currency note is the image of Sanchi Stupa printed\n"
                    options4 = "1. Rs.2000\n2. Rs.20\n3. Rs.200\n4. Rs.50"
                    print(question4)
                    print(options4)
                    res4  = input("enter 1 or 2 or 3 or 4 for your answer:")
                    if res4 == 3:
                        print("Correct Answer")
                        print("Congratulations......You Won Rs100000")
                    else:       
                        print("Oops! it was wrong answer.....")
                        print("Better Luck next time")    
                        print("You won Rs.0")
                 else:       
                     print("Oops! it was wrong answer.....")
                     print("Better Luck next time")
                     print("You won Rs.0")
         else:     
             print("Oops! it was wrong answer.....")
             print("Better Luck next time")
             print("You won Rs.0")
         
    else:
        res1  = input("enter 1 or 2 or 3 or 4 for your answer:")
        if res1 == 4:
            print("Correct Answer")
            print("You won Rs.10000")
            print("question for Rs.50000")
            question2 = "Second question : Who was the first woman prime minister of India\n"
            options2 = "1. Rukmini Devi Arundale\n2. Shakuntala Paranjpye\n3. Smt Indira Gandhi\n4. FathemaIsmail"       
            print(question2)
            print(options2) 
            lres2 = int( input("if you need lifeline enter 1 else enter 0 :"))
            if lres2 == 1:
                 print(3)
                 print("You won Rs.50000")    
                 print("question for Rs.75000")
                 question3 =  "Who is the current chief minister of Goa?"
                 options3 = "1. Naveen Patnaik\n2. Raghubar Das\n3. Manohar Parrikar\n4. Shashi Tharoor"
                 print(question3)
                 print(options3)
                 res3 = input("enter 1 or 2 or 3 or 4 for your answer:")
                 if res3 == 3:
                     print("Correct Answer")
                     print("You won Rs.75000")
                     print("question fo Rs.100000")
                     question4 = "Fourth question : On the reverse of which newly launched Indian currency note is the image of Sanchi Stupa printed\n"
                     options4 = "1. Rs.2000\n2. Rs.20\n3. Rs.200\n4. Rs.50"
                     print(question4)
                     print(options4)
                     res4  = input("enter 1 or 2 or 3 or 4 for your answer:")
                     if res4 == 3:
                         print("Correct Answer")
                         print("Congratulations......You Won Rs100000")
                     else:
                         print("Oops! it was wrong answer.....")
                         print("Better Luck next time")
                         print("You won Rs.0")
                 else:       
                     print("Oops! it was wrong answer.....")
                     print("Better Luck next time")
                     print("You won Rs.0")
            else:       
                res2 = input("enter 1 or 2 or 3 or 4 for your answer:")
                if res2 == 3:
                    print("Correct Answer")
                    print("You won RS.50000")
                    print("question for RS.75000")
                    question3 =  "Third question : Who is the current chief minister of Goa?"
                    options3 = "1. Naveen Patnaik\n2. Raghubar Das\n3. Manohar Parrikar\n4. Shashi Tharoor"
                    print(question3)
                    print(options3)
                    lres3 = int( input("if you need lifeline enter 1 else enter 0 :"))
                    if lres3 == 1:
                        print(3)
                        print("You Won RS.75000")
                        print("question for RS.100000")
                        question4 = "Fourth question : On the reverse of which newly launched Indian currency note is the image of Sanchi Stupa printed\n"
                        options4 = "1. Rs.2000\n2. Rs.20\n3. Rs.200\n4. Rs.50"
                        print(question4)
                        print(options4)
                        res4  = input("enter 1 or 2 or 3 or 4 for your answer:")
                        if res4 == 3:
                            print("Correct Answer")
                            print("Congratulations......You Won Rs100000")
                        else:
                            print("Oops! it was wrong answer.....")
                            print("Better Luck next time")
                            print("You won Rs.0")
                    else:
                        res3 = input("enter 1 or 2 or 3 or 4 for your answer:")
                        if res3 == 3:
                           print("Correct Answer")
                           print("You Won Rs.75000")
                           print("question fo Rs.100000")
                           question4 = "Fourth question : On the reverse of which newly launched Indian currency note is the image of Sanchi Stupa printed    \n"
                           options4 = "1. Rs.2000\n2. Rs.20\n3. Rs.200\n4. Rs.50"
                           print(question4)
                           print(options4)
                           lres4 = int( input("if you need lifeline enter 1 else enter 0 :"))
                           if lres4 == 1:
                              print(3)
                              print("Congratulations.....You Won RS.100000")
                           else:
                              if res4 == 3:
                                 print("Correct Answer")
                                 print("Congratulations......You Won Rs100000")
                              else:
                                print("Oops! it was wrong answer.....")
                                print("Better Luck next time")
                                print("You won Rs.0")
                        else:       
                            print("Oops! it was wrong answer.....")
                            print("Better Luck next time")
                            print("You won Rs.0")
                else:     
                    print("Oops! it was wrong answer.....")
                    print("Better Luck next time")
                    print("You won Rs.0")                                            
        else:
            print("Oops! it was wrong answer......")
            print("Better Luck next time") 
            print("You won Rs.0")                                          
    return "game is over"
                                                    
print(kbc())
        
                     
          
          
          
          
          
                
                
                
                
                 
          
          
              
          
