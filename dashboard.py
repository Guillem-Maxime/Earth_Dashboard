import pygame

from earthui import EarthUI
from timeui import TimeUI
from weatherui import WeatherUI

class Dashboard:
    def __init__(self, dashboardWidth, dashboardHeight, gameDisplay):
        self.m_Width = dashboardWidth
        self.m_Height = dashboardHeight

        self.m_EarthPart = EarthUI(self.ComputeHalfVertUISurface(), self.ComputeHalfUIPosition(0), gameDisplay)
        self.m_TimePart = TimeUI(self.ComputeQuarterUISurface(), self.ComputeQuarterUIPosition(1), gameDisplay)
        self.m_WeatherPart = WeatherUI(self.ComputeQuarterUISurface(), self.ComputeQuarterUIPosition(2), gameDisplay)

##################################
# Display / Update Methods Methods
##################################
    def Update(self):
        self.m_TimePart.Update()
        self.Display()
    
    def Display(self):
        self.m_EarthPart.Display()
        self.m_WeatherPart.Display()

##################################
# Surface Methods
##################################

    def ComputeQuarterUISurface(self):
        return (self.m_Width // 2, self.m_Height // 2)
    
    def ComputeHalfVertUISurface(self):
        return (self.m_Width // 2, self.m_Height)

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
    def ComputeHalfUIPosition(self, positionTag):
        return((2 * positionTag + 1) * self.m_Width // 4, self.m_Height // 2)

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
    def ComputeQuarterUIPosition(self, positionTag):
        if(positionTag == 0):
            return(self.m_Width // 4, self.m_Height // 4)
        elif(positionTag == 1):
            return(3 * self.m_Width // 4, self.m_Height // 4)
        elif(positionTag == 2):
            return(3 * self.m_Width // 4, 3 * self.m_Height // 4)
        else:
            return(self.m_Width // 4, 3 * self.m_Height // 4)
    