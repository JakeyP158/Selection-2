from random import randrange
print('Abu woz ere')
wrong = "Wrong you small brian"
print("----Welcome to the Joke Machine----")
joke = randrange(0, 4, 2)
if joke == 0:
  answer = input("How do you make holy water? ")
if answer == "boil the hell out of it":
  print("Correct, it's cringe you knew that...")
else:
  print(wrong)
  print("The answer was: Boil the hell out of it")
if joke == 2:
  answer = input("What do you call monkeys who share an amazon account? ")
if answer == "they were prime mates":
  print("Correct, that was a cringe order...")
else:
  print(wrong)
  print("The answer was: They were prime mates")
