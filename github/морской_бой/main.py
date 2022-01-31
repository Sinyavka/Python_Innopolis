# Реализована игра морской бой, ввод данных происходит через текстовый файл,
# в котором сначала записаны координаты расположения кораблей, а затем
# координаты по которым идут выстрелы.


from Factory_ship import *
def create_list():
    a = []
    for i in range(10):
        b = []
        for j in range(10):
            k = None
            b.append(k)
        a.append(b)
    return a


def place_ship(a,ship):
    if ship.gorizontal:
        for j in range(ship.y,ship.y+ship.get_length()):
            a[ship.x][j] = ship
    else:
        for i in range(ship.x,ship.x+ ship.get_length()):
            a[i][ship.y] = ship

def show_matrix(a):
    for row in a:
        for k in row:
            if k is None:
                print('.', end=' ')
            else:
                print(k,end=' ')
        print()

def check_shoot(a, shoot_x, shoot_y):
    if a[shoot_x][shoot_y] is None:
        print('miss')
    else:
        ship = a[shoot_x][shoot_y]
        if ship.check_alive() is False:
            print(f'{ship.display_name()} has already sunk')
        else:
            if ship.gorizontal is True:
                pal = shoot_y-ship.y
            else:
                pal = shoot_x - ship.x
            if ship.rip[pal] is True:
                print(f'{ship.display_name()} has already shot')
            else:
                ship.rip[pal] = True
                if ship.check_alive() is True:
                    print(f'{ship.display_name()} shot')
                else:
                    print(f'{ship.display_name()} sunk')



def main():
    a = create_list()
    f = open('xy', 'r')
    for i in range(10):
        type_ship, x, y, gor = f.readline().split()
        x = int(x)
        y = int(y)
        if gor == 'True':
            gor = True
        else:
            gor = False
        ship = Factory_ship.create(type_ship, x, y, gor)
        place_ship(a, ship)
    for line in f:
        shoot_x, shoot_y = line.split()
        check_shoot(a, int(shoot_x), int(shoot_y))


    f.close()
    show_matrix(a)

if __name__ == '__main__':
    main()

