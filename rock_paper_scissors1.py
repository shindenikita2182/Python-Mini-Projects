import random
def get_choices():
  player_choice=input("enter a choice")
  options= ["rock","paper","scissor"]
  computer_choice= random.choice(options)
  choices={"player":player_choice,"computer":computer_choice}
  return choices

def check_win(player,computer):
  print(f"you choose {player}, computer choose {computer}")
  if player==computer:
    return"it's a tie!"
  elif player=="rock" :
    if computer == "scissor":
      return "rock smashes scissor! you won!"
    else:
      return "paper covers rock! you lose."
  elif player=="paper" :
      if computer == "scissor":
        return "scissor cuts paper! you lose."
      else:
        return "paper covers rock! you won!"
  elif player=="scissor" :
        if computer == "paper":
          return "scissor cuts paper! you won!"
        else:
          return "rock smashes scissor! you lose."
  else:
     return "aborted"
    
  

choices=get_choices()
print(choices)
result=check_win(choices["player"], choices["computer"])
print(result)