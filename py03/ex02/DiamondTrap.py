from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing a King"""
    def __init__(self, first_name, is_alive=True):
        """King constructor"""
        super().__init__(first_name, is_alive)

    # @property
    def get_eyes(self):
        return self.eyes

    # @property
    def get_hairs(self):
        return self.hairs

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color
