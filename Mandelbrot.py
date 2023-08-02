import numpy as np
from numba import njit
import pygame

class Mandelbrot:
    def __init__(self, texture, font):
        self.center = (0, 0)
        self.distance = 4
        self.startX = self.center[0]-(self.distance/2)
        self.startY = self.center[1]+(self.distance/2)

        self.pixels = None

        self.xOffset = 0
        self.yOffset = 0

        self.size = 800
        
        self.maxIterations = 50

        self.zoomLevel = 1

        self.textureName = texture
        self.texture = pygame.image.load(self.textureName)
        self.textureSize = min(self.texture.get_size()) - 1
        self.textureArray = pygame.surfarray.array3d(self.texture)

        self.displayInfo = True
        self.maxIterText = font.render("Max Iterations :" + str(self.maxIterations), False, (0, 0, 0))
        self.textureTex = font.render("Texture :" + str(self.textureName[9:]), False, (0, 0, 0))
        self.zoomLevelText = font.render("Zoom Level: " + str(self.zoomLevel) + "x", False, (0, 0, 0))
        
        self.pixels = self.calcPixels(self.startX, self.startY, self.distance, self.size, self.maxIterations, self.textureSize, self.textureArray)



    @staticmethod
    @njit(fastmath=True)
    def calcPixels(x0, y0, distance, size, maxiterations, textureSize, textureArray):
        zReal = 0
        zImag = 0

        cReal = x0
        cImag = y0

        pixelList = np.zeros((size, size, 3), dtype=float)
        for i in range(size):
            for j in range(size):
                valueReal = zReal
                valueImag = zImag 
                iters = 0
                while(valueReal**2 + valueImag**2 <= 4 and iters < maxiterations):
                    vRtemp = ((valueReal * valueReal) - (valueImag * valueImag)) + cReal
                    valueImag = ((valueReal * valueImag) + (valueImag * valueReal)) + cImag
                    valueReal = vRtemp
                    iters += 1
                
                color = int(textureSize * iters / maxiterations)
                pixelList[i][j] = textureArray[color][color]
                cImag -= distance / size
        
            cImag = y0
            cReal += distance / size
        return pixelList

    def drawMandelbort(self, surface):
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[i])): 
                surface.set_at((i, j), (self.pixels[i][j][0], self.pixels[i][j][1], self.pixels[i][j][2]))

    def zoomIn(self, mx, my):
        mx -= self.size/2
        my = self.size/2-my

        mx = mx/(self.size/self.distance)
        my = my/(self.size/self.distance)

        self.center = (mx+self.xOffset, my+self.yOffset)

        self.xOffset += mx
        self.yOffset += my 

        self.distance/=2

        self.startX = self.center[0]-(self.distance/2)
        self.startY = self.center[1]+(self.distance/2)

        self.zoomLevel += 1

        self.pixels = self.calcPixels(self.startX, self.startY, self.distance, self.size, self.maxIterations, self.textureSize, self.textureArray)

    def displayInfos(self, surface, font):
        self.zoomLevelText = font.render("Zoom Level: " + str(self.zoomLevel) + "x", False, (0, 0, 0))

        surface.blit(self.maxIterText, (20, 750))
        surface.blit(self.textureTex, (280, 750))
        surface.blit(self.zoomLevelText, (590, 750))

    def incraseMaxIterations(self, font):
        if self.maxIterations < 3250:
            self.maxIterations += 400
        self.maxIterText = font.render("Max Iterations :" + str(self.maxIterations), False, (0, 0, 0))
        self.pixels = self.calcPixels(self.startX, self.startY, self.distance, self.size, self.maxIterations, self.textureSize, self.textureArray)

    def decraseMaxIterations(self, font):
        if self.maxIterations > 50:
            self.maxIterations -= 400
        self.maxIterText = font.render("Max Iterations :" + str(self.maxIterations), False, (0, 0, 0))
        self.pixels = self.calcPixels(self.startX, self.startY, self.distance, self.size, self.maxIterations, self.textureSize, self.textureArray)



