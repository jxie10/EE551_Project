import pygame
import Functions_and_classes

pygame.init()
surface_100 = Functions_and_classes.Message("Computer score:", 25, 0, 0, 0)
size = surface_100.get_rect()
print(size.right,size.bottom)
