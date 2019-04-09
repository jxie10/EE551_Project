import pygame
from pygame.locals import *
from sys import exit
import random
import Functions



pool=[1,2,3,4,5,6,7,8,9,10,11,12,13]
player_handcard=[]
ai_handcard=[]
player_stand = False
ai_stand = True


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
Hit_button = pygame.image.load('resources/button.png')
Stand_button = pygame.image.load('resources/button.png')

#Generate Words
Hit_surface = Functions.Message('Hit',25,0,0,0)
Stand_surface = Functions.Message('Stand',25,0,0,0)
cont_surface = Functions.Message("Continue",40,0,0,0)


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
    except:pass

def reset():
    global pool
    global player_handcard
    global ai_handcard
    global player_stand
    global ai_stand
    global ai_hide
    global cont_surface
    pool=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    player_handcard=[]
    ai_handcard=[]
    player_stand = False
    ai_stand = True
    player_handcard.append(Dealing(pool))
    ai_handcard.append(Dealing(pool))
    Conditional_Dealing(pool)
    ai_hide=['cardback',ai_handcard[1]]
    cont_surface = Functions.Message("Continue",40,0,0,0)

player_handcard.append(Dealing(pool))
ai_handcard.append(Dealing(pool))
Conditional_Dealing(pool)
ai_hide=['cardback',ai_handcard[1]]



while True:
    #Counting player's and ai's score
    player_score = 0
    for i in player_handcard:
        player_score += i
    ai_score = 0
    for i in ai_handcard:
        ai_score += i

    #Draw elements
    screen.blit(background,(0,0))

    player_score_surface1 = Functions.Message('player score:',25,0,0,0)
    player_score_surface2 = Functions.Message(str(player_score),25,0,0,0)
    Drawcard_player(1,0,0)
    Drawcard_ai(1,0,250)
    Drawcard_player(2,132,0)
    Drawcard_ai(2,132,250)
    Drawcard_player_else(264,0)
    screen.blit(player_score_surface1,(800,300))
    screen.blit(player_score_surface2,(950,302))
    screen.blit(Hit_button,(500,300))
    screen.blit(Stand_button,(500,360))
    screen.blit(Hit_surface,(500,300))
    screen.blit(Stand_surface,(500,360))

    #Get mouse position
    mousepos = pygame.mouse.get_pos()

    #Check quit or Hit or Stand
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if player_stand and ai_stand:
            if 805 <= mousepos[0] <= 955 and 400 <= mousepos[1] <= 441:
                cont_surface = Functions.Message("Continue",40,255,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    reset()
                    player_score = 0
            else:
                cont_surface = Functions.Message("Continue",40,0,0,0)


        if 505<=mousepos[0]<=617 and 305<=mousepos[1]<=325 and player_score < 21:
            if not player_stand or ai_stand:
                Hit_surface = Functions.Message("Hit",25,255,255,0)
                Functions.Hit_or_Stand(event,player_handcard,pool)
                player_stand = False
        elif player_score >= 21:
            Hit_surface = Functions.Message("Hit",25,192,192,192)
            player_stand = True
        elif player_score < 21 and player_stand and ai_stand:
            Hit_surface = Functions.Message("Hit",25,192,192,192)
        else:
            Hit_surface = Functions.Message("Hit",25,0,0,0)

        if 505<=mousepos[0]<=617 and 365<=mousepos[1]<=385:
            if not player_stand or not ai_stand:
                Stand_surface = Functions.Message("Stand",25,255,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_stand = True
        elif player_stand and ai_stand:
            Stand_surface = Functions.Message("Stand",25,192,192,192)
        else:
            Stand_surface = Functions.Message("Stand",25,0,0,0)

    if player_stand and ai_stand:
        if Functions.judgement(player_score,ai_score) == 1:
            Win_surface = Functions.Message("You win",40,0,0,0)
            screen.blit(Win_surface,(800,100))
        elif Functions.judgement(player_score,ai_score) == 2:
            Draw_surface = Functions.Message("It's a draw",40,0,0,0)
            screen.blit(Draw_surface,(800,100))
        elif Functions.judgement(player_score,ai_score) == 3:
            Loose_surface = Functions.Message("You Loose",40,0,0,0)
            screen.blit(Loose_surface,(800,100))
        screen.blit(cont_surface,(800,400))

    pygame.display.update()







