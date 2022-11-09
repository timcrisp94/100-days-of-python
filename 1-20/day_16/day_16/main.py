from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Wrestler Name", ["Ric Flair", "Stone Cold Steve Austin", "John Cena", "Roman Reigns"])
table.add_column("Hometown", ["Charlotte, North Carolina", "Victoria, Texas", "West Newbury, Massachusetts", "Pensacola, Florida"])
table.add_column("Finishing Move", ["Figure Four", "Stone Cold Stunner", "Attitude Adjustment", "Spear"])
table.add_column("Title Reigns", [18, 6, 16, 6])
table.align = "l"

# does not sort table, but inside a print statement, will print sorted table
table.get_string(sortby="Title Reigns", reversesort=True)


print(table)

"""
Objects are like people. They’re living, breathing things that have knowledge inside them about how to do things and 
have memory inside them so they can remember things. And rather than interacting with them at a very low level, 
you interact with them at a very high level of abstraction, like we’re doing right here.

Here’s an example: If I’m your laundry object, you can give me your dirty clothes and send me a message that says, 
“Can you get my clothes laundered, please.” I happen to know where the best laundry place in San Francisco is. 
And I speak English, and I have dollars in my pockets. 
So I go out and hail a taxicab and tell the driver to take me to this place in San Francisco. 
I go get your clothes laundered, I jump back in the cab, I get back here. I give you your clean clothes and say, 
“Here are your clean clothes.”

You have no idea how I did that. You have no knowledge of the laundry place. 
Maybe you speak French, and you can’t even hail a taxi. 
You can’t pay for one, you don’t have dollars in your pocket. 
Yet I knew how to do all of that. And you didn’t have to know any of it. 
All that complexity was hidden inside of me, and we were able to interact at a very high level of abstraction. 
That’s what objects are. They encapsulate complexity, and the interfaces to that complexity are high level.


"""