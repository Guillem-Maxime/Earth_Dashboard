import pygame

from uisurfacebase import UISurfaceBase

class WeatherUI(UISurfaceBase):
    def __init__(self, surface, position):
        super(UISurfaceBase, self).__init__(surface, position)