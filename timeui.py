import pygame
from datetime import datetime

from uisurfacebase import UISurfaceBase
import textdisplayutils

class TimeUI(UISurfaceBase):
    def __init__(self, surface, topLeftPosition, gameDisplay):
        super().__init__(surface, topLeftPosition, gameDisplay)

    def GetColor(self):
        return (255,0,0)

    def GetTimeString(self):
        return datetime.datetime.now().strftime("%H-%M-%s")

    def Update(self):
        super().Display()
        timeText = GetTimeString()
