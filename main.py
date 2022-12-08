import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


play=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if play==0:
  print(f"you choose : {rock}")
elif play==1:
  print(f"you choose : {paper}") 
else:
  print(f"you choose : {scissors}")
computer= random.randint(0, 1)
if computer==0:
  print(f"computer choose : {rock}")
elif computer==1:
  print(f"computer choose : {paper}") 
elif computer==2:
  print(f"computer choose : {scissors}")
if computer==play:
  print("Draw")
elif computer==0 and play==1 or computer==1 and play==2:
  print("You win")
elif computer==0 and play==2 or computer==2 and play==1:
  print("you lose")
