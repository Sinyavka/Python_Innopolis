from Class import *

class Factory_ship:

    @staticmethod
    def create(type_ship, x,y, gor):
        dct ={'Submarin':Submarin, 'Destroyer':Destroyer, 'Cruiser': Cruiser, 'Battleship': Battleship}
        type = dct[type_ship]
        return type(x,y,gor)