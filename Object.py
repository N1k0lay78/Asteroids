class Object:
    def __init__(self, position, velocity):
        self.pos = position
        self.vel = velocity
        # добавить название объекта

    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def set_vel(self):
        # TODO
        pass
    
    def set_pos(self, new_pos):
        self.pos = new_pos