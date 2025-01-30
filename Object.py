class Object:
    def __init__(self, position, velocity, groot):
        self.pos = position
        self.vel = velocity
        self.name = groot

    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def get_name(self):
        return self.name
    
    def set_vel(self, new_vel):
        self.vel = new_vel

    def set_pos(self, new_pos):
        self.pos = new_pos

    