import json

game_file = open('ex36.json')
game = json.load(game_file)

print(game['title'])

def print_step(step_name):
  # to-do: handle when the step does not exist.
  step = game['steps'][step_name]
  
  title = step['title']

  print("=" * len(title))
  print(title)
  print("=" * len(title))

  print(step['description'])

  for question in step['questions']:
    print(question['title'])

  answer = input("What do you want to do? > ")
  target = step['questions'][int(answer) - 1]['target']
  print_step(target)

print_step('lets_start')