import pygame

import earthui
import timeui
import weatherui

class Dashboard:
    def __init__(self):
        self.m_EarthPart = EarthUI()
        self.m_TimePart = TimeUI()
        self.m_WeatherPart = WeatherUI()