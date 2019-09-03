import pygame

class TextObject:
    def __init__(self, text, font, size, color, displayWidth, displayHeight):
        largeText = pygame.font.Font(font,size)
        textSurface = largeText.render(text, True, color)
        textSurface.get_rect().center = ((displayWidth/2),(displayHeight/2))
        self.m_TextSurf = textSurface
        self.m_TextRect = textSurface.get_rect()

    def Display(self, gameDisplay):
        gameDisplay.blit(self.m_TextSurf, self.m_TextRect)