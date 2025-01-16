class Object:
    def __init__(self, pos, velocity, name, signature):
        self.pos = pos
        self.velocity = velocity
        self.name = name
        self.signature = signature
    
    def set_pos(self, pos):
        self.pos = pos[:]
    
    def set_velocity(self, velocity):
        self.velocity = velocity[:]
    
    def get_pos(self):
        return self.pos[:]

    def get_velocity(self):
        return self.velocity[:]
    
    def get_name(self):
        return self.name
    
    def get_signature(self):
        return self.signature
    
    def __repr__(self):
        return f"p:{self.pos}, v:{self.velocity} n:{self.name} r:{self.signature}"