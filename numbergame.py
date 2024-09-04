import random

playing = True
number = random.randint(10,20)

print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")

while playing:
  guess = int(input("give me your best guess!:"))
  if number == guess:
    print("you won...")
    print("the number was",number)
    playing = False

  else:
    print("your guess is strange,try again loser..")