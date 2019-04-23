import pygame
from pygame.locals import *
import random


def judgement(player_score, ai_socre):
    Win, Draw, Loose = 1, 2, 3
    if player_score > 21 and ai_socre > 21:
        return Draw
    elif player_score == 21 and ai_socre == 21:
        return Draw
    elif player_score > 21 >= ai_socre:
        return Loose
    elif player_score <= 21 < ai_socre:
        return Win
    elif player_score > ai_socre:
        return Win
    elif player_score == ai_socre:
        return Draw
    else:
        return Loose


def Message(text, size, *color):
    my_font = pygame.font.SysFont("arial", size)
    surface = my_font.render(text, True, color)
    return surface
