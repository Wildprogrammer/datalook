from random import choice
class RandomWalk():
    def __init__(self,num=5000):
        self.num=num
        self.x_value=[0]
        self.y_value=[0]
    def fill_walk(self):
        while self.num>len(self.x_value):
            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance
            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance
            if x_step==0 and y_step==0:
                continue
            self.x_value.append(self.x_value[-1]+x_step)
            self.y_value.append(self.y_value[-1]+y_step)


