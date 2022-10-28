import random
import hangman_art
import hangman_words

# art
stages = hangman_art.stages
art = hangman_art.art

# generate a random word
word_list = hangman_words.word_list
chosen_word = word_list[random.randint(0, (len(word_list) - 1))]

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# display
display = []
word_len = len(chosen_word)

# display as many blanks as letters in word
for _ in range(word_len):
  display += '_'

# lives and end_of_game
lives = 6
end_of_game = False

# start game
while not end_of_game:
  # ask the user to guess a letter
  guess = input("Player, guess a letter ").lower()

  # check guessed letter
  for position in range(word_len):
    letter = chosen_word[position]    
    if letter == guess:
      display[position] = letter
  
  # guess not in chosen_word decrease lives 
  if guess not in chosen_word:
    lives -= 1
    print(stages[lives])

  #join all the elements in the list and turn it into a string.
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win")

  if lives == 0:
    end_of_game = True
    print("You lose")