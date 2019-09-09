import pygame
from pyowm import OWM

from uisurfacebase import UISurfaceBase

#Get an API key otherwise it might not work
API_KEY = 'a8d618e73ff68e0fcfeae966ba48eba9'

PLACE_01 = 'Montpellier,FR'
PLACE_02 = 'Montreuil,FR'
PLACE_03 = 'Manosque,FR'
PLACE_04 = 'La Mure,FR'

class WeatherUI(UISurfaceBase):
    def __init__(self, surface, topLeftPosition, gameDisplay):
        super().__init__(surface, topLeftPosition, gameDisplay)
        self.InitOWM()

    def InitOWM(self):
        self.m_Owm = OWM(API_KEY)
        self.m_Owm = OWM(language='fr')
        #self.m_ObsList = self.m_Owm.three_hours_forecast(PLACE_01)

    def GetColor(self):
        return (0,255,0)