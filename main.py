import time
import random

player_points = 0
computer_points = 0
out_of_cards = False
max_no_of_turns = 5
no_of_turns = 0

name = input("Enter your name here: ")
print()
time.sleep(.9)
print(f"Welcome to the game, {name}!")
print()
time.sleep(1.3)
print("How to play: ")
time.sleep(1.2)
print("1.You can only use the cards that you have.")
time.sleep(2)
print("2.Everytime the result is draw, you will get card.")
time.sleep(2)
print("3.The first player who got highest score after 5 turns will win the game.")
time.sleep(2)
print()

Final_Counter = 1000000000
x = 1
while Final_Counter > x:
    if Final_Counter%100000 == 0:
        progress = ((x/Final_Counter))*100
        stringpogress = str(progress)
        stringpogress = stringpogress[0:4]
        print("\rProgress = {}".format(stringpogress),end=' ')
    x+=100000
print("Game Started")
time.sleep(.3)
print()
print(f"{name} points: " +str(player_points))
print("Computer points: " + str(computer_points))
print()
card=["rock", "paper", "scissor", "rock", "paper", "scissor"]
player_card = random.sample(card, k=5)
computer_card = random.choices(card, k=5)

print()
while no_of_turns != max_no_of_turns:
    time.sleep(1.3)
    print("Your card: ")
    print(str(player_card))
    print()
    player_attack = input("Enter your attack here: ")
    print()
    time.sleep(1)
    print("You used: ")
    print(player_attack)
    time.sleep(1)
    computer_attack=random.choice(computer_card)
    print()
    print("Computer used: ")
    print (computer_attack)
    time.sleep(1)

    if player_attack == "paper" and computer_attack=="rock":
      try:
        print()
        time.sleep(1)
        print("You earn 1 point, you win!!")
        print()
        player_points+=1
        player_card.remove(player_attack)
        time.sleep(1.5)
        print("Your score: " + str(player_points))
        print("Computer score: " + str(computer_points))
        no_of_turns+=1
        print()
      except:
        time.sleep(1.3)
        print("Attack doesn't exist on your card")
        print()
         
    elif player_attack=="rock" and computer_attack=="paper":
      try:
        print()
        computer_points+=1
        player_card.remove(player_attack)
        time.sleep(1)
        print("Computer earn 1 point, computer win!!")
        print()
        time.sleep(1.5)
        print("Your score: " + str(player_points))
        print("Computer score: " + str(computer_points))
        no_of_turns+=1
        print()
      except:
        time.sleep(1.3)
        print("Attack doesn't exist on your card")
        print()
    elif player_attack=="scissor" and computer_attack=="paper":
      try:
        print()
        time.sleep(1)
        print("You earn 1 point, you win!!")
        print()
        player_points+=1
        player_card.remove(player_attack)
        time.sleep(1.5)
        print("Your score: " + str(player_points))
        print("Computer score: " + str(computer_points))
        no_of_turns+=1
        print()
      except:
        time.sleep(1.3)
        print("Attack doesn't exist on your card")
        print()
    elif player_attack=="paper" and computer_attack=="scissor":
      try:
        print()
        time.sleep(1)
        print("Computer earn 1 point, computer win!!")
        print()
        computer_points+=1
        player_card.remove(player_attack)
        time.sleep(1.5)
        print("Your score: " + str(player_points))
        print("Computer score: " + str(computer_points))
        no_of_turns+=1
        print()
      except:
        time.sleep(1.3)
        print("Attack doesn't exist on your card")
        print()
    elif player_attack=="scissor" and computer_attack=="rock":
      try:
        time.sleep(1)
        print()
        print("Computer earn 1 point, computer win!!")
        print()
        computer_points+=1
        player_card.remove(player_attack)
        time.sleep(1.5)
        print("Your score: " + str(player_points))
        print("Computer score: " + str(computer_points))
        no_of_turns+=1
        print()
      except:
        time.sleep(1.3)
        print("Attack doesn't exist on your card")
        print()
    elif player_attack=="rock" and computer_attack=="scissor":
      try:
        print()
        player_points+=1
        player_card.remove(player_attack)
        time.sleep(1)
        print("You earn 1 point, you win!!")
        print()
        time.sleep(1.5)
        print("Your score: " + str(player_points))
        print("Computer score: " + str(computer_points))
        no_of_turns+=1
        print()
      except:
        time.sleep(1.3)
        print("Attack doesn't exist on your card")
        print()
   
    elif player_attack == computer_attack:
      try:
        print()
        time.sleep(1.3)
        print("It is draw")
        time.sleep(1)
        no_of_turns+=1
        player_card.remove(player_attack)
        print()
#        print("You draw 1 card")
#        player_card=player_card+random.sample(card, k=1)
#        print()
      except:
        print("You don't have this card")
    
    else:
      print()
      time.sleep(1.3)
      print("invalid attack")
      print()                              
  
    
if player_points>computer_points:
  time.sleep(.9)
  print()
  print("Congatulations!, you WIN!")
  time.sleep(1)
  print("Thank you")
elif player_points<computer_points:
  time.sleep(.9)
  print()
  print("Computer win!")
  time.sleep(1)
  print("Try again to play to win!")
  time.sleep(.5)
  print("Thank you!")
