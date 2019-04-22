import pygame
from pygame.locals import *
from sys import exit
import random
import Functions
import copy

# global variables
pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
player_handcard = []
ai_handcard = []
player_stand = False
ai_stand = False
Start = 0
ai_Hit = False
player_total_score = 5000
ai_total_score = 5000

# initial position
initial_position = {'x1': 1200, 'x2': 1332}
initial_position_player = {'x3': 1200, 'x4': 1200, 'x5': 1200, 'x6': 1200}
initial_position_ai = {'x3': 1200, 'x4': 1200, 'x5': 1200, 'x6': 1200}
player_card_position_y = 365
ai_card_position_y = 70

# Clock & Speed
clock = pygame.time.Clock()
speed = 800

# Set Image Resolution
screen_width = 1200
screen_height = 640

# initialize
pygame.init()
# generate screen
screen = pygame.display.set_mode([screen_width, screen_height])
# Set the name of the screen
pygame.display.set_caption('BlackJack')
# Load background and cards
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

# Generate Words
Hit_surface = Functions.Message('Hit', 25, 0, 0, 0)
Stand_surface = Functions.Message('Stand', 25, 0, 0, 0)
cont_surface = Functions.Message("Continue", 40, 0, 0, 0)
quit_surface = Functions.Message("Quit", 40, 0, 0, 0)
surface_100 = Functions.Message('100$', 20, 0, 0, 0)
surface_200 = Functions.Message('200$', 20, 0, 0, 0)
surface_500 = Functions.Message('500$', 20, 0, 0, 0)
surface_1000 = Functions.Message('1000$', 20, 0, 0, 0)
player_total_score_surface1 = Functions.Message("Your Money:", 25, 0, 0, 0)
ai_total_score_surface1 = Functions.Message("Computer's Money:", 25, 0, 0, 0)
player_total_score_surface3 = Functions.Message("$", 25, 0, 0, 0)
ai_total_score_surface3 = Functions.Message("$", 25, 0, 0, 0)
New_game = Functions.Message('New Game', 40, 0, 0, 0)
Player_surface = Functions.Message("You",40,0,0,0)
AI_surface = Functions.Message("Computer",35,0,0,0)


def Dealing(pool):
    # release a poker and delete the card in the pool
    return pool.pop(random.randint(0, len(pool) - 1))


def Conditional_Dealing(pool):
    # Make sure the initial cards are not larger than 21
    player_handcard.append(Dealing(pool))
    ai_handcard.append(Dealing(pool))
    while player_handcard[0] + player_handcard[1] > 21:
        pool.append(player_handcard[1])
        del player_handcard[1]
        player_handcard.append(Dealing(pool))
    while ai_handcard[0] + ai_handcard[1] > 21:
        pool.append(ai_handcard[1])
        del ai_handcard[1]
        ai_handcard.append(Dealing(pool))
    return player_handcard, ai_handcard


def Drawcard_player(cardnum, pos1, pos2):
    cardnum -= 1
    if player_handcard[cardnum] == 1:
        screen.blit(card1, (pos1, pos2))
    elif player_handcard[cardnum] == 2:
        screen.blit(card2, (pos1, pos2))
    elif player_handcard[cardnum] == 3:
        screen.blit(card3, (pos1, pos2))
    elif player_handcard[cardnum] == 4:
        screen.blit(card4, (pos1, pos2))
    elif player_handcard[cardnum] == 5:
        screen.blit(card5, (pos1, pos2))
    elif player_handcard[cardnum] == 6:
        screen.blit(card6, (pos1, pos2))
    elif player_handcard[cardnum] == 7:
        screen.blit(card7, (pos1, pos2))
    elif player_handcard[cardnum] == 8:
        screen.blit(card8, (pos1, pos2))
    elif player_handcard[cardnum] == 9:
        screen.blit(card9, (pos1, pos2))
    elif player_handcard[cardnum] == 10:
        screen.blit(card10, (pos1, pos2))
    elif player_handcard[cardnum] == 11:
        screen.blit(card11, (pos1, pos2))
    elif player_handcard[cardnum] == 12:
        screen.blit(card12, (pos1, pos2))
    elif player_handcard[cardnum] == 13:
        screen.blit(card13, (pos1, pos2))


def Drawcard_ai(cardnum, pos1, pos2):
    cardnum -= 1
    if ai_hide[cardnum] == 1:
        screen.blit(card1, (pos1, pos2))
    elif ai_hide[cardnum] == 2:
        screen.blit(card2, (pos1, pos2))
    elif ai_hide[cardnum] == 3:
        screen.blit(card3, (pos1, pos2))
    elif ai_hide[cardnum] == 4:
        screen.blit(card4, (pos1, pos2))
    elif ai_hide[cardnum] == 5:
        screen.blit(card5, (pos1, pos2))
    elif ai_hide[cardnum] == 6:
        screen.blit(card6, (pos1, pos2))
    elif ai_hide[cardnum] == 7:
        screen.blit(card7, (pos1, pos2))
    elif ai_hide[cardnum] == 8:
        screen.blit(card8, (pos1, pos2))
    elif ai_hide[cardnum] == 9:
        screen.blit(card9, (pos1, pos2))
    elif ai_hide[cardnum] == 10:
        screen.blit(card10, (pos1, pos2))
    elif ai_hide[cardnum] == 11:
        screen.blit(card11, (pos1, pos2))
    elif ai_hide[cardnum] == 12:
        screen.blit(card12, (pos1, pos2))
    elif ai_hide[cardnum] == 13:
        screen.blit(card13, (pos1, pos2))
    elif ai_hide[cardnum] == 'cardback':
        screen.blit(cardback, (pos1, pos2))


def Drawcard_player_else():
    if len(player_handcard) >= 3:
        Drawcard_player(3, initial_position_player['x3'], player_card_position_y)
        initial_position_player['x3'] -= distance_moved
        if initial_position_player['x3'] <= 468:
            initial_position_player['x3'] = 468
    if len(player_handcard) >= 4:
        Drawcard_player(4, initial_position_player['x4'], player_card_position_y)
        initial_position_player['x4'] -= distance_moved
        if initial_position_player['x4'] <= 600:
            initial_position_player['x4'] = 600
    if len(player_handcard) >= 5:
        Drawcard_player(5, initial_position_player['x5'], player_card_position_y)
        initial_position_player['x5'] -= distance_moved
        if initial_position_player['x5'] <= 732:
            initial_position_player['x5'] = 732
    if len(player_handcard) >= 6:
        Drawcard_player(6, initial_position_player['x6'], player_card_position_y)
        initial_position_player['x6'] -= distance_moved
        if initial_position_player['x6'] <= 864:
            initial_position_player['x6'] = 864


def Drawcard_ai_else():
    if len(ai_handcard) >= 3:
        Drawcard_ai(3, initial_position_ai['x3'], ai_card_position_y)
        initial_position_ai['x3'] -= distance_moved
        if initial_position_ai['x3'] <= 468:
            initial_position_ai['x3'] = 468
    if len(ai_handcard) >= 4:
        Drawcard_ai(4, initial_position_ai['x4'], ai_card_position_y)
        initial_position_ai['x4'] -= distance_moved
        if initial_position_ai['x4'] <= 600:
            initial_position_ai['x4'] = 600
    if len(ai_handcard) >= 5:
        Drawcard_ai(5, initial_position_ai['x5'], ai_card_position_y)
        initial_position_ai['x5'] -= distance_moved
        if initial_position_ai['x5'] <= 732:
            initial_position_ai['x5'] = 732
    if len(ai_handcard) >= 6:
        Drawcard_ai(6, initial_position_ai['x6'], ai_card_position_y)
        initial_position_ai['x6'] -= distance_moved
        if initial_position_ai['x6'] <= 864:
            initial_position_ai['x6'] = 864


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
    global initial_position
    global initial_position_player
    global initial_position_ai
    global ai_condition
    pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    player_handcard = []
    ai_handcard = []
    player_stand = False
    ai_stand = False
    ai_Hit = False
    player_handcard.append(Dealing(pool))
    ai_handcard.append(Dealing(pool))
    Conditional_Dealing(pool)
    ai_hide = ['cardback', ai_handcard[1]]
    cont_surface = Functions.Message("Continue", 40, 0, 0, 0)
    quit_surface = Functions.Message("Quit", 40, 0, 0, 0)
    initial_position = {'x1': 1200, 'x2': 1332}
    initial_position_player = {'x3': 1200, 'x4': 1200, 'x5': 1200, 'x6': 1200}
    initial_position_ai = {'x3': 1200, 'x4': 1200, 'x5': 1200, 'x6': 1200}
    ai_condition = Functions.Message("", 25, 0, 0, 0)


# initialize
player_handcard.append(Dealing(pool))
ai_handcard.append(Dealing(pool))
Conditional_Dealing(pool)
ai_hide = ['cardback', ai_handcard[1]]

while True:
    # Set FPS
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000
    distance_moved = time_passed_seconds * speed
    # Get mouse position
    mousepos = pygame.mouse.get_pos()
    # Display money
    player_total_score_surface2 = Functions.Message(str(player_total_score), 25, 0, 0, 0)
    ai_total_score_surface2 = Functions.Message(str(ai_total_score), 25, 0, 0, 0)
    screen.blit(player_total_score_surface1, (310, 578))
    screen.blit(player_total_score_surface2, (457, 580))
    screen.blit(player_total_score_surface3, (513, 580))
    screen.blit(ai_total_score_surface1, (310, 30))
    screen.blit(ai_total_score_surface2, (530, 32))
    screen.blit(ai_total_score_surface3, (586, 32))
    pygame.display.update()
    # Press Start to start game
    if Start == 0:
        screen.blit(background, (0, 0))
        screen.blit(chip100, (200, 400))
        screen.blit(chip200, (430, 400))
        screen.blit(chip500, (660, 400))
        screen.blit(chip1000, (890, 405))
        screen.blit(surface_100, (228, 438))
        screen.blit(surface_200, (458, 436))
        screen.blit(surface_500, (690, 437))
        screen.blit(surface_1000, (910, 438))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if 200 <= mousepos[0] <= 300 and 400 <= mousepos[1] <= 500:
                surface_100 = Functions.Message('100$', 20, 255, 255, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 1
            else:
                surface_100 = Functions.Message('100$', 20, 0, 0, 0)
            if 430 <= mousepos[0] <= 530 and 400 <= mousepos[1] <= 500:
                surface_200 = Functions.Message('200$', 20, 255, 255, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 2
            else:
                surface_200 = Functions.Message('200$', 20, 0, 0, 0)
            if 660 <= mousepos[0] <= 760 and 400 <= mousepos[1] <= 500:
                surface_500 = Functions.Message('500$', 20, 255, 255, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 3
            else:
                surface_500 = Functions.Message('500$', 20, 0, 0, 0)
            if 890 <= mousepos[0] <= 990 and 405 <= mousepos[1] <= 495:
                surface_1000 = Functions.Message('1000$', 20, 255, 255, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 4
            else:
                surface_1000 = Functions.Message('1000$', 20, 0, 0, 0)

    # Quit the game
    if Start == 5:
        screen.blit(background, (0, 0))
        if player_total_score > ai_total_score:
            win_surface = Functions.Message("You win!", 40, 0, 0, 0)
            screen.blit(win_surface, (600, 320))
        elif player_total_score < ai_total_score:
            loose_surface = Functions.Message("You Loose!", 40, 0, 0, 0)
            screen.blit(loose_surface, (600, 320))
        elif player_total_score == ai_total_score:
            draw_surface = Functions.Message("Draw!", 40, 0, 0, 0)
            screen.blit(draw_surface, (600, 320))
        screen.blit(New_game, (600, 420))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if 600 <= mousepos[0] <= 755 and 420 <= mousepos[1] <= 466:
                New_game = Functions.Message("New Game", 40, 255, 255, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Start = 0
                    reset()
                    player_total_score = 5000
                    ai_total_score = 5000
            else:
                New_game = Functions.Message("New Game", 40, 0, 0, 0)

    if 0 < Start < 5:
        # Counting player's and ai's score
        player_score = 0
        for i in player_handcard:
            player_score += i
        ai_score = 0
        for i in ai_handcard:
            ai_score += i

        # Draw elements
        screen.blit(background, (0, 0))
        screen.blit(Player_surface,(20,550))
        screen.blit(AI_surface,(5,20))
        player_score_surface1 = Functions.Message('Your score:', 25, 0, 0, 0)
        player_score_surface2 = Functions.Message(str(player_score), 25, 0, 0, 0)
        Drawcard_player(1, initial_position['x1'], player_card_position_y)
        Drawcard_ai(1, initial_position['x1'], ai_card_position_y)
        Drawcard_player(2, initial_position['x2'], player_card_position_y)
        Drawcard_ai(2, initial_position['x2'], ai_card_position_y)
        Drawcard_player_else()
        Drawcard_ai_else()
        screen.blit(player_score_surface1, (204, 305))
        screen.blit(player_score_surface2, (334, 307))
        screen.blit(Hit_button, (550, 580))
        screen.blit(Stand_button, (692, 580))
        screen.blit(Hit_surface, (592, 580))
        screen.blit(Stand_surface, (720, 580))

        initial_position['x1'] -= distance_moved
        initial_position['x2'] -= distance_moved
        if initial_position['x1'] <= 204:
            initial_position['x1'] = 204
        if initial_position['x2'] <= 336:
            initial_position['x2'] = 336

        # Check quit or Hit or Stand
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # Choose Continue or Quit
            if player_stand and ai_stand:
                if 740 <= mousepos[0] <= 895 and 240 <= mousepos[1] <= 286:
                    cont_surface = Functions.Message("Continue", 40, 255, 255, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Functions.judgement(player_score, ai_score) == 1:
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
                        elif Functions.judgement(player_score, ai_score) == 3:
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
                    cont_surface = Functions.Message("Continue", 40, 0, 0, 0)
                if 950 <= mousepos[0] <= 1021 and 240 <= mousepos[1] <= 286:
                    quit_surface = Functions.Message("Quit", 40, 255, 255, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Functions.judgement(player_score, ai_score) == 1:
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
                        elif Functions.judgement(player_score, ai_score) == 3:
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
                    quit_surface = Functions.Message("Quit", 40, 0, 0, 0)

            # Check Hit or Stand
            if 552 <= mousepos[0] <= 672 and 582 <= mousepos[1] <= 610 and player_score < 21:
                if not player_stand or not ai_stand:
                    Hit_surface = Functions.Message("Hit", 25, 255, 255, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player_handcard.append(Dealing(pool))
                        player_stand = False
                        ai_Hit = True
            elif player_score >= 21:
                Hit_surface = Functions.Message("Hit", 25, 192, 192, 192)
                player_stand = True
                if not ai_stand:
                    ai_Hit = True
            elif player_score < 21 and player_stand and ai_stand:
                Hit_surface = Functions.Message("Hit", 25, 192, 192, 192)
            else:
                Hit_surface = Functions.Message("Hit", 25, 0, 0, 0)

            if 694 <= mousepos[0] <= 814 and 582 <= mousepos[1] <= 610:
                if not player_stand or not ai_stand:
                    Stand_surface = Functions.Message("Stand", 25, 255, 255, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player_stand = True
                        ai_Hit = True
            elif player_stand and ai_stand:
                Stand_surface = Functions.Message("Stand", 25, 192, 192, 192)
            else:
                Stand_surface = Functions.Message("Stand", 25, 0, 0, 0)

        # ai Hit or Stand
        if ai_Hit:
            if ai_score <= 10:
                if random.randint(1, 100) <= 85:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                    ai_condition = Functions.Message("Computer Hit", 25, 0, 0, 0)
                else:
                    ai_stand = True
                    ai_Hit = False
                    ai_condition = Functions.Message("Computer Stand", 25, 0, 0, 0)
            elif 10 < ai_score <= 12:
                if random.randint(1, 100) <= 65:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                    ai_condition = Functions.Message("Computer Hit", 25, 0, 0, 0)
                else:
                    ai_stand = True
                    ai_Hit = False
                    ai_condition = Functions.Message("Computer Stand", 25, 0, 0, 0)
            elif 12 < ai_score <= 15:
                if random.randint(1, 100) <= 35:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                    ai_condition = Functions.Message("Computer Hit", 25, 0, 0, 0)
                else:
                    ai_stand = True
                    ai_Hit = False
                    ai_condition = Functions.Message("Computer Stand", 25, 0, 0, 0)
            elif 15 < ai_score <= 17:
                if random.randint(1, 100) <= 14:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                    ai_condition = Functions.Message("Computer Hit", 25, 0, 0, 0)
                else:
                    ai_stand = True
                    ai_Hit = False
                    ai_condition = Functions.Message("Computer Stand", 25, 0, 0, 0)
            elif 17 < ai_score <= 19:
                if random.randint(1, 100) <= 8:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                    ai_condition = Functions.Message("Computer Hit", 25, 0, 0, 0)
                else:
                    ai_stand = True
                    ai_Hit = False
                    ai_condition = Functions.Message("Computer Stand", 25, 0, 0, 0)
            elif 19 < ai_score <= 20:
                if random.randint(1, 100) <= 1:
                    ai_Hit = False
                    ai_stand = False
                    ai_handcard.append(Dealing(pool))
                    ai_condition = Functions.Message("Computer Hit", 25, 0, 0, 0)
                else:
                    ai_stand = True
                    ai_Hit = False
                    ai_condition = Functions.Message("Computer Stand", 25, 0, 0, 0)
            elif ai_score >= 21:
                ai_stand = True
                ai_Hit = False
                ai_condition = Functions.Message("Computer Stand", 25, 0, 0, 0)
            ai_hide = copy.copy(ai_handcard)
            ai_hide[0] = "cardback"

        try:
            screen.blit(ai_condition, (610, 32))
        except:
            pass

        if player_stand and ai_stand:
            if Functions.judgement(player_score, ai_score) == 1:
                Win_surface = Functions.Message("Win", 60, 0, 0, 0)
                screen.blit(Win_surface, (800, 100))
            elif Functions.judgement(player_score, ai_score) == 2:
                Draw_surface = Functions.Message("Draw", 60, 0, 0, 0)
                screen.blit(Draw_surface, (800, 100))
            elif Functions.judgement(player_score, ai_score) == 3:
                Loose_surface = Functions.Message("Loose", 60, 0, 0, 0)
                screen.blit(Loose_surface, (800, 100))
            ai_hide = ai_handcard
            ai_score_surface1 = Functions.Message("Computer score:", 25, 0, 0, 0)
            ai_score_surface2 = Functions.Message(str(ai_score), 25, 0, 0, 0)
            vs_surface = Functions.Message("VS", 25, 0, 0, 0)
            screen.blit(vs_surface, (370, 307))
            screen.blit(ai_score_surface1, (414, 305))
            screen.blit(ai_score_surface2, (604, 307))
            screen.blit(cont_surface, (740, 240))
            screen.blit(quit_surface, (950, 240))

        if player_total_score <= 0 or ai_total_score <= 0:
            Start = 5
