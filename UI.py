from World import World
from Object import Object
import pygame
from random import randrange
from math import cos, pi, atan2, degrees
from time import time


class GameUI:
    def __init__(self):
        self.world = World()

        obj = Object(
            [self.world.world_size[0] / 2 , self.world.world_size[1] / 2], 
            [-30, 15], 
            "bg", 0
        )
        self.world.add_object(obj)

        for _ in range(15):
            obj = Object(
                [randrange(0, self.world.world_size[0]), randrange(0, self.world.world_size[1])], 
                [randrange(-50, 50), randrange(-50, 50)], 
                "cometa", 20
            )
            self.world.add_object(obj)
        
        self.ship = Object(
                [self.world.world_size[0] / 2 , self.world.world_size[1] / 2], 
                [0, 0],
                "player", 20
            )
        self.world.add_object(self.ship)

        self.bullets = []
        pygame.init()
        self.screen = pygame.display.set_mode(self.world.world_size)
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Астероид')
        self.clock = pygame.time.Clock()

        self.asteroid = pygame.image.load('asteroid.png')
        self.asteroid.set_colorkey((255,255,255))
        self.ship_sprite = pygame.image.load('ship.png')
        self.ship_sprite.set_colorkey((255,255,255))
        self.bullet_sprite = pygame.image.load('bullet.png')
        self.bullet_sprite.set_colorkey((255,255,255))
        self.background_sprite = pygame.transform.scale(pygame.image.load('pattern bg.jpg'), (1200, 1200))

    def input(self):
        v = [0, 0]
        gp = pygame.key.get_pressed()
        if gp[pygame.K_w]:
            v[1] = -40
        if gp[pygame.K_s]:
            v[1] = 40
        if gp[pygame.K_a]:
            v[0] = -40
        if gp[pygame.K_d]:
            v[0] = 40
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    bullet = Object(
                        self.ship.get_pos(), 
                        self.get_bullet_vector(),
                        "bullet", 5
                    )
                    self.bullets.append([bullet, time()])
                    self.world.add_object(bullet)
        if v[0] != 0 and v[1] != 0:
            v[0] *= cos(pi/4)
            v[1] *= cos(pi/4)
        self.ship.set_velocity(v)
    
    def get_bullet_vector(self):
        mouse_pos = pygame.mouse.get_pos()
        ship_pos = self.ship.get_pos()
        vector = [mouse_pos[0] - ship_pos[0], mouse_pos[1] - ship_pos[1]]
        dlina = (vector[0]**2 + vector[1]**2)**0.5
        bullet_speed = 100
        vector[0] *= bullet_speed/dlina
        vector[1] *= bullet_speed/dlina
        return vector

    def game_logic(self):
        if len(self.bullets) == 0:
            return
        for i in range(len(self.bullets) - 1, -1, -1):
            data = self.bullets[i]
            bullet, lived_time = data
            if time() - lived_time > 5:
                self.world.objects.remove(bullet)
                self.bullets.remove(data)
                continue
            collide_object = self.world.get_collide(bullet)
            if collide_object is not None:
                if collide_object.get_name() == "cometa":
                    self.world.objects.remove(collide_object)
                    self.world.objects.remove(bullet)
                    self.bullets.remove(data)

    def draw_world(self):
        name_to_sprite = {
            "cometa": self.asteroid, "player": self.ship_sprite, 
            "bullet": self.bullet_sprite, "bg": self.background_sprite
        }
        # self.screen.fill((255, 255, 255))
        for obj in self.world.get_objects():
            sprite = name_to_sprite[obj.get_name()]
            if obj.get_name() == "player":
                ship_pos = obj.get_pos()
                mouse_pos = pygame.mouse.get_pos()
                angle = degrees(atan2(mouse_pos[0] - ship_pos[0], mouse_pos[1] - ship_pos[1])) + 180
                sprite = pygame.transform.rotate(sprite, angle)
                sprite.set_colorkey((255,255,255))
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
            self.game_logic()

            pygame.display.update()
            self.clock.tick(30)


GameUI().run()