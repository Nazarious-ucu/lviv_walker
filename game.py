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
                [f'The {self.__conected_rooms[key].room_name} is {key}'\
                for key in self.__conected_rooms])
        print('BAD ROOM')

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

class Character:
    """
    class representation game room
    """

    def __init__(self, name: str) -> None:
        """
        init func
        """
        self.name = name
        self.__desc = ''
        self.__conversation = ''
        self.weakness = ''
        self._item = None

    def set_conversation(self, conversation: str):
        """
        setter for conversation
        """
        self.__conversation = conversation

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
        print(self.__desc)

    def talk(self):
        """
        func to talk with enemy
        """
        return f'[{self.name} says]: {self.__conversation}'

    def set_item(self, item: object):
        """
        setter for item for character
        """
        if isinstance(item, Item):
            self._item = item

class Item:
    """
    class representation item
    """
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.__description = None
        self.power = power

    def set_description(self, desc: str):
        """
        setter for description of item
        """
        self.__description = desc

    def describe(self):
        """
        output info about item in room
        """
        print(f'The [{self.name}] is here', end=' - ')
        print(self.__description)

    def get_name(self):
        """
        getter for name
        """
        if self.name:
            return self.name


class Enemy(Character):
    """
    class representation enemy
    """

    def __init__(self, name: str) -> None:
        """
        init func
        """
        super().__init__(name)

    def fight(self, fight_with: object):
        """
        func generate a fight between two characters
        """
        win = random.choice([0, 0, 1, 1, 1])
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

class Friend(Character):
    """
    class representation enemy
    """

    def trade(self, item: Item):
        """
        func for trade with main character
        """
        trade_item = self._item
        self._item = item
        return trade_item
