from Space import Space
from Object import Object
import pygame
from random import randrange


class GameUI:
    def __init__(self):
        self.space = Space()
        # создание космического корабля
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.space.world_size))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('SAMOKATSTEROIDS')
        self.asteroid_sprite = pygame.image.load('Samokat.png')
        self.asteroid_sprite.set_colorkey((255,255,255))
        # загружаем картинку космического корабля и пули

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
        # добавить отрисовку разных типов объектов
        self.screen.fill((255, 255, 255))
        for obj in self.space.objects:
            self.screen.blit(self.asteroid_sprite, obj.get_pos())
    
    def run(self):
        while True:
            self.input()

            self.space.update()

            self.draw_world()

            pygame.display.update()
            self.clock.tick(30)

GameUI().run()