"""
lab4 task6
"""
import game

railway = game.Room("Залізнична станція")
railway.set_description("Залізнична станція, від якої всі добирається до Львова")

horodotska = game.Room("Городоцька")
horodotska.set_description("Одна з найбільших вулиць міста, а ще тут є ринок")

runok = game.Room("Ринок")
runok.set_description("Тут продається багато різної всячини")

opernui = game.Room("Опериний театр")
opernui.set_description("Головна пам'ятка міста. Тут є багато музикантів")

freedom_p = game.Room("Площа свободи")
freedom_p.set_description("Площа біля оперного театру. Тут часто грають вуличні музиканти")

freedom_s = game.Room("Проспект свободи")
freedom_s.set_description("Одна з найбільших вулиць міста, а ще тут є ринок")

freedom_s = game.Room("Автобус")
freedom_s.set_description("Великий автобус, де можна зустріти різних людей")



# railway.link_room(horodotska, "south")
# horodotska.link_room(railway, "north")
# horodotska.link_room(opernui, "west")
# opernui.link_room(horodotska, "east")

dave = game.Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
horodotska.set_character(dave)

tabitha = game.Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
opernui.set_character(tabitha)

cheese = game.Item("cheese")
cheese.set_description("A large and smelly block of cheese")
opernui.set_item(cheese)

book = game.Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
horodotska.set_item(book)

current_room = railway
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
