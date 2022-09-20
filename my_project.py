import art
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
	return random.choice(cards)


def main_game():
  should_continue = True
  while should_continue:
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_input == 'y':
      clear()
      print(art.logo)

      #Initial default
      player_card_list = []
      player_score = 0
      computer_card_list = []
      computer_score = 0

      #deal user a starting hand of 2 random card values
      for _ in range(2):
        chosen_card = deal_card()
        player_card_list.append(chosen_card)
        player_score += chosen_card
      #deal computer a starting hand of 2 random card values
      for _ in range(2):
        chosen_card = deal_card()
        computer_card_list.append(chosen_card)
        computer_score += chosen_card

      player_turn = True
      computer_turn = True
      if computer_score == 21 and player_score == 21:
        player_turn = False
        computer_turn = False
      elif computer_score == 21 or player_score == 21:
        if computer_score == 21:
          computer_turn = False
        else:
          player_turn == False

      if player_score > 21:
        player_card_list.remove(11)
        player_card_list[0] = 1
        player_score -= 10
      elif computer_score > 21:
        computer_card_list.remove(11)
        computer_card_list[0] = 1
        computer_score -= 10
        
      while player_turn:
        player_details = (f"Your cards: {player_card_list}, current score: {player_score}")
        print(player_details)
        print(f"Computer's first card: {computer_card_list[0]}")
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_choice == 'y':
          chosen_card = deal_card()
          player_card_list.append(chosen_card)
          player_score += chosen_card

          if player_score > 21:
            if 11 in player_card_list:
              player_card_list[player_card_list.index(11)] = 1
              player_score -= 10
            else:
              player_turn = False
          elif player_score == 21:
            player_turn = False
        else:
          player_turn = False
          
        player_details = (f"Your cards: {player_card_list}, final score: {player_score}")

      while computer_turn:
        
        if computer_score < 17:
          chosen_card = deal_card()
          computer_card_list.append(chosen_card)
          computer_score += chosen_card
          print(computer_card_list)
          print(computer_score)
        elif computer_score > 21:
          if 11 in computer_card_list:
            computer_card_list[computer_card_list.index(11)] = 1
            computer_score -= 10
          else:
            computer_turn = False
        elif computer_score == 21:
          computer_turn = False
        else:
          computer_turn = False
        
      computer_details = f"Computer's final card: {computer_card_list}, final score: {computer_score}"
      print(player_details)
      print(computer_details)
      if player_score > 21:
        print('You lose!')
      elif computer_score > 21:
        print('You win!')
      elif computer_score > player_score:
        print('You lose!')
      elif computer_score == 21 and player_score == 21:
        print('You lose!')
      elif computer_score == player_score:
        print('Draw!')
      else:
        print('You win!')

          
    else:
      should_continue = False
  
main_game()
