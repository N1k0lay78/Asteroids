from Object import Object
from World import World

obj = Object([0, 0], [3000, 3000], "cometa", 10)
world = World()
world.add_object(obj)
world.print()
world.update()
world.print()
world.update()
world.print()
world.update()
world.print()
world.update()
world.print()