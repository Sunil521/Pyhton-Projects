print("\n >>> welcome to the game of Team Chooser \n ")
print(""" It is a simple 'ROLL THE DICE' game  where the players of the two teams will take alternate turns to roll the dice . \n """) 
print("---------------------RULES-----------------------")
print("""
>>> Game contains two teams
>>> Players number should always be even.
>>> Players number should be more than or equal to two.
>>> Once the team selection is done then  begins the game "ROLL THE DICE " between the  two teams.
>>> Use  the key 'r' to roll the dice.
>>> Use the key 'q' to forfeit.
>>>. Each team will  get five(5) chances to roll the dice . And the team which wins maximum rounds is the winner .  Hope you enjoy it.""")
print("\n>>> lets start the game\n ")
teams = []
print("Please enter the  names of the two teams ")
for i in range(1,3):
    x = input("enter team %s name : "%(i))
    teams.append(x)    
print("\nPlayers number should always  be even")
p = int(input("enter number of players:"))
while p%2 != 0:
    print(" You have to select even number ofplayers ")
    p = int(input(" enter number of players : "))
players = []
for j in range(1,p+1):
    y = input("enter player  %s name : "%(j))
    players.append(y)
print("\nGiven teams list : ")      
print(teams)
print("Given players list : ")
print(players)
from random import choice
team = [ [ ] , [ ]  ]
while len(players)  > 0 :
    i = 0
    j = 0
    while ( j < 2) :
        player = choice(players)
        team[i].append(player)
        players.remove(player)
        i = i + 1
        j = j + 1
        if players == []:
            break
print("\nNew teams list : \n")            
s = teams[0]
teams2 = { s  :  team[0] } 
print(teams2)
t  = teams[1]
teams3 = { t :  team[1]}
print(teams3)
print("\nTeam selection is done ! \n") 

print("The game begins now !!! ")
from random import randint
TeamOneWins = 0
TeamTwoWins = 0
for a in teams2:
    x = a
    l = len(teams2[x])
for b in teams3:
    y = b
i = 0
c = 0
while(i<6):
        print("-------------------------")
        i = i + 1
        for k in range(0,l):
            if(c==5):
                break
            c = c + 1    
            print("Team 1 it's your turn.         Type 'r' to roll the dice or 'q' to forfeit. ")
            input1= input(">>>")
            if  input1  == "r":
                valueOne = randint(1,6)            
                print("Team 1 rolled ", valueOne)
                print("Team2 it's your turn.         Type 'r' to roll the dice or 'q' to forfeit. ")
                input2 = input(">>>")
                if input2 == "r":
                    valueTwo = randint(1,6)
                    print("Team 2 rolled ",  valueTwo)
                    if valueOne > valueTwo:
                        print("-------------------------")
                        print("Team 1 wins this round! ")
                        TeamOneWins += 1
                    elif valueOne == valueTwo:
                        print("-------------------------")
                        print("It's a draw! ")
                    else:
                        print("-------------------------")
                        print("Team 2 wins this round!")
                        TeamTwoWins += 1 
                elif input2 == "q":
                    print("-------------------------")
                    print("Team 1 wins this round! ")
                    TeamOneWins += 1
                else:
                    print("-------------------------")
                    print("Program ended abruptly")
                    break
            elif input1 == "q":
                print("-------------------------")
                print ("Team 2 wins this round! ")
                TeamTwoWins += 1
            else:
                print("-------------------------")
                print("Program ended abruptly. ")
                break
                      
                    
print("\nFinal results: ", TeamOneWins, "-", TeamTwoWins)
if TeamOneWins > TeamTwoWins:
    print("\nThe  winning team is Team 1: ",teams2)
elif TeamOneWins == TeamTwoWins:
    print("It's a draw! ")
else:
    print("The winning team is Team 2 : ",teams3)
print("\ngame ended ")
print("\nHope you have enjoyed the game !!\n")            
