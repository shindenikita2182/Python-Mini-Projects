import random
top_of_range=input("Type a number:")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
random_number = random.randint(1,top_of_range)

gusses=0
while True:
    gusses+=1
    user_guess=input("Make a guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")
        quit()

    if user_guess == random_number:
        print("You got it!")
        break
   
    elif user_guess>random_number:
        print("you are above the number!")
    else:
        print("you are below the number!")
        
print("you got it in", gusses, "gusses")