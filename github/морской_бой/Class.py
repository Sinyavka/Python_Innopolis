class Ship:
    def __init__(self,x, y, gorizontal):
        self.x =x
        self.y = y
        self.gorizontal = gorizontal
        self.rip = [False]*self.get_length()

    def get_length(self) -> int:
        pass

    def check_alive(self):
        for i in range(len(self.rip)):
            if self.rip[i] is False:
                return True
        return False

    def display_name(self):
        pass


class Submarin(Ship):

    def get_length(self) -> int:
        return 1

    def __repr__(self):
        return 's'

    def display_name(self):
        return 'Submarine'

class Destroyer(Ship):

    def get_length(self) -> int:
        return 2

    def __repr__(self):
        return 'd'

    def display_name(self):
        return 'Destroyer'


class Cruiser(Ship):

    def get_length(self) -> int:
        return 3

    def __repr__(self):
        return 'c'

    def display_name(self):
        return 'Cruiser'


class Battleship(Ship):

    def get_length(self) -> int:
        return 4

    def __repr__(self):
        return 'b'

    def display_name(self):
        return 'Battleship'
