from S1E9 import Character


class Baratheon(Character):
    """Class representing a Baratheon"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Baratheon's class"""
        self.is_alive = is_alive
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set is_alive to false"""
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of the character.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """
        Return a string representation of the character.
        """
        return self.__str__()


class Lannister(Character):
    """Class representing a Lannister"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Lannister's class"""
        self.is_alive = is_alive
        self.first_name = first_name
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Set is_alive to false"""
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of the character.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """
        Return a string representation of the character.
        """
        return self.__str__()

    @classmethod
    def create_lannister(self, first_name, is_alive=True):
        return Lannister(first_name, is_alive)
