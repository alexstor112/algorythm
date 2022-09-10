import random


mysterious_number = random.randrange(0, 100)

for i in range(10, 0, -1):
  x = int(input('Your guess: '))
  if x == mysterious_number:
    print('Right!')
    exit()
  elif x < mysterious_number:
    print('Too small')
  else:
    print('Too big')

print('You lose. The answer was: ', mysterious_number)
