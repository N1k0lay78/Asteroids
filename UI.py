from Space import Space
from Object import Object
import pygame
from random import randrange


class GameUI:
    def __init__(self):
        self.space = Space()
        self.ship = Object([450, 237],[0,0], "player")
        self.space.add_object(self.ship)
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.space.world_size))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('SAMOKATSTEROIDS')
        self.asteroid_sprite = pygame.image.load('Samokat.png')
        self.asteroid_sprite.set_colorkey((255,255,255))
        self.stoit_sprite = pygame.image.load('Stoit.png')
        self.stoit_sprite.set_colorkey((255,255,255))
        self.kofe_sprite = pygame.image.load('kofe.png')
        self.kofe_sprite.set_colorkey((255,255,255))
    def input(self):
        # добавить перемешение корабля
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # добавить стрельбу
    
    def game_logic(self):
        # убирать патрон при привышении времени жизни и при попадании в астероид
        pass

    def draw_world(self):
        name_to_sprite = {"aster": self.asteroid_sprite, "player": self.stoit_sprite, "kofe" : self.kofe_sprite}
        self.screen.fill((255, 255, 255))
        for obj in self.space.objects:
            self.screen.blit(name_to_sprite[obj.get_name()], obj.get_pos())
    
    def run(self):
        while True:
            self.input()

            self.space.update()

            self.draw_world()

            pygame.display.update()
            self.clock.tick(30)

GameUI().run()