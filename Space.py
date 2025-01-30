from Object import Object

class Space:
    def __init__(self):
        self.objects = [
            Object([300, 300], [0, 30], "aster"),
            Object([200, 300], [0, 50], "aster"),
            Object([100, 300], [0, 100], "aster"),
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
        pass

    def get_is_collided(self, obj):
        pass

    def update(self):
        for obj in self.objects:
            self.update_object(obj)


game = Space()
for i in range(300):
    game.update()
    print(game.objects[0].get_pos())