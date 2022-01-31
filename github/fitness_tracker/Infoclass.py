
class InfoMessage:
    def __init__(self,train):
        self.training_type = train[0]
        self.duration = train[1]
        self.distance = train[2]
        self.speed = train[3]
        self.calories = train[4]

    def get_message(self):
        return f'f Тип тренировки: {self.training_type}; Длительность: {self.duration} ч; Дистанция: {round(self.distance,2)} км; Ср.скорость: {round(self.speed,2)} км\ч; Потрачено ккал: {round(self.calories,2)}'

