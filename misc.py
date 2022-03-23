import sys
import time

def slowprint(string):
	for letter in string + '\n':
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(5./500)

def read(x):
  in_file = open(x + ".txt", "r")
  line = in_file.readline()
  line_list = line.split(" ")
  in_file.close()
  return " ".join(line_list)

def write(x, string):
  in_file = open(x + ".txt", "w")
  print(string, file = in_file, end=" ")
  in_file.close()