import pygame

import earthui
import timeui
import weatherui

class Dashboard:
    def __init__(self, dashboardWidth, dashboardHeight):
        self.m_Width = dashboardWidth
        self.m_Height = dashboardHeight

        self.m_EarthPart = EarthUI(self.ComputeHalfVertUISurface(), self.ComputeHalfUIPosition(0))
        self.m_TimePart = TimeUI(self.ComputeQuarterUISurface(), self.ComputeQuarterUIPosition(1))
        self.m_WeatherPart = WeatherUI(self.ComputeQuarterUISurface(), self.ComputeQuarterUIPosition(2))

    def ComputeQuarterUISurface():
        return (m_Width / 2, m_Height /2)
    
    def ComputeHalfVertUISurface():
        return (m_Width / 2, m_Height)

#the positionTag is 0 for the left half and 1 for the right one
#  -------------------------------
#  |              |              |
#  |              |              |
#  |              |              |
#  |      0       |      1       |
#  |              |              |
#  |              |              |
#  |              |              |
#  -------------------------------
    def ComputeHalfUIPosition(positionTag):
        return((2*positionTag + 1)*m_Width/4, m_Height/2)

#the positionTag is 0 for the top left quarter and then on clockwise
#  -------------------------------
#  |              |              |
#  |      0       |      1       |
#  |              |              |
#  |-----------------------------|
#  |              |              |
#  |      3       |      2       |
#  |              |              |
#  -------------------------------
    def ComputeQuarterUIPosition(positionTag):
        if(positionTag == 0):
            return(m_Width/4, m_Height/4)
        elif(positionTag == 1):
            return(3 * m_Width/4, m_Height/4)
        elif(positionTag == 2):
            return(3 * m_Width/4, 3 * m_Height/4)
        else:
            return(m_Width/4, 3 * m_Height/4)
    