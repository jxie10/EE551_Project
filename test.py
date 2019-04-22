import pygame
import Functions

pygame.init()
surface_100 = Functions.Message("Computer score:", 25, 0, 0, 0)
size = surface_100.get_rect()
print(size.right,size.bottom)
