import os
import random
from functions import *

os.system("cls")
print("====== The Great McDonalds Battle ======")
slowprint("You are an underage McDonalds worker, who flips burger patties for a living while hoping to get a promotion so you can make a little bit more money.")
slowprint("One day, a woman walks into the store and complains about her burger, which turned out to be a little undercooked on the inside.")
slowprint("Since no one takes her seriously, she starts throwing things around the restaurant and attacking people.")
slowprint("Thinking to yourself that you don't get paid enough for this, you walk out with your trusty frying pan to engage in combat with the Karen and take care of the problem. Maybe this will give you a promotion.")
print()
print("Press Enter to continue.")
input("> ")

# Clears the terminal for battle mode
os.system("cls")

def attack():
  print("====== YOU ATTACKED ======")
  chance = random.randrange(11)
  attack = random.randrange(10, 20)
  if chance > 0 and chance < 3:
    slowprint("You missed! The Karen dodged your attack!")
    print()
    slowprint("You did not deal any damage to the Karen.")
    print()
  elif chance > 2 and chance < 9:
    slowprint("You attacked the Karen with your frying pan!")
    health = int(read("enemyhp")) - attack
    print()
    slowprint("You dealt " + str(attack) + " damage to the Karen!")
    write("enemyhp", health)
    if int(read("enemyhp")) < 1:
      shedied()
  else:
    slowprint("You landed a critical attack! Your damage has been doubled!")
    health = int(read("enemyhp")) - (attack * 2)
    print()
    print("You dealt " + str(attack * 2) + " damage to the Karen (" + str(attack) + " x 2)!")
    write("enemyhp", health)
    if int(read("enemyhp")) < 1:
      shedied()
  print()
  print("Press Enter to continue.")
  input("> ")
  os.system("cls")
  enemystrike()


def enemystrike():
  print("====== YOU GOT ATTACKED ======")
  chance = random.randrange(11)
  attack = random.randrange(10, 20)
  if chance > 0 and chance < 3:
    slowprint("You dodged the Karens attack!")
    print()
    slowprint("Karen did not deal any damage to you.")
    print()
  elif chance > 2 and chance < 9:
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