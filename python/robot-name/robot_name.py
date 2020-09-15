import random
import string


robo_names = []

class Robot:
    def __init__(self):
        self.set_name()

    
    def set_name(self):
        name = ""
        while name == "" or name in robo_names:
            name = ""
            name += 2 * random.choice(string.ascii_uppercase)
            name += str(random.randint(100, 999))
        robo_names.append(name)
        self.name = name
    
    def reset(self):
        curr_name = self.name
        self.set_name()
        robo_names.remove(curr_name)