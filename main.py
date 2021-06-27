# Higher Lower Game   

import art
from game_data import data
from random import choice
from replit import clear

#get a random key value pair
def get_person(people):
  random_person = choice(people)
  return(random_person)

game_over = False
score = 0
personA = get_person(data)
print(art.logo)

while not game_over:
  #get second person and make sure they arent repeated
  personB = get_person(data)
  if personB == personA:
    personB = get_person(data)

  #main block of text shown
  print(f"Choice A: {personA['name']}, a {personA['description']}, from {personA['country']}.")
  print(art.vs)
  print(f"Choice B: {personB['name']}, a {personB['description']}, from {personB['country']}.")

  player_choice = input("Choose who you think has more followers. Type 'a' or 'b': ").lower()
  clear()
  print(art.logo)

#check if player guess correct
  if player_choice == "a":
    if personA['follower_count'] > personB['follower_count']:
      score += 1
      print(f"Thats right! Your score is {score}")
      personA = personB
    elif personA['follower_count'] < personB['follower_count']:
      print(f"That was the wrong answer your final score is {score}.")
      game_over = True

  if player_choice == "b":
    if personA['follower_count'] < personB['follower_count']:
      score += 1
      print(f"Thats right! Your score is {score}")
      personA = personB
    elif personA['follower_count'] > personB['follower_count']:
      print(f"That was the wrong answer your final score is {score}.")
      game_over = True

  
  


