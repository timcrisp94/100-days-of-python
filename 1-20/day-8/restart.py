# * a simple play_again construction *

from project_caesar_cypher import caesar

game_over = False
while not game_over:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  # trigger caesar function with input arguments
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  # restart condition 
  restart = input("Want to play again? Type 'yes' if you want to play again. Otherwise type 'no' ")
  if restart == "no":
    game_over = True
    print("bye bye")
