# -*- coding: utf-8 -*-
"""
region.py
Class for region, esentially the master model
"""
import engine
import protocol_pb2 as proto
import city
import Image

class Region(engine.Entity):
    def __init__(self):
        #self.accept("loginRequest", self.login)

        self.name = "Region"
        self.cities = []
        self.terrainTextureDB = {}

    def generate(self, hightMapPath=None, colorMapPath=None, cityMapPath=None, terrainTextureDB=None):
        """
        Generates region
        heightmap is a filepath for grayscale bitmap for heigh
        colormap is color bitmap for terrain texture
        terrainTextureDB is data on texture to use for color map
        Creates an unfounded city
        """
        # if no paramets are passed
        # default is two small, one large
        # one medium
        # two small
        x, y = 0, 0
        defaultCityMap = [[(255,0,0),(255,0,0),(0,0,255),(0,0,255),(0,0,255),(0,0,255)],
            [(0,255,0),(0,255,0),(0,0,255),(0,0,255),(0,0,255),(0,0,255)],
            [(0,255,0),(0,255,0),(0,0,255),(0,0,255),(0,0,255),(0,0,255)],
            [(255,0,0),(255,0,0),(0,0,255),(0,0,255),(0,0,255),(0,0,255)]]        
        
        # Default Heighmap
        # Default Colormap
            
        # Convert Bitmap to test list
        # If failure resort to default
        # TODO: Add error checking
        cityMap = []
        if cityMapPath:
            cityMapImage = Image.open(cityMapPath)
            imgX, imgY = cityMapImage.size
            for iX in range(imgX):
                row = []
                for iY in range(imgY):
                    row.append(cityMapImage.getpixel(iX, iY))
                cityMap.append(row)
        else:
            cityMap = defaultCityMap
        
        cityCounter = 1
        
        # Skip contians the pixles to skip over for the non small city sizes
        skip = []
        for row in cityMap:
            for pixel in row:
                if (x,y) not in skip:
                    name = "City " + str(cityCounter)
                    if pixel[0] is 255:
                        #print "Small"
                        c = city.City(name=name, size=1)
                    elif pixel[1] is 255:
                        #print "Medium"
                        c = city.City(name=name, size=2)
                        skip += [(x+1,y),
                            (x,y+1),(x+1,y+1)]
                    elif pixel[2] is 255:
                        #print "Large"
                        c = city.City(name=name, size=4)
                        skip += [(x+1,y),(x+2,y),(x+3,y),
                            (x,y+1),(x+1,y+1),(x+2,y+1),(x+3,y+1),
                            (x,y+2),(x+1,y+2),(x+2,y+2),(x+3,y+2),
                            (x,y+3),(x+1,y+3),(x+2,y+3),(x+3,y+3)]
                    c.position = (x,y)
                    c.id = cityCounter
                    self.cities.append(c)
                    cityCounter += 1
                x += 1
            x = 0
            y += 1
        # 6 Total
        print "Cities:", self.cities
        print "Total Cities:", len(self.cities)
    
    
    
    def loadCity(self, cityKey, playerName, password=""):
        """
        loads a city based on cityKey
        """
        self.cities(cityKey).login(playerName, password="")
    
    #def login(self, password, playerName, playerPassword):
    
    
    def syncCities(self):
        """
        Syncronizes intercity effects on a regulat basis
        """
    