B = []
value = 0
pos = 0
for i in range(0,23):
    B.append(2)
print("\n")    
print("\n")
print("---------------------------TIGERS & GOATS---------------------------")
print (B)
print("In the game\ntiger's are represented by 0\ngoat's are represented by 1\nempty spot is represented by 2") 
print("\nIf all tiger's get trapped then GOATS WINS THE GAME\nIf five goats are killed by tigers then TIGER'S WINS THE GAME\n")
goats_died = 0   
           
def winning():
    global B
    global value
    for i in range(0,23):
        if i == 0:    #tiger is in B[0]position
           if B[i] == 0 and B[i+2] == 1 and B[i+3] == 1 and B[i+4] == 1 and B[i+5] == 1 and B[i+8]  ==1 and B[i+9] == 1 and B[i+10] == 1 and B[i+11] == 1 : 
              value += 1
        if i == 1:    #tiger is in B[1]position
           if B[i] == 0 and B[i+1] == 1 and B[i+2] == 1 and B[i+6] == 1 and B[i+12] == 1 : 
              value += 1
        if i == 2:    #tiger is in B[2]position
           if B[i] == 0 and B[0] == 1 and B[i+1] == 1 and B[i-1] == 1 and B[i+2] == 1 and B[i+6] ==1 and B[i+12] == 1 : 
              value += 1              
        if i == 3 or i== 4:    #tiger is in B[3] or B[4] position
           if B[i] == 0 and B[0] == 1 and B[i-1] == 1 and B[i+1] == 1 and B[i-2] == 1 and B[i+2] ==1 and B[i+6] == 1 and B[i+12] == 1 and B[i+11] == 1 : 
              value += 1
        if i == 5 :    #tiger is in B[5]position
           if B[i] == 0 and B[0] == 1 and B[i+1] == 1 and B[i-1] == 1 and B[i-2] == 1 and B[i+6] ==1 and B[i+12] == 1 : 
              value += 1 
        if i == 6:    #tiger is in B[6]position
           if B[i] == 0 and B[i-1] == 1 and B[i-2] == 1 and B[i+6] == 1 and B[i+12] == 1 :
              value += 1
        if i == 7:    #tiger is in B[7]position
           if B[i] == 0 and B[i+1] == 1 and B[i+2] == 1 : 
              value += 1
        if i == 8:    #tiger is in B[8]position
           if B[i] == 0 and B[i+1] == 1 and B[i-1] == 1 and B[i+2] == 1 and B[i-6] == 1 and B[0] ==1 and B[i+6] == 1 and B[i+11] == 1 : 
              value += 1  
        if i == 9 or i == 10:    #tiger is in B[9] and B[10]position
           if B[i] == 0 and B[0] == 1 and B[i-1] == 1 and B[i+1] == 1 and B[i-2] == 1 and B[i+2] ==1 and B[i+6] == 1 and B[i-6] == 1 and B[i+11] == 1 : 
              value += 1
        if i == 11:    #tiger is in B[11]position
           if B[i] == 0 and B[0] == 1 and B[i+1] == 1 and B[i-1] == 1 and B[i-2] == 1 and B[i-6] ==1 and B[i+6] == 1 and B[i+11] == 1: 
              value += 1
        if i == 12:    #tiger is in B[12]position
           if B[i] == 0 and B[i-1] == 1 and B[i-2] == 1 and B[i-6] == 1 and B[i+6] == 1 : 
              value += 1 
        if i == 13:    #tiger is in B[13]position
           if B[i] == 0 and B[i+1] == 1 and B[i+2] == 1 and B[i-6] == 1 and B[i-12] == 1 :
              value += 1
        if i == 14:    #tiger is in B[14]position
           if B[i] == 0 and B[i-1] == 1 and B[i+1] == 1 and B[i+2] == 1 and B[i-6] == 1 and B[i+5] ==1 and B[i-12] == 1 : 
              value += 1
        if i == 15 or i == 16:    #tiger is in B[15] and B[16]position
           if B[i] == 0 and B[i+1] == 1 and B[i-1] == 1 and B[i+2] == 1 and B[i-2] == 1 and B[i+5] ==1 and B[i-6] == 1 and B[i-12] == 1 : 
              value += 1 
        if i == 17:    #tiger is in B[17]position
           if B[i] == 0 and B[i+1] == 1 and B[i-1] == 1 and B[i-2] == 1 and B[i-6] == 1 and B[i+5] ==1 and B[i-12] == 1 : 
              value += 1
        if i == 18:    #tiger is in B[18]position
           if B[i] == 0 and B[i-1] == 1 and B[i-2] == 1 and B[i-6] == 1 and B[i-12] == 1 : 
              value += 1
        if i == 19 :  #tiger is in B[19]position
           if B[i] == 0 and B[i+1] == 1 and B[i+2] == 1 and B[i-5] == 1 and B[i-11] == 1 :         
              value += 1
        if i == 20 :  #tiger is in B[20]position
           if B[i] == 0 and B[i-1] == 1 and B[i+1] == 1 and B[i+2] == 1 and B[i-5] == 1 and B[i-11] == 1 :      
              value += 1
        if i == 21 :  #tiger is in B[21]position
           if B[i] == 0 and B[i-1] == 1 and B[i+1] == 1 and B[i-2] == 1 and B[i-5] == 1 and B[i-11] == 1 : 
              value += 1
        if i == 22 :  #tiger is in B[22]position
           if B[i] == 0 and B[i-1] == 1 and B[i-2] == 1 and B[i-5] == 1 and B[i-11] == 1 : 
              value += 1                  
    return 0
    
def capturing_probability():
    global B
    global goats_died
    for i in range(0,23):
        if i==0 and B[i]==0 :
           print(i)
           if B[i+2] == 1 and B[i+8] == 2 :
              B[i]=2
              B[i+2]=2
              B[i+8]=0
              goats_died += 1
           if B[i+3] == 1 and B[i+9] == 2 :
              B[i] =2
              B[i+3] =2
              B[i+9] =0
              goats_died += 1
           if B[i+4] == 1 and B[i+10] == 2 : 
              B[i] =2
              B[i+4] =2
              B[i+10] =0
              goats_died += 1
           if B[i+5] == 1 and B[i+11] == 2 :
              B[i] =2
              B[i+5] =2
              B[i+11] =0
              goats_died += 1
        if i==1 or i==2 and B[i]==0 :
           if B[i+1] == 1 and B[i+2] == 2 :
              B[i] =2
              B[i+1] =2
              B[i+2] =0
              goats_died += 1
           if B[i+6] == 1 and B[i+12] == 2 :
              B[i] =2
              B[i+6] =2
              B[i+12] =0
              goats_died += 1
        if i==3 or i==4 and B[i]==0 :
           if B[i+1] == 1 and B[i+2] == 2 :
              B[i] =2
              B[i+1] =2
              B[i+2] =0
              goats_died += 1
           if B[i+6] == 1 and B[i+12] == 2 :
              B[i] =2
              B[i+6] =2
              B[i+12] =0
              goats_died += 1
           if B[i-1] == 1 and B[i-2] == 2 :
              B[i] =2
              B[i-1] =2
              B[i-2] =0
              goats_died += 1
        if i==5 or i==6 and B[i]==0 :
           if B[i-1] == 1 and B[i-2] == 2 :
              B[i] =2
              B[i-1] =2
              B[i-2] =0
              goats_died += 1
           if B[i+6] == 1 and B[i+12] == 2 :
              B[i] =2
              B[i+6] =2
              B[i+12] =0
              goats_died += 1
        if i==7 and B[i]==0 :
           if B[i+1] == 1 and B[i+2] == 2 :
              B[i] =2
              B[i+1] =2
              B[i+2] =0
              goats_died += 1
        if i==8 and B[i]==0 :
           if B[i+1] == 1 and B[i+2] == 2 :
              B[i] =2
              B[i+1] =2
              B[i+2] =0
              goats_died += 1
           if B[i+6] == 1 and B[i+11] == 2 : 
              B[i] =2
              B[i+6] =2
              B[i+11] =0
              goats_died += 1
           if B[i-6] == 1 and B[i-i] == 2 :
              B[i] =2
              B[i-6] =2
              B[i-i] =0
              goats_died += 1 
        if i==9 or i==10 and B[i]==0:
           if B[i+1] == 1 and B[i+2] == 2:
              B[i] =2
              B[i+1] =2
              B[i+2] =0
              goats_died += 1
           if B[i-1] == 1 and B[i-2] == 2:
              B[i] =2
              B[i-1] =2
              B[i-2] =0
              goats_died += 1
           if B[i-6] == 1 and B[i-i] == 2:
              B[i] =2
              B[i-6] =2
              B[i-i] =0
              goats_died += 1           
           if B[i+6] == 1 and B[i+11] == 2:
              B[i] =2
              B[i+6] =2
              B[i+11] =0
              goats_died += 1
        if i==11 and B[i]==0 :
           if B[i-1] == 1 and B[i-2] == 2 :
              B[i] =2
              B[i-1] =2
              B[i-2] =0
              goats_died += 1
           if B[i-6] == 1 and B[i-i] == 2 :
              B[i] =2
              B[i-6] =2
              B[i-i] =0
              goats_died += 1           
           if B[i+6] == 1 and B[i+11] == 2:
              B[i] =2
              B[i+6] =2
              B[i+11] =0
              goats_died += 1
        if i==12 and B[i]==0 :
           if B[i-1] == 1 and B[i-2] == 2 :
              B[i] =2
              B[i-1] =2
              B[i-2] =0
              goats_died += 1
        if i==13 or i==14 and B[i]==0 :
           if B[i+1] == 1 and B[i+2] == 2 :
              B[i] =2
              B[i+1] =2
              B[i+2] =0
              goats_died += 1
           if B[i-6] == 1 and B[i-12] == 2 :
              B[i] =2
              B[i-6] =2
              B[i-12] =0
              goats_died += 1  
        if i==15 or i==16 and B[i]==0 :
           if B[i-1] == 1 and B[i-2] == 2 :
              B[i] =2
              B[i-1] =2
              B[i-2] =0
              goats_died += 1
           if B[i-6] == 1 and B[i-12] == 2:
              B[i] =2
              B[i-6] =2
              B[i-12] =0           
              goats_died += 1
           if B[i+1] == 1 and B[i+2] == 2:
              B[i] =2
              B[i+6] =2
              B[i+2] =0
              goats_died += 1
        if i==17 or i==18 and B[i]==0 :
           if B[i-1] == 1 and B[i-2] == 2 :
              B[i] =2
              B[i-1] =2
              B[i-2] =0
              goats_died += 1
           if B[i-6] == 1 and B[i-12] == 2 :
              B[i] =2
              B[i-6] =2
              B[i-12] =0
              goats_died += 1             
        if i==19 or i==20 and B[i]==0 :
           if B[i+1] == 1 and B[i+2] == 2 :
              B[i] =2
              B[i+1] =2
              B[i+2] =0 
              goats_died += 1            
           if B[i-5] == 1 and B[i-11] == 2 :
              B[i] =2
              B[i-5] =2
              B[i-11] =0
              goats_died += 1
        if i==21 or i==22 and B[i]==0 :
           if B[i-1] == 1 and B[i-2] == 2 :
              B[i] =2
              B[i-1] =2
              B[i-2] =0
              goats_died += 1             
           if B[i-5] == 1 and B[i-11] == 2 :
              B[i] =2
              B[i-5] =2
              B[i-11] =0
              goats_died += 1                       
    return 0
  
def position_changing(x):
    global B
    global pos
    pos = int(input("position is occupied,choose another position :"))
    pos = pos - 1
    B[pos] = x            
    return 0

def movement(x,initial,final):
   global B
   if B[final] == 2 :
      B[initial] = 2
      B[final] = x
   else:
      print("Oops..!position is occupied,try again")
   return 0   
def person_turn(x):
    global B
    global pos
    print("turn is up\n")
    pos = int(input("enter(or)move your position to :"))
    pos = pos - 1
    if B.count(0) < 4 and B.count(1) < 16: 
       if pos < 23 :
          if B[pos] == 2 : 
             B[pos] = x
             capturing_probability()
             winning()
             print("goats died :",goats_died)
             print("no.of tigers trapped:",value)
             print(B)
          else:
             position_changing(0)
             capturing_probability()
             print("goats died :",goats_died)           
             winning()
             print("no.of tigers trapped:",value)
             print(B)   
       else:
          pos = int(input("position is invalid\nenter a valid position :"))
          pos = pos - 1
          if B[pos] == 2 : 
             B[pos] = x
             capturing_probability()
             print("goats died :",goats_died)
             winning()
             print("no.of tigers trapped:",value)
             print(B)
          else:
             position_changing(1)           
             capturing_probability()
             print("goats died :",goats_died)
             winning()
             print("no.of tigers trapped:",value)
             print(B)
    else:        
       if B.count(0) == 3 :
          print("\nOops..!no more tigers\nplease move your tigers")
          if x == 0:
             initial,final = int(input("enter your movement position from initial to final:"))  
             movement(x,initial,final)   
          else:
             print("\nOops..!no more goats\nplease move your goats")
             initial,final = int(input("enter your movement position from initial to final:"))  
             movement(x,initial,final)   
    return 0
        
def game():
    global goats_died
    global value
    print("choose tiger or goat ")
    person1 = int(input("for tiger enter 0 and for goat enter 1:"))
    if person1 == 0:
       person2 = 1
       print("the second person's is goat")
    else:
       person2 = 0
       print("the second person's is tiger")    
    while value < 4 and goats_died < 6:
          print("\ntiger's")
          person_turn(0)         
          print("\ngoat's")
          person_turn(1)
    if value == 3:
       print("GOATS WON THE GAME :)")
    if goats_died == 5:
       print("TIGERS WON THE GAME :)")                     
    return 0   
    
game()                                                                                       
