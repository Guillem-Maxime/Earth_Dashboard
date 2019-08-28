import pygame

from uisurfacebase import UISurfaceBase

class EarthUI(UISurfaceBase):
    def __init__(self, surface, topLeftPosition, gameDisplay):
        super().__init__(surface, topLeftPosition, gameDisplay)

    def GetColor(self):
        return (0,0,255)