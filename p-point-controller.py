#!/usr/bin/python
import pygame
import math
import time

class World():
    def __init__(self):
        pygame.init()
        self.size = width, height = 320, 240
        self.screen = pygame.display.set_mode(self.size)
        self.dt = 0.05
        self.kp = 0.02
        self.mass = 0.25
        self.kinetic_energy = [0,0]
        self.current_pos = [0,0]

    def get_target(self):
        pos = pygame.mouse.get_pos()
        return [pos[0],pos[1]]

    def draw_points(self, target):
        lamp_head = self.apply_velocity(target)
        pygame.draw.line(self.screen, (10, 200, 150), (self.size[0], 0), lamp_head, 10)
        pygame.draw.circle(self.screen,(100,0,255),lamp_head,10)
        pygame.draw.circle(self.screen,(255,255,255),target,10)
        pygame.display.flip()
        pygame.draw.circle(self.screen, (0, 0, 0), (self.size[0]/2,self.size[1]/2,), 1000)

    def apply_velocity(self,target):
        avg_vel = self.calc_effort(target)
        move_to = [0,0]
        for x in range(2):
            self.current_pos[x] = self.current_pos[x] + avg_vel[x] * self.dt
            move_to[x] = int(self.current_pos[x])
        return move_to

    def calc_effort(self,target):
        effort = [0,0]
        for x in range(2):
            error = target[x] - self.current_pos[x]
            effort[x] = error * self.kp
        return effort

if __name__ == "__main__":
    world = World()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        target = world.get_target()
        world.draw_points(target)