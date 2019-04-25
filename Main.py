import pygame
from sys import exit
import Functions_and_classes
from Functions_and_classes import Card, Player, AI

# global variables
player = Player([], 0, False, None)
ai = AI([], 0, False, False)
Start = 0
player_total_score = 5000
ai_total_score = 5000

# initial position
initial_position_x_player = {'x1': 1200, 'x2': 1332, 'x3': 1200, 'x4': 1200, 'x5': 1200, 'x6': 1200}
initial_position_x_ai = {'x1': 1200, 'x2': 1332, 'x3': 1200, 'x4': 1200, 'x5': 1200, 'x6': 1200}
player_card_position_y = 365
ai_card_position_y = 70

# Clock & Image speed
clock = pygame.time.Clock()
speed = 800

# Set Resolution
screen_width = 1200
screen_height = 640

# initialize
pygame.init()
# generate screen
screen = pygame.display.set_mode([screen_width, screen_height])
# Set the name of the screen
pygame.display.set_caption('BlackJack')
# Load Images
background = pygame.image.load('resources/background.png')
card1 = Card('resources/Card1.png', 1)
card2 = Card('resources/Card2.png', 2)
card3 = Card('resources/Card3.png', 3)
card4 = Card('resources/Card4.png', 4)
card5 = Card('resources/Card5.png', 5)
card6 = Card('resources/Card6.png', 6)
card7 = Card('resources/Card7.png', 7)
card8 = Card('resources/Card8.png', 8)
card9 = Card('resources/Card9.png', 9)
card10 = Card('resources/Card10.png', 10)
card11 = Card('resources/Card11.png', 11)
card12 = Card('resources/Card12.png', 12)
card13 = Card('resources/Card13.png', 13)
cardback = Card('resources/Cardback.png', 0)
cardpack = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13]
Hit_button = pygame.image.load('resources/button.png')
Stand_button = pygame.image.load('resources/button.png')
chip100 = pygame.image.load('resources/100$.png')
chip200 = pygame.image.load('resources/200$.png')
chip500 = pygame.image.load('resources/500$.png')
chip1000 = pygame.image.load('resources/1000$.png')

# Generate Words
Hit_surface = Functions_and_classes.Message('Hit', 25, 192, 192, 192)
Stand_surface = Functions_and_classes.Message('Stand', 25, 192, 192, 192)
cont_surface = Functions_and_classes.Message("Continue", 40, 0, 0, 0)
quit_surface = Functions_and_classes.Message("Quit", 40, 0, 0, 0)
surface_100 = Functions_and_classes.Message('100$', 20, 0, 0, 0)
surface_200 = Functions_and_classes.Message('200$', 20, 0, 0, 0)
surface_500 = Functions_and_classes.Message('500$', 20, 0, 0, 0)
surface_1000 = Functions_and_classes.Message('1000$', 20, 0, 0, 0)
player_total_score_surface1 = Functions_and_classes.Message("Your Money:", 25, 0, 0, 0)
ai_total_score_surface1 = Functions_and_classes.Message("Computer's Money:", 25, 0, 0, 0)
player_total_score_surface3 = Functions_and_classes.Message("$", 25, 0, 0, 0)
ai_total_score_surface3 = Functions_and_classes.Message("$", 25, 0, 0, 0)
New_game = Functions_and_classes.Message('New Game', 40, 0, 0, 0)
Player_surface = Functions_and_classes.Message("You", 40, 0, 0, 0)
AI_surface = Functions_and_classes.Message("Computer", 35, 0, 0, 0)
start_surface = Functions_and_classes.Message("Choose a chip to start", 40, 0, 0, 0)
turn_surface = Functions_and_classes.Message("", 30, 0, 0, 0)
ai_condition = Functions_and_classes.Message("", 25, 0, 0, 0)


def reset():
    global cardpack
    global cont_surface
    global quit_surface
    global initial_position_x_player
    global initial_position_x_ai
    global ai_condition
    global New_game
    global surface_100
    global surface_200
    global surface_500
    global surface_1000
    cardpack = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13]
    player.handcard = []
    ai.handcard = []
    player.stand = False
    ai.stand = False
    ai.hit = False
    player.dealing(cardpack)
    ai.dealing(cardpack)
    player.conditional_dealing(cardpack)
    ai.conditional_dealing(cardpack)
    ai.hidefirst(cardback)
    cont_surface = Functions_and_classes.Message("Continue", 40, 0, 0, 0)
    quit_surface = Functions_and_classes.Message("Quit", 40, 0, 0, 0)
    initial_position_x_player = {'x1': 1200, 'x2': 1332, 'x3': 1200, 'x4': 1200, 'x5': 1200, 'x6': 1200}
    initial_position_x_ai = {'x1': 1200, 'x2': 1332, 'x3': 1200, 'x4': 1200, 'x5': 1200, 'x6': 1200}
    ai_condition = Functions_and_classes.Message("", 25, 0, 0, 0)
    New_game = Functions_and_classes.Message('New Game', 40, 0, 0, 0)
    surface_100 = Functions_and_classes.Message('100$', 20, 0, 0, 0)
    surface_200 = Functions_and_classes.Message('200$', 20, 0, 0, 0)
    surface_500 = Functions_and_classes.Message('500$', 20, 0, 0, 0)
    surface_1000 = Functions_and_classes.Message('1000$', 20, 0, 0, 0)


# initialize
player.dealing(cardpack)
ai.dealing(cardpack)
player.conditional_dealing(cardpack)
ai.conditional_dealing(cardpack)
ai.hidefirst(cardback)

while True:
    # Set FPS
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000
    distance_moved = time_passed_seconds * speed
    # Get mouse position and detect if mouse is pressed
    mousepos = pygame.mouse.get_pos()
    mousepress = pygame.mouse.get_pressed()
    # Display money
    player_total_score_surface = Functions_and_classes.Message("Your money:" + str(player_total_score) + "$", 25, 0, 0,
                                                               0)
    ai_total_score_surface = Functions_and_classes.Message("Computer's money:" + str(ai_total_score) + "$", 25, 0, 0, 0)
    screen.blit(player_total_score_surface, (310, 578))
    screen.blit(ai_total_score_surface, (310, 30))
    pygame.display.update()

    # Choose chip to start
    if Start == 0:
        screen.blit(background, (0, 0))
        screen.blit(chip100, (200, 400))
        screen.blit(chip200, (430, 400))
        screen.blit(chip500, (660, 400))
        screen.blit(chip1000, (890, 405))
        screen.blit(start_surface, (409.5, 250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if 200 <= mousepos[0] <= 300 and 400 <= mousepos[1] <= 500:
            surface_100 = Functions_and_classes.Message('100$', 20, 255, 255, 0)
            if mousepress[0]:
                Start = 1
        else:
            surface_100 = Functions_and_classes.Message('100$', 20, 0, 0, 0)
        if 430 <= mousepos[0] <= 530 and 400 <= mousepos[1] <= 500 and player_total_score >= 200 <= ai_total_score:
            surface_200 = Functions_and_classes.Message('200$', 20, 255, 255, 0)
            if mousepress[0]:
                Start = 2
        elif player_total_score < 200 or ai_total_score < 200:
            surface_200 = Functions_and_classes.Message('200$', 20, 192, 192, 192)
        else:
            surface_200 = Functions_and_classes.Message('200$', 20, 0, 0, 0)
        if 660 <= mousepos[0] <= 760 and 400 <= mousepos[1] <= 500 and player_total_score >= 500 <= ai_total_score:
            surface_500 = Functions_and_classes.Message('500$', 20, 255, 255, 0)
            if mousepress[0]:
                Start = 3
        elif player_total_score < 500 or ai_total_score < 500:
            surface_500 = Functions_and_classes.Message('500$', 20, 192, 192, 192)
        else:
            surface_500 = Functions_and_classes.Message('500$', 20, 0, 0, 0)
        if 890 <= mousepos[0] <= 990 and 405 <= mousepos[1] <= 495 and player_total_score >= 1000 <= ai_total_score:
            surface_1000 = Functions_and_classes.Message('1000$', 20, 255, 255, 0)
            if mousepress[0]:
                Start = 4
        elif player_total_score < 1000 or ai_total_score < 1000:
            surface_1000 = Functions_and_classes.Message('1000$', 20, 192, 192, 192)
        else:
            surface_1000 = Functions_and_classes.Message('1000$', 20, 0, 0, 0)
        screen.blit(surface_100, (228, 438))
        screen.blit(surface_200, (458, 436))
        screen.blit(surface_500, (690, 437))
        screen.blit(surface_1000, (910, 438))

    # Quit the game
    if Start == 5:
        screen.blit(background, (0, 0))
        if player_total_score > ai_total_score:
            win_surface = Functions_and_classes.Message("You win!", 60, 0, 0, 0)
            screen.blit(win_surface, (487.5, 200))
        elif player_total_score < ai_total_score:
            loose_surface = Functions_and_classes.Message("You Loose!", 60, 0, 0, 0)
            screen.blit(loose_surface, (451, 200))
        elif player_total_score == ai_total_score:
            draw_surface = Functions_and_classes.Message("Draw!", 60, 0, 0, 0)
            screen.blit(draw_surface, (521, 200))

        # Start a new game
        screen.blit(New_game, (500, 320))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if 500 <= mousepos[0] <= 700 and 320 <= mousepos[1] <= 366:
            New_game = Functions_and_classes.Message("New Game", 40, 255, 255, 0)
            if mousepress[0]:
                Start = 0
                reset()
                player_total_score = 5000
                ai_total_score = 5000
        else:
            New_game = Functions_and_classes.Message("New Game", 40, 0, 0, 0)

    if 0 < Start < 5:
        # Counting player's and ai's score
        player.score = 0
        player.add_score()
        ai.score = 0
        ai.add_score()

        # Draw elements
        screen.blit(background, (0, 0))
        screen.blit(Player_surface, (20, 550))
        screen.blit(AI_surface, (5, 20))
        player_score_surface = Functions_and_classes.Message('Your score:' + str(player.score), 25, 0, 0, 0)
        player.display(initial_position_x_player, player_card_position_y, screen, distance_moved)
        ai.display(initial_position_x_ai, ai_card_position_y, screen, distance_moved)
        screen.blit(player_score_surface, (204, 305))
        screen.blit(Hit_button, (550, 580))
        screen.blit(Stand_button, (692, 580))
        screen.blit(Hit_surface, (592, 580))
        screen.blit(Stand_surface, (720, 580))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # Choose Continue or Quit
        if player.stand and ai.stand:
            if 740 <= mousepos[0] <= 895 and 240 <= mousepos[1] <= 286:
                cont_surface = Functions_and_classes.Message("Continue", 40, 255, 255, 0)
                if mousepress[0]:
                    player_total_score, ai_total_score = Functions_and_classes.counttotalscore(player.score, ai.score,
                                                                                               Start,
                                                                                               player_total_score,
                                                                                               ai_total_score)
                    reset()
                    Start = 0
                    player.score = 0
                    ai.score = 0
            else:
                cont_surface = Functions_and_classes.Message("Continue", 40, 0, 0, 0)
            if 950 <= mousepos[0] <= 1021 and 240 <= mousepos[1] <= 286:
                quit_surface = Functions_and_classes.Message("Quit", 40, 255, 255, 0)
                if mousepress[0]:
                    player_total_score, ai_total_score = Functions_and_classes.counttotalscore(player.score, ai.score,
                                                                                               Start,
                                                                                               player_total_score,
                                                                                               ai_total_score)
                    Start = 5
                    player.score = 0
                    ai.score = 0
            else:
                quit_surface = Functions_and_classes.Message("Quit", 40, 0, 0, 0)

        if Functions_and_classes.candecide(len(player.handcard), len(ai.handcard), initial_position_x_player,
                                           initial_position_x_ai):
            # Check Hit or Stand
            turn_surface, Hit_surface, Stand_surface = player.hit_or_stand(cardpack, mousepos, mousepress, ai,
                                                                           Hit_surface, Stand_surface)

        try:
            screen.blit(turn_surface, (830, 560))
        except:
            pass

        if Functions_and_classes.candecide(len(player.handcard), len(ai.handcard), initial_position_x_player,
                                           initial_position_x_ai):
            # ai Hit or Stand
            turn_surface, ai_condition = ai.Hit(cardpack, cardback, player, turn_surface, ai_condition)

        try:
            screen.blit(ai_condition, (610, 32))
        except:
            pass

        # Show the result
        if player.stand and ai.stand:
            if Functions_and_classes.judgement(player.score, ai.score) == 1:
                Win_surface = Functions_and_classes.Message("Win", 60, 0, 0, 0)
                screen.blit(Win_surface, (800, 100))
            elif Functions_and_classes.judgement(player.score, ai.score) == 2:
                Draw_surface = Functions_and_classes.Message("Draw", 60, 0, 0, 0)
                screen.blit(Draw_surface, (800, 100))
            elif Functions_and_classes.judgement(player.score, ai.score) == 3:
                Loose_surface = Functions_and_classes.Message("Loose", 60, 0, 0, 0)
                screen.blit(Loose_surface, (800, 100))
            ai.restore()
            ai_score_surface = Functions_and_classes.Message(" VS Computer score:" + str(ai.score), 25, 0, 0, 0)
            screen.blit(ai_score_surface, (357, 305))
            screen.blit(cont_surface, (740, 240))
            screen.blit(quit_surface, (950, 240))

        # When one's money is 0, quit the game
        if player_total_score == 0 or ai_total_score == 0:
            Start = 5
