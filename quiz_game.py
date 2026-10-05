print("Welcome to my Computer quiz!")
playing=input("Do you want to play?")
if playing.lower()!="yes":
    quit()

print("Okay! Let's play:)")
score=0
answer=input("What does AWS stands for? ")
if answer.lower()=="amazon web services":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("What does ELB stands for? ")
if answer.lower()=="elastic load balancer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("Which command is used to make Directory ")
if answer.lower()=="mkdir":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("Which command is used to check the GIT Version ")
if answer.lower()=="git --version":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("What does VPN stands for? ")
if answer.lower()=="virtual private network":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got "+ str((score/5)*100) + " %.")