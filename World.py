class World:
    def __init__(self):
        self.objects = []
        self.world_size = (300, 300)
        self.fps = 30
    
    def print(self):
        for obj in self.objects:
            print(obj)

    def add_object(self, obj):
        self.objects.append(obj)
    
    def update_object(self, obj):
        pos = obj.get_pos()
        vel = obj.get_velocity()
        # смещается на скорость
        pos[0] += vel[0] * (1/self.fps)
        pos[1] += vel[1] * (1/self.fps)
        # Замкнутый мир
        pos[0] %= self.world_size[0]
        pos[1] %= self.world_size[1]
        obj.set_pos(pos)

    def update(self):
        for obj in self.objects:
            self.update_object(obj)