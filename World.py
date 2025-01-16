class World:
    def __init__(self):
        self.objects = []
        self.world_size = (600, 600)
        self.fps = 30
    
    def print(self):
        for obj in self.objects:
            print(obj)

    def get_objects(self):
        return self.objects

    def add_object(self, obj):
        self.objects.append(obj)
    
    def get_distance(self, obj_1, obj_2):
        pos_1 = obj_1.get_pos()
        pos_2 = obj_2.get_pos()
        return ((pos_1[0] - pos_2[0])**2 + (pos_1[1] - pos_2[1])**2)**0.5

    def check_collide(self, obj_1, obj_2):
        return self.get_distance(obj_1, obj_2) < obj_1.get_signature() + obj_2.get_signature()

    def get_is_collided(self, obj):
        for another_obj in self.objects:
            if another_obj != obj and self.check_collide(another_obj, obj):
                return True
        return False
    
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