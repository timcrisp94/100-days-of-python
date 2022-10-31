# def greet(name):  
#   print(f"hi {name}\nhow do you do?\nisn't the weather nice?")

# greet('Jack')
# greet('Diane')

def greet_with(name, location):
  print(f"Hello {name} from {location}")

greet_with("Tim", "Valparaiso")



def five_knuckle_shuffle(opponent):
  cena_moves = ["shoulder block", "suplex", "five knuckle shuffle"]
    
  print(f"Michael Cole: Cena off the ropes with a {cena_moves[0]} block and {opponent} goes down")
  print(f"Michael Cole: Cena with another {cena_moves[0]} and down goes {opponent} again!")
  print(f"Michael Cole: {opponent} throws a clothesline but Cena ducks and there's the {cena_moves[1]}")
  print(f"Jerry Lawler: it's time for the {cena_moves[2]}!")

five_knuckle_shuffle("The Rock")