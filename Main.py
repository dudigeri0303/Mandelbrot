import pygame
import Mandelbrot as mb

class RenderSurface(object):
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS', 25)

        self.width = 800
        self.height = 800
                
        self.window = pygame.display.set_mode((self.width, self.height))

        self.mousePos = pygame.mouse.get_pos()

        self.runing = True

        self.mandelbrot = mb.Mandelbrot("Textures/texture_5.jpg", self.font)

    def eventHandler(self):
        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runing = False
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    self.mousePos = pygame.mouse.get_pos()
                    self.mandelbrot.zoomIn(self.mousePos[0], self.mousePos[1])
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.mandelbrot = mb.Mandelbrot("Textures/texture_1.jpg", self.font)
                elif event.key == pygame.K_2:
                    self.mandelbrot = mb.Mandelbrot("Textures/texture_2.jpg", self.font)
                elif event.key == pygame.K_3:
                    self.mandelbrot = mb.Mandelbrot("Textures/texture_3.jpg", self.font)
                elif event.key == pygame.K_4:
                    self.mandelbrot = mb.Mandelbrot("Textures/texture_4.jpg", self.font)
                elif event.key == pygame.K_5:
                    self.mandelbrot = mb.Mandelbrot("Textures/texture_5.jpg", self.font)
                   
                elif event.key == pygame.K_r:
                    self.mandelbrot = mb.Mandelbrot(self.mandelbrot.textureName, self.font)

                elif event.key == pygame.K_SPACE:
                    if self.mandelbrot.displayInfo == True:
                        self.mandelbrot.displayInfo = False
                    else:
                        self.mandelbrot.displayInfo = True

                elif event.key == pygame.K_UP:
                    self.mandelbrot.incraseMaxIterations(self.font)
                elif event.key == pygame.K_DOWN:
                    self.mandelbrot.decraseMaxIterations(self.font)
                    
    def drawGame(self):
        self.window.fill("white")
        self.mandelbrot.drawMandelbort(self.window)
        if self.mandelbrot.displayInfo == True:
            self.mandelbrot.displayInfos(self.window, self.font)
        pygame.display.update()

    def updateGame(self):
        self.eventHandler()
    
    def gameLoop(self):
        while self.runing:
            self.updateGame()
            self.drawGame()
        pygame.quit()

def main():
    renderSurface = RenderSurface()
    renderSurface.gameLoop()

if __name__ == '__main__':
    main()