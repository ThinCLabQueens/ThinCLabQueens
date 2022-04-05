# This is an example script that will randomly pick my breakfast each morning (I love fruit).

import random

mylist = ["apple", "banana", "cherry"]

random_choice = random.choice(mylist)

print(random_choice)

#///////////////////////////////////////////////////////////////

# This is the same script, but turned into a function.

import random

def pick_fruit():
  
  mylist = ["apple", "banana", "cherry"]

  random_choice = random.choice(mylist)

  print(random_choice)
 
pick_fruit()
 
#They will both behave exactly the same.

#Here is the same script, but with an "if __name__ == "__main__":" block.

import random

def pick_fruit():
  
  mylist = ["apple", "banana", "cherry"]

  random_choice = random.choice(mylist)

  print(random_choice)
 
if __name__ == "__main__":
  pick_fruit()
  
#For some weird python reasons, this helps the script not get accidentally run.
#If you have any questions, please ask Ian through email.
