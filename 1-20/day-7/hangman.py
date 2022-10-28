import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, (len(word_list) - 1))]


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"
print(display)

end_of_game = False

while not end_of_game:
  guess = input("Player, guess a letter ").lower()
  # checked guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess: 
      display[position] = letter

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")



