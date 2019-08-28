import pygame

class UISurfaceBase:
    def __init__(self, surface, position, gameDisplay):
        self.m_Width = surface[0]
        self.m_Height = surface[1]
        self.m_PositionX = self.ComputeTopLeftPositionX(position[0])
        self.m_PositionY = self.ComputeTopLeftPositionY(position[1])
        self.m_Surface = gameDisplay

    m_Padding = 10

    def Display(self):
        pygame.draw.rect(self.m_Surface, self.GetColor(), [self.m_PositionX, self.m_PositionY, self.m_Width - self.m_Padding, self.m_Height - self.m_Padding])

    def ComputeTopLeftPositionX(self, positionX):
        return positionX - self.m_Width / 2 + self.m_Padding // 2

    def ComputeTopLeftPositionY(self, positionY):
        return positionY - self.m_Height / 2 + self.m_Padding // 2