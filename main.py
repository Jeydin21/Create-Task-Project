import time
import sys
import os
import random

def slowprint(string):
	for letter in string + '\n':
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(5./250)

def read(x):
  in_file = open(x + ".txt", "r")
  line = in_file.readline()
  line_list = line.split(" ")
  in_file.close()
  return " ".join(line_list)

def write(x, string):
  in_file = open(x + ".txt", "w")
  print(string, file = in_file)
  in_file.close()
'''
print("====== The McDonalds Conflict ======")
slowprint("You are a under-age, under-paid, harshly treated McDonalds worker who makes money by flipping burgers for the people of America who don't give a crap about what goes inside of their bodies.")
slowprint("One day, a deranged middle-aged woman walks in and demands to know why her hamburger was wet in the exact place where she had bitten into, not realizing that it was only her saliva that came out of her own teeth.")
slowprint("The insane looking woman immediately starts causing chaos in the American restaurant and disturbs the customers")
slowprint("Thinking to yourself that you don’t get paid enough for this, you walk out with your trusty frying pan to engage in combat with the lady and take care of the problem. Maybe this will give you a promotion.")
input("> ")
'''
# Clears the terminal for battle mode
os.system("cls")

def attack():
  print("====== YOU ATTACKED ======")
  chance = random.randrange(11)
  attack = random.randrange(10, 20)
  if chance > 0 and chance < 5:
    slowprint("You missed! The Karen dodged your attack!")
    slowprint("You did not deal any damage")
  elif chance > 4 and chance < 9:
    slowprint("You attacked the Karen with your frying pan!")
    health = int(read("stats")) - attack
    print()
    slowprint("You dealt " + attack + " damage to the Karen!")
    write("stats", health)
  else:
    slowprint("You landed a critical attack! Your damage has been doubled!")
    health = int(read("stats")) - (attack * 2)
    print()
    print("You dealt " + attack * 2 + " damage to the enemy (" + attack + " x 2)!")
    write("stats", health)
  input("> ")
  os.system("cls")
  battle()
  

def battle():
  print("====== BATTLE ======")
  slowprint("You must defend your restaurant against the Karen! Send a number to select an option:")
  print("Your HP:", read("stats"))
  print("The Lady's HP:", read("stats"))
  print()
  print("Send 1 to engage with the Karen")
  print("Send 2 to increase your shield count")
  choice = input("> ")
  if choice == "1":
    os.system("cls")
    attack()
  elif choice == "2":
    print("shield")
  else:
    os.system("cls")
    battle()


battle()