from Infoclass import *
class Training:
    def __init__(self,action, duration, weight):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.M_IN_KM = 1000
        self.LEN_STEP = 0.65

    def get_distance(self):
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self):
        return self.get_distance() / self.duration

    def get_spent_calories(self):
        pass

    def get_training_type(self):
        pass

    def show_training_info(self):
        info = InfoMessage([self.get_training_type(), self.duration, self.get_distance(),self.get_mean_speed(),self.get_spent_calories()])
        return info

class Running(Training):
    def get_spent_calories(self):
        return (18 * self.get_mean_speed() - 20) * self.weight / self.M_IN_KM * self.duration*60

    def get_training_type(self):
        return 'RUN'

class SportsWalking(Training):
    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        return (0.035 * self.weight + (self.get_mean_speed()**2 // self.height) * 0.29 * self.weight)*self.duration*60

    def get_training_type(self):
        return 'WLK'

class Swimming(Training):

    def __init__(self, action, duration, weight, length_pool, count_pool):
        super().__init__(action, duration, weight)
        self.LEN_STEP = 1.38
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_training_type(self):
        return 'SWM'

    def get_mean_speed(self):
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self):
        return (self.get_mean_speed() + 1.1) * 2 * self.weight


