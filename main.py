import random
class Enemy(character):
    def __init__(self, center_x, center_y, speed, change_x, change_y, time_to_change_direction):
        super().__init__(center_x, center_y, speed, change_x, change_y)
        self.time_to_change_direction = time_to_change_direction
    def pick_new_direction(self):
        directions = ["up" , "down" , "left" , "right"]
        direction = random.choice(directions)