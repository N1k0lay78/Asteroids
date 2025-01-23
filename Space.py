from Object import Object

class Space:
    def __init__(self):
        self.objects = [
            Object([300, 300], [0, 35])
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


    def update(self):
        for obj in self.objects:
            self.update_object(obj)


game = Space()
for i in range(300):
    game.update()
    print(game.objects[0].get_pos())