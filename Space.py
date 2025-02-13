from Object import Object

class Space:
    def __init__(self):
        self.objects = [
            Object([300, 300], [0, 30], "aster", 25),
            Object([200, 300], [0, 50], "aster", 25),
            Object([100, 300], [0, 100], "aster", 25),
        ]
        self.world_size = (600, 600)
        self.dt = 1/30
    
    def update_object(self, obj: Object):
        pos = obj.get_pos()
        vel = obj.get_vel()
        pos[0] += vel[0] * self.dt
        pos[1] += vel[1] * self.dt

        pos[0] %= self.world_size[0]
        pos[1] %= self.world_size[1]

        obj.set_pos(new_pos=pos)

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def get_distance(self, obj_1, obj_2):
        pos1 = obj_1.get_pos()
        pos2 = obj_2.get_pos()
        a = pos2[1] - pos1[1]
        b = pos2[0] - pos1[0]
        distance = (a**2 + b**2)**0.5
        return distance

    def get_is_collided(self, obj_1):
        for obj_2 in self.objects:
            if obj_1 != obj_2 and obj_2.get_name() == "aster":
                if self.get_distance(obj_1, obj_2) <= obj_1.get_rad() + obj_2.get_rad():
                    return obj_2

    def update(self):
        for obj in self.objects:
            self.update_object(obj)


game = Space()
for i in range(300):
    game.update()
    print(game.objects[0].get_pos())