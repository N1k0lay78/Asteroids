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
        velocity = [0,0]
        gp = pygame.key.get_pressed()
        if gp[pygame.K_w]:
            velocity[1] = -40
        if gp[pygame.K_s]:
            velocity[1] = 40
        if gp[pygame.K_d]:
            velocity[0] = 40
        if gp[pygame.K_a]:
            velocity[0] = -40
        self.ship.set_vel(velocity)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    bullet = Object(self.ship.get_pos(), self.get_bullet_velocity(), "kofe" )
                    self.space.add_object(bullet)
                
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

    def get_bullet_velocity(self):
        mouse_pos = pygame.mouse.get_pos()
        ship_pos = self.ship.get_pos()
        dp_pos = [mouse_pos[0] - ship_pos[0], mouse_pos[1] - ship_pos[1]]
        dlinna = (dp_pos[0]**2 + dp_pos[1]**2) ** 0.5
        dp_pos[0] *= 100/dlinna
        dp_pos[1] *= 100/dlinna
        return dp_pos

GameUI().run()