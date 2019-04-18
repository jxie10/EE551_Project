import pygame
from pygame.locals import *
from sys import exit
import random
import Functions
import copy


pool=[1,2,3,4,5,6,7,8,9,10,11,12,13]
player_handcard=[]
ai_handcard=[]
player_stand = False
ai_stand = False
Start = 0
ai_Hit = False
player_total_score = 5000
ai_total_score = 5000

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
chip100 = pygame.image.load('resources/100$.png')
chip200 = pygame.image.load('resources/200$.png')
chip500 = pygame.image.load('resources/500$.png')
chip1000 = pygame.image.load('resources/1000$.png')

#Generate Words
Hit_surface = Functions.Message('Hit',25,0,0,0)
Stand_surface = Functions.Message('Stand',25,0,0,0)
cont_surface = Functions.Message("Continue",40,0,0,0)
quit_surface = Functions.Message("Quit",40,0,0,0)
surface_100 = Functions.Message('100$',20,0,0,0)
surface_200 = Functions.Message('200$',20,0,0,0)
surface_500 = Functions.Message('500$',20,0,0,0)
surface_1000 = Functions.Message('1000$',20,0,0,0)
player_total_score_surface1 = Functions.Message("player total score",25,0,0,0)
ai_total_score_surface1 = Functions.Message("ai total score",25,0,0,0)
New_game = Functions.Message('New Game',40,0,0,0)


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

def Drawcard_ai_else(initialposition1,initialposition2):
    try:
        for i in range(4):
            i += 3
            Drawcard_ai(i,initialposition1,initialposition2)
            initialposition1 += 132
    except:pass

def ai_Hit_or_Stand():
    global ai_Hit
    global ai_stand


def reset():
    global pool
    global player_handcard
    global ai_handcard
    global player_stand
    global ai_stand
    global ai_hide
    global cont_surface
    global quit_surface
    global ai_Hit
    pool=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    player_handcard=[]
    ai_handcard=[]
    player_stand = False
    ai_stand = False
    ai_Hit = False
    player_handcard.append(Dealing(pool))
    ai_handcard.append(Dealing(pool))
    Conditional_Dealing(pool)
    ai_hide=['cardback',ai_handcard[1]]
    cont_surface = Functions.Message("Continue",40,0,0,0)
    quit_surface = Functions.Message("Quit",40,0,0,0)

player_handcard.append(Dealing(pool))
ai_handcard.append(Dealing(pool))
Conditional_Dealing(pool)
ai_hide=['cardback',ai_handcard[1]]


while True:
    #Get mouse position
    mousepos = pygame.mouse.get_pos()
    #Display money
    player_total_score_surface2 = Functions.Message(str(player_total_score),25,0,0,0)
    ai_total_score_surface2 = Functions.Message(str(ai_total_score),25,0,0,0)
    screen.blit(player_total_score_surface1,(700,400))
    screen.blit(player_total_score_surface2,(850,400))
    screen.blit(ai_total_score_surface1,(700,450))
    screen.blit(ai_total_score_surface2,(850,450))
    pygame.display.update()
    #Press Start to start game
    if Start == 0:
        screen.blit(background,(0,0))
        screen.blit(chip100,(200,400))
        screen.blit(chip200,(400,400))
        screen.blit(chip500,(600,400))
        screen.blit(chip1000,(800,400))
        screen.blit(surface_100,(230,430))
        screen.blit(surface_200,(430,430))
        screen.blit(surface_500,(630,430))
        screen.blit(surface_1000,(830,430))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if 200 <= mousepos[0] <= 300 and 400 <= mousepos[1] <= 500:
                surface_100 = Functions.Message('100$',20,255,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 1
            else:
                surface_100 = Functions.Message('100$',20,0,0,0)
            if 400 <= mousepos[0] <= 500 and 400 <= mousepos[1] <= 500:
                surface_200 = Functions.Message('200$',20,255,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 2
            else:
                surface_200 = Functions.Message('200$',20,0,0,0)
            if 600 <= mousepos[0] <= 800 and 400 <= mousepos[1] <= 500:
                surface_500 = Functions.Message('500$',20,255,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 3
            else:
                surface_500 = Functions.Message('500$',20,0,0,0)
            if 800 <= mousepos[0] <= 900 and 400 <= mousepos[1] <= 500:
                surface_1000 = Functions.Message('1000$',20,255,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 4
            else:
                surface_1000 = Functions.Message('1000$',20,0,0,0)

    #Quit the game
    if Start == 5:
        screen.blit(background,(0,0))
        if player_total_score > ai_total_score:
            win_surface = Functions.Message("You win!",40,0,0,0)
            screen.blit(win_surface,(600,320))
        elif player_total_score < ai_total_score:
            loose_surface = Functions.Message("You Loose",40,0,0,0)
            screen.blit(loose_surface,(600,320))
        elif player_total_score == ai_total_score:
            draw_surface = Functions.Message("It's a draw",40,0,0,0)
            screen.blit(draw_surface,(600,320))
        screen.blit(New_game,(600,420))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if 600 <= mousepos[0] <= 755 and 420 <= mousepos[1] <= 466:
                New_game = Functions.Message("New Game",40,255,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 0
                    reset()
                    player_total_score = 5000
                    ai_total_score = 5000
            else:
                New_game = Functions.Message("New Game",40,0,0,0)

    if 0 < Start < 5:
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
        Drawcard_ai_else(264,250)
        screen.blit(player_score_surface1,(700,300))
        screen.blit(player_score_surface2,(850,302))
        screen.blit(Hit_button,(500,300))
        screen.blit(Stand_button,(500,360))
        screen.blit(Hit_surface,(500,300))
        screen.blit(Stand_surface,(500,360))



        #Check quit or Hit or Stand
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            #Choose Continue or Quit
            if player_stand and ai_stand:
                if 805 <= mousepos[0] <= 955 and 400 <= mousepos[1] <= 441:
                    cont_surface = Functions.Message("Continue",40,255,255,0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Functions.judgement(player_score,ai_score) == 1:
                            if Start == 1:
                                player_total_score += 100
                                ai_total_score -= 100
                            elif Start == 2:
                                player_total_score += 200
                                ai_total_score -= 200
                            elif Start == 3:
                                player_total_score += 500
                                ai_total_score -= 500
                            elif Start == 4:
                                player_total_score += 1000
                                ai_total_score -= 1000
                        elif Functions.judgement(player_score,ai_score) == 3:
                            if Start == 1:
                                player_total_score -= 100
                                ai_total_score += 100
                            elif Start == 2:
                                player_total_score -= 200
                                ai_total_score += 200
                            elif Start == 3:
                                player_total_score -= 500
                                ai_total_score += 500
                            elif Start == 4:
                                player_total_score -= 1000
                                ai_total_score += 1000
                        reset()
                        Start = 0
                        player_score = 0
                        ai_score = 0
                else:
                    cont_surface = Functions.Message("Continue",40,0,0,0)
                if 805 <= mousepos[0] <= 955 and 500 <= mousepos[1] <= 541:
                    quit_surface = Functions.Message("Quit",40,255,255,0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Functions.judgement(player_score,ai_score) == 1:
                            if Start == 1:
                                player_total_score += 100
                                ai_total_score -= 100
                            elif Start == 2:
                                player_total_score += 200
                                ai_total_score -= 200
                            elif Start == 3:
                                player_total_score += 500
                                ai_total_score -= 500
                            elif Start == 4:
                                player_total_score += 1000
                                ai_total_score -= 1000
                        elif Functions.judgement(player_score,ai_score) == 3:
                            if Start == 1:
                                player_total_score -= 100
                                ai_total_score += 100
                            elif Start == 2:
                                player_total_score -= 200
                                ai_total_score += 200
                            elif Start == 3:
                                player_total_score -= 500
                                ai_total_score += 500
                            elif Start == 4:
                                player_total_score -= 1000
                                ai_total_score += 1000
                        Start = 5
                        player_score = 0
                        ai_score = 0
                else:
                    quit_surface = Functions.Message("Quit",40,0,0,0)

            #Check Hit or Stand
            if 505<=mousepos[0]<=617 and 305<=mousepos[1]<=325 and player_score < 21:
                if not player_stand:
                    Hit_surface = Functions.Message("Hit",25,255,255,0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player_handcard.append(Dealing(pool))
                        player_stand = False
                        ai_Hit = True
            elif player_score >= 21:
                Hit_surface = Functions.Message("Hit",25,192,192,192)
                player_stand = True
                if not ai_stand:
                    ai_Hit = True
            elif player_score < 21 and player_stand and ai_stand:
                Hit_surface = Functions.Message("Hit",25,192,192,192)
            else:
                Hit_surface = Functions.Message("Hit",25,0,0,0)

            if 505<=mousepos[0]<=617 and 365<=mousepos[1]<=385:
                if not player_stand or not ai_stand:
                    Stand_surface = Functions.Message("Stand",25,255,255,0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player_stand = True
                        ai_Hit = True
            elif player_stand and ai_stand:
                Stand_surface = Functions.Message("Stand",25,192,192,192)
            else:
                Stand_surface = Functions.Message("Stand",25,0,0,0)


        #ai Hit
        if ai_Hit:
            if ai_score <= 10:
                if random.randint(1,100)<=85:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                else:
                    ai_stand = True
                    ai_Hit = False
            elif 10 < ai_score <= 12:
                if random.randint(1,100)<=65:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                else:
                    ai_stand = True
                    ai_Hit = False
            elif 12 < ai_score <= 15:
                if random.randint(1,100)<=40:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                else:
                    ai_stand = True
                    ai_Hit = False
            elif 15 < ai_score <= 17:
                if random.randint(1,100)<=14:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                else:
                    ai_stand = True
                    ai_Hit = False
            elif 17 < ai_score <= 19:
                if random.randint(1,100)<=8:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                else:
                    ai_stand = True
                    ai_Hit = False
            elif 19 < ai_score <= 20:
                if random.randint(1,100)<=1:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                else:
                    ai_stand = True
                    ai_Hit = False
            elif ai_score >= 21:
                ai_stand = True
                ai_Hit = False
            ai_hide = copy.copy(ai_handcard)
            ai_hide[0]="cardback"




        if player_stand and ai_stand:
            if Functions.judgement(player_score,ai_score) == 1:
                Win_surface = Functions.Message("Win",40,0,0,0)
                screen.blit(Win_surface,(800,100))
            elif Functions.judgement(player_score,ai_score) == 2:
                Draw_surface = Functions.Message("Draw",40,0,0,0)
                screen.blit(Draw_surface,(800,100))
            elif Functions.judgement(player_score,ai_score) == 3:
                Loose_surface = Functions.Message("Loose",40,0,0,0)
                screen.blit(Loose_surface,(800,100))
            ai_hide = ai_handcard
            ai_score_surface1 = Functions.Message("Ai score:",25,0,0,0)
            ai_score_surface2 = Functions.Message(str(ai_score),25,0,0,0)
            vs_surface = Functions.Message("VS",25,0,0,0)
            screen.blit(vs_surface,(900,300))
            screen.blit(ai_score_surface1,(925,300))
            screen.blit(ai_score_surface2,(975,302))
            screen.blit(cont_surface,(800,400))
            screen.blit(quit_surface,(800,500))

        if player_total_score <= 0 or ai_total_score <= 0:
            Start = 5

        print(Start)








