import json
from sys import exit

game_file = open('ex36.json')
game = json.load(game_file)

print(game['title'])

def print_step(step_name):
  
  if step_name in game['steps']:
    step = game['steps'][step_name]
  else:
    print("Step not found. Exiting the game")
    print_step('end')

  title = step['title']
  print("=" * len(title))
  print(title)
  print("=" * len(title))

  if 'end' in step: 
    exit(0)

  print(step['description'])

  for question in step['questions']:
    print(question['title'])

  answer = input("What do you want to do? > ")
  target = step['questions'][int(answer) - 1]['target']
  print_step(target)

print_step(game['start'])