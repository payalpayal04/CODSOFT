import random
print("***Let's play Rock-Paper-Scissors***")

n=1
c=0
p=0

def match(n,c,p):
    print("\nChoose 1 for ROCK\nChoose 2 for PAPER\nChoose 3 for SCISSOR\n")
    player=int(input("Enter your choie : "))
    computer=random.randint(1,3)
    
    if(computer==1):
        comp="ROCK"
    if(computer==2):
        comp="PAPER"
    if(computer==3):
        comp="SCISSOR"
    
    if(player<computer):
        print(f"The computer choose {comp} and you LOST")
        c+=1
    elif(player>computer):
        print(f"The computer choose {comp} and you WON")
        p+=1
    else:
        print(f"The computer choose {comp} and Its's a DRAW")

    rematch=input("Do you want a rematch? (y/n) : ")
    if(rematch=='y'):
        n+=1
        match(n,c,p)
    else:
        result(n,c,p)
        
match(n,c,p) 

 
def result(n,c,p):
    if(n>1):
        print("\nRESULTS")
        print("-------")
        for i in range (n):
            if (p>c):
                print(f"You have WON the series by {p}:{c}")
            elif(c>p):
                print(f"You have LOST the series by {c}:{p}")
            else:
                print(f"The match is DRAW by {p}:{c}")   
            break
