from World import World
from Object import Object
import pygame
from random import randrange


class GameUI:
    def __init__(self):
        self.world = World()
        for _ in range(15):
            obj = Object(
                [randrange(0, self.world.world_size[0]), randrange(0, self.world.world_size[1])], 
                [randrange(-50, 50), randrange(-50, 50)], 
                "cometa", 20
            )
            self.world.add_object(obj)
        
        pygame.init()
        self.screen = pygame.display.set_mode(self.world.world_size)
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Астероид')
        self.clock = pygame.time.Clock()

        self.asteroid = pygame.image.load('asteroid.png')
        self.asteroid.set_colorkey((255,255,255))

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    def draw_world(self):
        name_to_sprite = {"cometa": self.asteroid}
        self.screen.fill((255, 255, 255))
        for obj in self.world.get_objects():
            sprite = name_to_sprite[obj.get_name()]
            pos = obj.get_pos()
            pos[0] -= sprite.get_size()[0]/2
            pos[1] -= sprite.get_size()[1]/2
            self.screen.blit(sprite, pos)
            if self.world.get_is_collided(obj):
                color = (0, 255, 0)
            else:
                color = (255, 0, 255)
            pygame.draw.circle(self.screen, color, obj.get_pos(), obj.get_signature(), 2)
    
    def run(self):
        while True:
            self.input()
            self.draw_world()
            self.world.update()

            pygame.display.update()
            self.clock.tick(30)


GameUI().run()