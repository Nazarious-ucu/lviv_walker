"""
lab4 task6
"""
import random

class Room:
    """
    class representation game room(street)
    """

    def __init__(self, name:str) -> None:
        """
        init func
        """
        self.name = name
        self.__room_desc = ''
        self.__conected_rooms = {}
        self.__character = None
        self.__item = None
        self.__link_rooms_info = ''

    def link_room(self, __o: object, direction: str):
        """
        connect room to another room
        """
        if isinstance(__o, Room):
            self.__conected_rooms[direction] = __o
            self.__link_rooms_info = '\n'.join(\
                [f'The {self.__conected_rooms[key].name} is {key}'\
                for key in self.__conected_rooms])

    def set_character(self, character: object):
        """
        setter of character
        """
        self.__character = character

    def set_item(self, item: object):
        """
        setter of item in room
        """
        self.__item = item

    def get_details(self):
        """
        getter of rooms details
        """
        print(self.name)
        print('-'*20)
        print(self.__room_desc)
        print(self.__link_rooms_info)

    def get_character(self):
        """
        getter of character in room
        """

        if self.__character:
            return self.__character

    def get_item(self):
        """
        getter of character in room
        """

        if self.__item:
            return self.__item

    def move(self, direction: str):
        """
        getter for room
        """
        if direction in self.__conected_rooms:
            return self.__conected_rooms[direction]

    def set_description(self, description: str):
        """
        setter game description
        """
        self.__room_desc = description

class Character:
    """
    class representation game room
    """

    def __init__(self, name: str, description: str) -> None:
        """
        init func
        """
        self.name = name
        self._desc = description
        self._conversation = ''
        self.weakness = ''
        self.item = None

    def set_conversation(self, conversation: str):
        """
        setter for conversation
        """
        self._conversation = conversation

    def set_weakness(self, weakness: str):
        """
        setter for weakness
        """
        self.weakness = weakness

    def describe(self):
        """
        output info about enemy in room
        """
        print(f'{self.name} is here')
        print(self._desc)

    def talk(self):
        """
        func to talk with enemy
        """
        return f'[{self.name} says]: {self._conversation}'

    def set_item(self, item: object):
        """
        setter for item for character
        """
        if isinstance(item, Item):
            self.item = item

class Item:
    """
    class representation item
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self._description = None
        self._life = 1

    def set_description(self, desc: str):
        """
        setter for description of item
        """
        self._description = desc

    def describe(self):
        """
        output info about item in room
        """
        print(f'The [{self.name}] is here', end=' - ')
        print(self._description)

    def get_name(self):
        """
        getter for name
        """
        if self.name:
            return self.name

    def using_item(self):
        """
        using item counter
        """
        self._life -= 1


class Veapon(Item):
    """
    class representation veapon
    """
    def __init__(self, name: str, power: int) -> None:
        super().__init__(name)
        self.power = power

    def describe(self):
        """
        output info about enemy in room
        """
        super().describe()
        print(self.power)
class HelpItem(Item):
    """
    class representation help item
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.cure_helth = 1

    def helth(self, __o: object):
        """
        healing hero
        """
        if isinstance(__o, Hero):
            self.cure_helth -= 1

class Friend(Character):
    """
    class representation enemy
    """

    def __init__(self, name: str, description: str) -> None:
        """
        init func
        """
        super().__init__(name, description)

    def trade(self, item: Item):
        """
        func for trade with main character
        """
        trade_item = self._item
        self._item = item
        return trade_item
class Hero(Character):
    """
    class representation veapon
    """

    def __init__(self, name: str, decs: str) -> None:
        super().__init__(name, decs)
        self.helth = 1
        self.items   = []

    def set_item(self, item: object):
       """
       setter for item
       """
       if isinstance(item, Item):
           self.items.append(item)

    def choose_item(self):
        print('Виберіть чим будете торгуватися:')
        for i, elem in enumerate(self.items, 1):
            print(f'{i}. {elem.name} power:', end=' ')
            if isinstance(elem, Veapon):
                print(elem.power, end='')
            print(' | ', end='')
        num = input('\n вибірть цифру зброї')
        return self.items[num - 1%len(self.items)]

class Enemy(Character):
    """
    class representation enemy
    """

    __defeated = 0

    def fight(self, __o: Hero):
        """
        func generate a fight between two characters
        """
        fight_with = __o.choose_item()
        win = random.choice([1]*fight_with.power + [0]*self._item.power)
        if win == 1:
            print(f'You fend {self.name} off with the {fight_with}')
            return True
        else:
            print(f'{self.name} crushes you, puny adventurer!')
            return False

    def get_defeated(self):
        """
        getter for defeated enemies
        """
        Enemy.__defeated =+ 1
        return Enemy.__defeated

    def losing_item(self):
        """
        remove item from enemy
        """
        self._item = None
