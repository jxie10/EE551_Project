import pygame
from pygame.locals import *
import random

def Dealing(pool):
    #release a poker and delete the card in the pool
    return pool.pop(random.randint(0,len(pool)-1))

def Conditional_Dealing(pool):
    #Make sure the initial cards are not larger than 21
    player_handcard.append(Dealing(pool))
    ai_handcard.append(Dealing(pool))
    while player_handcard[0]+player_handcard[1]>21:
        pool.append(player_handcard[1])
        del player_handcard[1]
        player_handcard.append(Dealing(pool))
    while ai_handcard[0]+ai_handcard[1]>21:
        pool.append(ai_handcard[1])
        del ai_handcard[1]
        ai_handcard.append(Dealing(pool))
    return player_handcard,ai_handcard

def Hit_or_Stand(event,player_handcard,pool):
    if event.type == pygame.MOUSEBUTTONDOWN:
        player_handcard.append(Dealing(pool))
        return player_handcard

def judgement(player_score,ai_socre):
    Win,Draw,Loose = 1,2,3
    if player_score > 21 and ai_socre > 21:
        return Draw
    elif player_score == 21 and ai_socre == 21:
        return Draw
    elif player_score > 21 and ai_socre <= 21:
        return Loose
    elif player_score <= 21 and ai_socre > 21:
        return Win
    elif player_score > ai_socre:
        return Win
    elif player_score == ai_socre:
        return Draw
    else:
        return Loose


def Drawcard_player(cardnum,pos1,pos2):
    cardnum -= 1
    if player_handcard[cardnum] == 1:
        screen.blit(card1,(pos1,pos2))
    elif player_handcard[cardnum] == 2:
        screen.blit(card2,(pos1,pos2))
    elif player_handcard[cardnum] == 3:
        screen.blit(card3,(pos1,pos2))
    elif player_handcard[cardnum] == 4:
        screen.blit(card4,(pos1,pos2))
    elif player_handcard[cardnum] == 5:
        screen.blit(card5,(pos1,pos2))
    elif player_handcard[cardnum] == 6:
        screen.blit(card6,(pos1,pos2))
    elif player_handcard[cardnum] == 7:
        screen.blit(card7,(pos1,pos2))
    elif player_handcard[cardnum] == 8:
        screen.blit(card8,(pos1,pos2))
    elif player_handcard[cardnum] == 9:
        screen.blit(card9,(pos1,pos2))
    elif player_handcard[cardnum] == 10:
        screen.blit(card10,(pos1,pos2))
    elif player_handcard[cardnum] == 11:
        screen.blit(card11,(pos1,pos2))
    elif player_handcard[cardnum] == 12:
        screen.blit(card12,(pos1,pos2))
    elif player_handcard[cardnum] == 13:
        screen.blit(card13,(pos1,pos2))



def Drawcard_ai(cardnum,pos1,pos2):
    cardnum -= 1
    if ai_hide[cardnum] == 1:
        screen.blit(card1,(pos1,pos2))
    elif ai_hide[cardnum] == 2:
        screen.blit(card2,(pos1,pos2))
    elif ai_hide[cardnum] == 3:
        screen.blit(card3,(pos1,pos2))
    elif ai_hide[cardnum] == 4:
        screen.blit(card4,(pos1,pos2))
    elif ai_hide[cardnum] == 5:
        screen.blit(card5,(pos1,pos2))
    elif ai_hide[cardnum] == 6:
        screen.blit(card6,(pos1,pos2))
    elif ai_hide[cardnum] == 7:
        screen.blit(card7,(pos1,pos2))
    elif ai_hide[cardnum] == 8:
        screen.blit(card8,(pos1,pos2))
    elif ai_hide[cardnum] == 9:
        screen.blit(card9,(pos1,pos2))
    elif ai_hide[cardnum] == 10:
        screen.blit(card10,(pos1,pos2))
    elif ai_hide[cardnum] == 11:
        screen.blit(card11,(pos1,pos2))
    elif ai_hide[cardnum] == 12:
        screen.blit(card12,(pos1,pos2))
    elif ai_hide[cardnum] == 13:
        screen.blit(card13,(pos1,pos2))
    elif ai_hide[cardnum] == 'cardback':
        screen.blit(cardback,(pos1,pos2))

def Drawcard_player_else(initialposition1,initialposition2):
    try:
        for i in range(4):
            i += 3
            Drawcard_player(i,initialposition1,initialposition2)
            initialposition1 += 132
    except:pygame.display.update()

def Message(text,size,*color):
    my_font = pygame.font.SysFont("arial",size)
    surface = my_font.render(text,True,color)
    return surface
