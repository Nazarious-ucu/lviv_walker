"""
lab4 task6
"""
import game
import random

main_hero = game.Hero('Nazarchuk', 'Крутиай чувак')

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

bus = game.Room("Автобус")
bus.set_description("Великий автобус, де можна зустріти різних людей")

stryskiy_park = game.Room("Стризький парк")
stryskiy_park.set_description("Дуже красиве місце")

svencic = game.Room("Корпус УКУ на Свенціцького")
svencic.set_description("Мальовниче місце з гуманітарними студентами")

cumpus = game.Room("Кампус")
cumpus.set_description("Це серце УКУ")

railway.link_room(horodotska, "south")
horodotska.link_room(railway, "north")

horodotska.link_room(runok, "west")
runok.link_room(horodotska, "east")

horodotska.link_room(opernui, "east")
opernui.link_room(horodotska, "west")

runok.link_room(opernui, "north")
opernui.link_room(runok, "south")

opernui.link_room(freedom_p, "north")
freedom_p.link_room(opernui, "south")

opernui.link_room(freedom_s, "east")
freedom_s.link_room(opernui, "west")

freedom_p.link_room(freedom_s, "north")
freedom_s.link_room(freedom_p, "south")

freedom_s.link_room(bus, "east")
bus.link_room(freedom_p, "west")

bus.link_room(stryskiy_park, "north")
stryskiy_park.link_room(freedom_p, "south")

bus.link_room(svencic, "east")
svencic.link_room(freedom_p, "west")

stryskiy_park.link_room(svencic, "west")
svencic.link_room(freedom_p, "east")

stryskiy_park.link_room(cumpus, "north")
cumpus.link_room(freedom_p, "south")

dave = game.Friend("Dave", "Торгаш")
dave.set_conversation("Я хочу викидати одну річ, не хочеш забрати")
dave.set_weakness("Скрипка")
runok.set_character(dave)

nazar = game.Friend("Nazar", "Акторко")
nazar.set_conversation("Я працюю в оперному, і  у мене поломалася скрипка:(")
nazar.set_weakness("Нічого")
opernui.set_character(nazar)

danya = game.Friend("Данило", "Вуличний музикант")
danya.set_conversation("Заплатіть мені грошей")
danya.set_weakness("Струни від гітари")
freedom_p.set_character(danya)

noy = game.Friend("Ной", "Прохожий")
noy.set_conversation("Я тут просто іду на роботу, хочу кави")
noy.set_weakness("Кросовок")
freedom_s.set_character(noy)

bogdan = game.Enemy("Богдан", "Маршрутчик")
bogdan.set_conversation("Передавайте за проїзд")
bogdan.set_weakness("Руль")
bus.set_character(bogdan)

petrovuch = game.Enemy("Петрович", "Бомж")
petrovuch.set_conversation("Я живу в стризькому під лавкою, у тебе є пиво?")
petrovuch.set_weakness("Розбита пляшка")
stryskiy_park.set_character(petrovuch)

student = game.Enemy("Єрена", "Соціологиня")
student.set_conversation("Я дуже змучена")
student.set_weakness("Опитування")
svencic.set_character(student)

stick = game.Veapon("Палка", 20)
stick.set_description("Дерев'яна")
railway.set_item(stick)

syringe = game.Veapon("Шприц", 45)
syringe.set_description("Колючий")
horodotska.set_item(syringe)

violing = game.Item("Скрипка")
violing.set_description("Корисна")
dave.set_item(violing)

cofee = game.Item("Кава")
cofee.set_description("гаряча та смачна")
nazar.set_item(cofee)

strings = game.HelpItem("Пісня")
strings.set_description("Прекрасна")
danya.set_item(strings)

knife = game.Veapon("Ніж", 60)
knife.set_description("Хороша зброя")
noy.set_item(knife)

handlebar = game.Veapon("Руль", 50)
handlebar.set_description("Круглий")
bogdan.set_item(handlebar)

survey = game.Veapon("Опитування", 80)
survey.set_description("Набридливе")
student.set_item(survey)

botlle = game.Veapon("Побита бутилка", 65)
botlle.set_description("Розбита")
petrovuch.set_item(botlle)

current_room = railway

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
            fight_with = main_hero.choose_item()

            # Do I have this item?
            if main_hero.items:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if random.randint(0, 2):
                        main_hero.set_item(inhabitant.item)

                    if inhabitant.get_defeated() == 3:
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
    elif command == 'trade' and isinstance(inhabitant, game.Friend) \
        and inhabitant.trade(main_hero.choose_item()):
        main_hero.set_item(inhabitant.trade(main_hero.choose_item()))

        print(f'у вашому рюкзаку є: {" ".join([elem.name for elem in main_hero.items])}')
        print("Ви успішно помінялися речами")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            main_hero.set_item(item)
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
