import pygame

class TextObject:
    def __init__(self, text, font, size, color, dimention, position):
        largeText = pygame.font.Font(font,size)
        textSurface = largeText.render(text, True, color)
        self.m_TextSurf = textSurface
        self.m_TextRect = self.m_TextSurf.get_rect()
        self.m_TextRect.center = dimention
        self.m_TextRect.x = position[0]
        self.m_TextRect.y = position[1]

    def __init__(self, text, font, size, color, rect, offset):
        largeText = pygame.font.Font(font,size)
        textSurface = largeText.render(text, True, color)
        self.m_TextSurf = textSurface
        self.m_TextRect = self.m_TextSurf.get_rect()
        newRect = self.m_TextRect.clamp(rect)
        newRect.centerx = rect.centerx + offset[0]
        newRect.centery = rect.centery + offset[1]
        self.m_TextRect = newRect

    def Display(self, gameDisplay):
        pygame.draw.rect(gameDisplay, (125, 125, 125), self.m_TextRect)
        gameDisplay.blit(self.m_TextSurf, self.m_TextRect)