import pygame
from datetime import datetime

from uisurfacebase import UISurfaceBase
from textobject import TextObject

class TimeUI(UISurfaceBase):
    def __init__(self, surface, topLeftPosition, gameDisplay):
        super().__init__(surface, topLeftPosition, gameDisplay)

    def GetColor(self):
        return (255,0,0)

    def GetTimeString(self):
        return datetime.now().strftime("%H-%M-%S")

    def GetDateString(self):
        return datetime.now().strftime("%d-%b")

    def DisplayTime(self):
        timeText = self.GetTimeString()
        font = 'freesansbold.ttf'
        size = 80
        color = (0,0,0)
        offset = (0,-45)
        textObject = TextObject(timeText, font, size, color, self.m_Rect, offset)
        textObject.Display(self.m_Surface)

    def DisplayDate(self):
        dateText = self.GetDateString()
        font = 'freesansbold.ttf'
        size = 80
        color = (0,0,0)
        offset = (0,45)
        textObject = TextObject(dateText, font, size, color, self.m_Rect, offset)
        textObject.Display(self.m_Surface)

    def Update(self):
        super().Display()
        self.DisplayTime()
        self.DisplayDate()
