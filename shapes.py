import pygame
import sys

screen1=pygame.display.set_mode((700,700))
pygame.display.set_caption("Shapes")

class Rectangle:
    def __init__(self,color,dimensions):
        self.color = color
        self.dimensions = dimensions
    def draw(self):
        pygame.draw.rect(screen1,self.color,self.dimensions)

reangle = Rectangle("Red",(100,100,75,200))
reangle1 = Rectangle("blue",(300,300,75,200))
reangle.draw()
reangle1.draw()


class Circle:
    def __init__(self,color,position,radi,width):
        self.color=color
        self.postion=position
        self.radi=radi
        self.width=width
    def draw(self):
        pygame.draw.circle(screen1,self.color,self.postion,self.radi,self.width)
    def grow(self,nuy):
        self.radi=self.radi+nuy
corcle = Circle("white",(500,500),50,0)
cercle = Circle("yellow",(500,40),60,6)


        
        




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            corcle.draw()
            cercle.draw()
        if event.type==pygame.MOUSEWHEEL:
            corcle.grow(2)
            cercle.grow(1)    
    pygame.display.update()