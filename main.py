import os
import random
from functions import *
import time

# Clear the terminal in case the program is run multiple times
os.system("cls")

# Adding a delay in between each print statement gives the user more time to read each statement without getting overloaded by so much text
print("====== The Great McDonalds Battle ======")
print("You are an underage McDonalds worker, who flips burger patties for a living while hoping to get a promotion so you can make a little bit more money.")
time.sleep(4)
print("One day, a woman walks into the store and complains about her burger, which turned out to be a little undercooked on the inside.")
time.sleep(4)
print("Since no one takes her seriously, she starts throwing things around the restaurant and attacking people.")
time.sleep(4)
print("You walk out of the kitchen with your trusty frying pan to engage in combat with the Karen and take care of the problem. Maybe this will give you a promotion.")
print()
print("Press Enter to continue.")
input("> ")

# Clears the terminal for battle mode
os.system("cls")

def attack():
  print("====== YOU ATTACKED ======")
  chance = random.randrange(11) # The chance of landing a critical attack is decided out of 10
  attack = random.randrange(10, 20) # The amount of damage that you do is based out of 10-20
  if chance >= 0 and chance <= 3: # If chance is between 0 and 3, or IS 0 or 3, you will miss the attack
    slowprint("You missed! The Karen dodged your attack!")
    print()
    slowprint("You did not deal any damage to the Karen.")
    print()
  elif chance >= 4 and chance <= 8: # If chance is between 4 and 8, or IS 4 and 8, you will attack normally
    slowprint("You attacked the Karen with your frying pan!")
    health = int(read("enemyhp")) - attack # Karen's updated HP is her current HP subtracted by the amount of attack
    print()
    slowprint("You dealt " + str(attack) + " damage to the Karen!")
    write("enemyhp", health) # Updates Karen's HP into her corresponding .txt file
    if int(read("enemyhp")) <= 0: # If her updated health is equal to or below 0, then it will run the shedied() function
      shedied()
  else:
    slowprint("You landed a critical attack! Your damage has been doubled!")
    health = int(read("enemyhp")) - (attack * 2) # Karen's updated HP is her current HP subtracted by the amount of attack multiplied by 2, because the attack was a critical attack
    print()
    print("You dealt " + str(attack * 2) + " damage to the Karen (" + str(attack) + " x 2)!")
    write("enemyhp", health) # Updates Karen's Hp into her corresponding .txt file
    if int(read("enemyhp")) <= 0: # if her updated health is equal to or below 0, then it will run the shedied() function
      shedied()
  # If she did not die to any attacks, then code below will run
  print()
  print("Press Enter to continue.")
  input("> ")
  os.system("cls") # This will clear the terminal for Karen's attack
  enemystrike() # This will generate Karen's attack


def enemystrike():
  print("====== YOU GOT ATTACKED ======")
  chance = random.randrange(11) # The chance of landing a critical attack is decided out of 10
  attack = random.randrange(10, 20) # The amount of damage that Karen deals is based out of 10-20
  if chance >= 0 and chance < 3: # If chance is between 0 and 3, or IS 0 or 3, Karen will miss her attack
    slowprint("You dodged the Karens attack!")
    print()
    slowprint("Karen did not deal any damage to you.")
    print()
  elif chance >= 4 and chance <= 8: # If chance is between 4 and 8, or IS 4 and 8, then Karen will attack normally
    slowprint("Karen attacked you with her purse!")
    health = int(read("yourhealth")) - attack
    print()
    slowprint("You took " + str(attack) + " damage!")
    write("yourhealth", health)
    if int(read("yourhealth")) < 1:
      youdied()
  else:
    slowprint("Karen landed a critical attack! Her attack has been doubled!")
    health = int(read("yourhealth")) - (attack * 2)
    print()
    print("She dealt " + str(attack * 2) + " damage to the you (" + str(attack) + " x 2)!")
    write("yourhealth", health)
    if int(read("yourhealth")) < 1:
      youdied()
  print()
  print("Press Enter to continue.")
  input("> ")
  os.system("cls")
  battle()
  
def youdied():
  print("====== YOU DIED ======")
  os.system("cls")
  slowprint("You died! Karen hit you with her purse too many times and you lost too much HP.")
  slowprint("You feel sad in your last moments, regretting that you even decided to defend a restaurant that barely even payed anything.")
  slowprint("At least, you won't have to worry about getting that promotion anymore.")
  print()
  print("Press Enter to continue.")
  input("> ")
  write("yourhealth", 100)
  write("enemyhp", 100)
  os.system("cls")
  exit()

def shedied():
  print("====== KAREN DIED ======")
  os.system("cls")
  slowprint("You killed Karen! You hit her with your frying pan too many times and she lost too much HP.")
  slowprint("Good job! You successfully defended your restaurant against the Karen!")
  slowprint("Your boss was so proud of you that he gave you a promotion")
  print()
  print("Press Enter to continue.")
  input("> ")
  write("yourhealth", 100)
  write("enemyhp", 100)
  os.system("cls")
  exit()

def surrender():
  print("====== YOU SURRENDERED ======")
  slowprint("You surrendered to the Karen!")
  slowprint("You surrender, only to be slapped across the face with her purse.")
  slowprint("Your HP drops to 0 and you die.")
  slowprint("Never trust a Karen.")
  print()
  print("Press Enter to continue.")
  input("> ")
  write("yourhealth", 100)
  write("enemyhp", 100)
  os.system("cls")
  exit()


def battle():
  print("====== BATTLE ======")
  slowprint("You must defend your restaurant against the Karen! Send a number to select an option:")
  print("Your HP:", read("yourhealth"))
  print("The Karen's HP:", read("enemyhp"))
  print()
  print("Send 1 to engage with the Karen")
  print("Send 2 to surrender to Karen")
  choice = input("> ")
  if choice == "1":
    os.system("cls")
    attack()
  elif choice == "2":
    surrender()
  else:
    os.system("cls")
    battle()

battle()