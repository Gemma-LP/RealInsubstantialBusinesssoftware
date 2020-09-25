print("Hello World")
weather = "raining"
if weather == "raining":
    print("Take Umbrealla")
else:
    print("Wear Coat")
weather = input("Is it raining or not?")
if weather == "raining":
    print("Take Umbrella")
else:
    print("Wear Coat")
import random
myName = input("Hello! What is your name?")
number = random.randint(1, 10)
print("Well, " + myName +  " I am thinking of a number between 1 and 10.")
guess = int(input("Take a guess:"))
if guess == number:
  print("Good job, " + myName + "! You guessed my number")
else:
  print("Wrong, better luck next time")
def user_name():
  user = input("Please enter your name ")
  print("Hello " + user + " a pleasure to meet you")