import sys
import time
import random
import msvcrt

def slowprint(string):
	for letter in string + '\n':
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(5./500)

def read(x):
  in_file = open("data/" + x + ".txt", "r")
  line = in_file.readline()
  line_list = line.split(" ")
  in_file.close()
  return " ".join(line_list)

def write(x, string):
  in_file = open("data/" + x + ".txt", "w")
  print(string, file = in_file, end=" ")
  in_file.close()

def openfile(filename):
  file = open("data/" + filename + ".txt", 'r')
  list = []
  for line in file:
    line = line.strip()
    statement = line.split(',')
    list.append(statement)
  file.close()
  return list

def choosestatement(x):
  file = openfile(x)
  index = random.randrange(len(file))
  statement = file[index]
  return " ".join(statement)