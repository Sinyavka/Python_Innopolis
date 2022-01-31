# Программный модуль фитнес-трекера, который обрабатывает данные для трех видов тренировок:
# для бега, спортивной ходьбы и плавания.


from Trainings import *

def read_package(workout_type, data):
    dct = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    type = dct[workout_type]
    return type(*data)

def main(training):
    info = training.show_training_info()
    print(info.get_message())

if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

