name=input("Enter your name: ")
print("Welcome",name, "to this adventure!")
answer = input("You are on a dam road, it has come to an end and you" \
" can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around " \
    "it or swim accross? Type walk to walk around and swim to swim across: ").lower()
    if answer == "swim":
        print("you swam accross and were eaten by an alligator")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a vaid option, You Lose.")

elif answer == "right":
    answer = input("you come to a bridge, it looks woobly, do you wantto " \
    "cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them(yes/no)? ").lower()
        if answer == "yes":
            print("you talked to the stranger and they give a gold. you WIN!")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose.")
        else:
             print("Not a vaid option, You Lose.")  
    else:
        print("Not a vaid option, You Lose.")
else:
    print("Not a vaid option, You Lose.")
print("Thank you for trying", name,"!")