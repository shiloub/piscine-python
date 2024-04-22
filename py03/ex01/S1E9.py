from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character:
take:
-one mandatory parameter first_name
-one optional parameter is_alive set to True"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Need to be implemented by the childs classes:
set is_alive to False"""
        pass


class Stark(Character):
    """Class representing a Strak"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character:
take:
-one mandatory parameter first_name
-one optional parameter is_alive set to True"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set is_alive to false"""
        self.is_alive = False
