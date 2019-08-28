import pygame

class UISurfaceBase:
    def __init__(self, surface, position):
        self.m_Width = surface[0]
        self.m_Height = surface[1]
        self.m_PositionX = position[0]
        self.m_PositonY = position[1]