#scrapped the other one cause of major laws same thing different build
import time
def yes_no(question):
  valid = False
  while not valid:

   response = input(question).lower ()
   if response == "yes" or response == "y":
     response = "hope you enjoy"
     return response

   elif response == "no" or response == "n":
     response = "Welcome to lucky unicorn the slot machine. The aim to win is to get the unicorn but there are 3 more things you can also roll like donkey zebra and horse each have a set value you get or dont for example if you rolled and got a donkey you wouldnt get anything zebra and horse you would only get $2 and unicorn being our jackpot of $4"
     return response


   else:
     print ("yes or no nothing fancy")
show_instrustions = yes_no ("have you played on this machine before?")
print ("{}" .format(show_instrustions))

print()
print ("Goodluck!")

import random

#the goodie main 
starting_balance = 100
balance = starting_balance
for items in range (0,500) :
 chosen_num = random.randint (1,100)
#1 in 5 chance to get unicorn adds 4 dollars to balance
if 1 <= chosen_num <= 5:
  chosen = "unicorn" 
  balance += 4
#6 in 36 chance to get donkey lose 1 dollar to balance
elif 6 <= chosen_num <= 36:
 chosen = "donkey"
 balance -= 1
else:
  if chosen_num % 2 == 0 :
    chosen = "horse"
  else :
    chosen = "zebra"
  balance -= 0.5

print()
print(chosen_num)

print ()
print ("starting_balance : ${:.2f} " .format (starting_balance))
print ("Final Balance: ${:.2f}" .format (balance))

