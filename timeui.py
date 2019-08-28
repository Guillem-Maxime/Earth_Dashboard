import pygame

from uisurfacebase import UISurfaceBase

class TimeUI(UISurfaceBase):
    def __init__(self, surface, topLeftPosition, gameDisplay):
        super().__init__(surface, topLeftPosition, gameDisplay)

    def GetColor(self):
        return (255,0,0)