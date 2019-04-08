import pygame
from pygame.locals import *
from sys import exit
import random
import Functions



pool=[1,2,3,4,5,6,7,8,9,10,11,12,13]
player_handcard=[]
ai_handcard=[]
player_stand = False
ai_stand = False


#Set Image Resolution
screen_width = 1200
screen_height = 640

#initialize
pygame.init()
#generate screen
screen = pygame.display.set_mode([screen_width,screen_height])
#Set the name of the screen
pygame.display.set_caption('BlackJack')
#Load background and cards
background = pygame.image.load('resources/background.png')
card1 = pygame.image.load('resources/Card1.png')
card2 = pygame.image.load('resources/Card2.png')
card3 = pygame.image.load('resources/Card3.png')
card4 = pygame.image.load('resources/Card4.png')
card5 = pygame.image.load('resources/Card5.png')
card6 = pygame.image.load('resources/Card6.png')
card7 = pygame.image.load('resources/Card7.png')
card8 = pygame.image.load('resources/Card8.png')
card9 = pygame.image.load('resources/Card9.png')
card10 = pygame.image.load('resources/Card10.png')
card11 = pygame.image.load('resources/Card11.png')
card12 = pygame.image.load('resources/Card12.png')
card13 = pygame.image.load('resources/Card13.png')
cardback = pygame.image.load('resources/Cardback.png')

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

def Hit_or_Stand():
    if event.type == pygame.MOUSEBUTTONDOWN:
        player_handcard.append(Dealing(pool))
        return player_handcard

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

def reset():
    global pool
    global player_handcard
    global ai_handcard
    global player_stand
    global ai_stand
    global ai_hide
    pool=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    player_handcard=[]
    ai_handcard=[]
    player_stand = False
    ai_stand = False
    player_handcard.append(Dealing(pool))
    ai_handcard.append(Dealing(pool))
    Conditional_Dealing(pool)
    ai_hide=['cardback',ai_handcard[1]]

player_handcard.append(Dealing(pool))
ai_handcard.append(Dealing(pool))
Conditional_Dealing(pool)
ai_hide=['cardback',ai_handcard[1]]



while True:
    #Draw background
    player_score = 0
    for i in player_handcard:
        player_score += i
    ai_score = 0
    for i in ai_handcard:
        ai_score += i
    screen.blit(background,(0,0))
    Drawcard_player(1,0,0)
    Drawcard_ai(1,0,250)
    Drawcard_player(2,132,0)
    Drawcard_ai(2,132,250)
    Drawcard_player_else(264,0)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if player_stand and ai_stand:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    reset()
                    player_score = 0
        if player_score >= 21:
            player_stand = True
            ai_stand = True
            break
        Hit_or_Stand()

    if player_stand and ai_stand:
        if Functions.judgement(player_score,ai_score) == 1:
            print('Win')
        elif Functions.judgement(player_score,ai_score) == 2:
            print('Draw')
        elif Functions.judgement(player_score,ai_score) == 3:
            print('Loose')





    print(player_handcard,player_score,ai_score)




