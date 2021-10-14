from colorama import Fore, Back, Style
import random

pricelist = [
  1000,
  2000,
  3000,
  5000,
  10000,
  20000,
  40000,
  80000,
  160000,
  320000,
  640000,
  1250000,
  2500000,
  5000000,
  10000000,
  70000000
]


def init():
  kbc = [
    {'q': 'Q1', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q2', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q3', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q4', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q5', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q6', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q7', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q8', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q9', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q10', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q11', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q12', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q13', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q14', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q15', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q16', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
    {'q': 'Q17', 1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Pink', 'c': 2, 'hint': 'hint'},
  ]

  lifes = [
    'Flip the question',
    'Remove two wrong answers(50 - 50)',
    'Hint',
    'two guesses allowed'
  ]

  counter = 0
  return kbc, lifes, counter


def rules():
  print(Fore.GREEN + '''1. The player has to choose the correct answer. 
2. If your answer is correct, you win a specific amount of prize money and moves to the next question.
3. If your answer is incorrect, you have to quit the game.
4. The prize amount starts from  1000/- and increases after every question.

''' + Style.RESET_ALL)


def price():
  pass


def lifelines(lifes):
  for x in range(len(lifes)):
    print(f'{x + 1}. {lifes[x]}')
  print('0. Cancel')

  c = int(input('Enter your choice: '))
  if c == 1:
    lifes.remove(lifes[c - 1])
  elif c == 2:
    lifes.remove(lifes[c - 1])
  elif c == 3:
    lifes.remove(lifes[c - 1])
  elif c == 4:
    lifes.remove(lifes[c - 1])
  elif c == 0:
    return lifes
  else:
    print('Invalid Choice')
    lifelines(lifes)
  return lifes


def win(count):
  count += 1
  return count


def lose():
  pass


def askquestion(kbc, lifes, counter):
  c = random.choice(kbc)
  print(Fore.BLUE + 'Question: ' + str(c['q']) + Style.RESET_ALL)
  print()
  print('1.', c[1])
  print('2.', c[2])
  print('3.', c[3])
  print('4.', c[4])

  if len(lifes) > 0:
    l = input(Fore.RED + 'Do you want to use a Life Line? (y/n): ' + Style.RESET_ALL)
    if l == 'y':
      lifes = lifelines(lifes)
  else:
    print(Fore.RED + 'You are out of Life Lines' + Style.RESET_ALL)

  ans = int(input('Enter your Answer: '))
  if c['c'] == ans:
    print('Correct Answer!')
    counter = win(counter)
  else:
    print('Wrong Answer!')
    lose()
  kbc.remove(c)

  return kbc, lifes, counter


# Driver Code

x = 10

rules()
qs, life, counter = init()
while x < 16:
  qs, life, counter = askquestion(qs, life, counter)
  print(pricelist[counter])
  x += 1
