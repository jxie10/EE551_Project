import pygame
import random
import copy


# Compare score
def judgement(player_score, ai_socre):
    win, draw, loose = 1, 2, 3
    if player_score > 21 and ai_socre > 21:
        return draw
    elif player_score == 21 and ai_socre == 21:
        return draw
    elif player_score > 21 >= ai_socre:
        return loose
    elif player_score <= 21 < ai_socre:
        return win
    elif player_score > ai_socre:
        return win
    elif player_score == ai_socre:
        return draw
    else:
        return loose


# Count total score
def counttotalscore(player_score, ai_score, Start, player_total_score, ai_total_score):
    if judgement(player_score, ai_score) == 1:
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
    elif judgement(player_score, ai_score) == 3:
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
    return player_total_score, ai_total_score


# Generate words surface
def Message(text, size, *color):
    my_font = pygame.font.SysFont("arial", size)
    surface = my_font.render(text, True, color)
    return surface


def candecide_player(len_player, pos_player):
    if len_player == 2 and pos_player['x2'] == 336:
        return True
    elif len_player == 3 and pos_player['x3'] == 468:
        return True
    elif len_player == 4 and pos_player['x4'] == 600:
        return True
    elif len_player == 5 and pos_player['x5'] == 732:
        return True
    elif len_player == 6 and pos_player['x6'] == 864:
        return True
    else:
        return False


def candecide_ai(len_ai, pos_ai):
    if len_ai == 2 and pos_ai['x2'] == 336:
        return True
    elif len_ai == 3 and pos_ai['x3'] == 468:
        return True
    elif len_ai == 4 and pos_ai['x4'] == 600:
        return True
    elif len_ai == 5 and pos_ai['x5'] == 732:
        return True
    elif len_ai == 6 and pos_ai['x6'] == 864:
        return True
    else:
        return False


# Decide whether player or ai can choose to stand or hit
def candecide(len_player, len_ai, pos_player, pos_ai):
    if candecide_player(len_player, pos_player) and candecide_ai(len_ai, pos_ai):
        return True
    else:
        return False


class Card(object):
    def __init__(self, surface, value):
        self.surface = pygame.image.load(surface)
        self.value = value


class Player(object):
    def __init__(self, handcard, score, stand, hit):
        self.handcard = handcard
        self.score = score
        self.stand = stand
        self.hit = hit

    # Dealing a card
    def dealing(self, cardpack):
        self.handcard.append(cardpack.pop(random.randint(0, len(cardpack) - 1)))

    # Make sure the initial card will less than 21
    def conditional_dealing(self, cardpack):
        self.dealing(cardpack)
        while self.handcard[0].value + self.handcard[1].value > 21:
            cardpack.append(self.handcard.pop(1))
            self.dealing(cardpack)
        return self.handcard

    # Sum score
    def add_score(self):
        for i in self.handcard:
            self.score += i.value
        return self.score

    # Display card on the screen
    def display_card(self, number, posx, posy, screen):
        screen.blit(self.handcard[number - 1].surface, (posx, posy))

    # Display all the cards
    def display(self, posx, posy, screen, distance):
        self.display_card(1, posx['x1'], posy, screen)
        posx['x1'] -= distance
        if posx['x1'] <= 204:
            posx['x1'] = 204
        self.display_card(2, posx['x2'], posy, screen)
        posx['x2'] -= distance
        if posx['x2'] <= 336:
            posx['x2'] = 336
        if len(self.handcard) >= 3:
            self.display_card(3, posx['x3'], posy, screen)
            posx['x3'] -= distance
            if posx['x3'] <= 468:
                posx['x3'] = 468
        if len(self.handcard) >= 4:
            self.display_card(4, posx['x4'], posy, screen)
            posx['x4'] -= distance
            if posx['x4'] <= 600:
                posx['x4'] = 600
        if len(self.handcard) >= 5:
            self.display_card(5, posx['x5'], posy, screen)
            posx['x5'] -= distance
            if posx['x5'] <= 732:
                posx['x5'] = 732
        if len(self.handcard) >= 6:
            self.display_card(6, posx['x6'], posy, screen)
            posx['x6'] -= distance
            if posx['x6'] <= 864:
                posx['x6'] = 864

    # Check Hit or Stand
    def hit_or_stand(self, cardpack, mousepos, mousepress, ai, hit_surface, stand_surface):
        turn_surface = Message("Your turn", 30, 0, 0, 0)
        if 552 <= mousepos[0] <= 672 and 582 <= mousepos[1] <= 610 and self.score < 21:
            if not self.stand or not ai.stand:
                hit_surface = Message("Hit", 25, 255, 255, 0)
                if mousepress[0]:
                    turn_surface = Message("", 30, 0, 0, 0)
                    self.dealing(cardpack)
                    self.stand = False
                    ai.hit = True
        elif self.score >= 21:
            turn_surface = Message("", 30, 0, 0, 0)
            hit_surface = Message("Hit", 25, 192, 192, 192)
            self.stand = True
            if not ai.stand:
                ai.hit = True
        elif self.score < 21 and self.stand and ai.stand:
            hit_surface = Message("Hit", 25, 192, 192, 192)
        else:
            hit_surface = Message("Hit", 25, 0, 0, 0)

        if self.stand and ai.stand:
            turn_surface = Message("", 30, 0, 0, 0)
            stand_surface = Message("Stand", 25, 192, 192, 192)
        elif 694 <= mousepos[0] <= 814 and 582 <= mousepos[1] <= 610:
            if not self.stand or not ai.stand:
                stand_surface = Message("Stand", 25, 255, 255, 0)
                if mousepress[0]:
                    self.stand = True
                    ai.hit = True
        elif self.score >= 21:
            stand_surface = Message("Stand", 25, 192, 192, 192)
        else:
            stand_surface = Message("Stand", 25, 0, 0, 0)
        return turn_surface, hit_surface, stand_surface


class AI(Player):
    # Hide the first card
    def hidefirst(self, card):
        self.hide = copy.copy(self.handcard)
        self.hide[0] = card

    # Show the first card
    def restore(self):
        self.hide = self.handcard

    def display_card(self, number, posx, posy, screen):
        screen.blit(self.hide[number - 1].surface, (posx, posy))

    # Computer dicide hit or stand and show computer's choice
    def Hit(self, cardpack, cardback, player, turn_surface, ai_condition):
        if self.hit:
            turn_surface = Message("", 30, 0, 0, 0)
            if self.score <= 10 and random.randint(1, 100) <= 90:
                self.stand = False
                self.dealing(cardpack)
                ai_condition = Message("Computer Hit", 25, 0, 0, 0)
            elif 10 < self.score <= 12 and random.randint(1, 100) <= 65:
                self.stand = False
                self.dealing(cardpack)
                ai_condition = Message("Computer Hit", 25, 0, 0, 0)
            elif 12 < self.score <= 15 and random.randint(1, 100) <= 35:
                self.stand = False
                self.dealing(cardpack)
                ai_condition = Message("Computer Hit", 25, 0, 0, 0)
            elif 15 < self.score <= 17 and random.randint(1, 100) <= 14:
                self.stand = False
                self.dealing(cardpack)
                ai_condition = Message("Computer Hit", 25, 0, 0, 0)
            elif 17 < self.score <= 19 and random.randint(1, 100) <= 8:
                self.stand = False
                self.dealing(cardpack)
                ai_condition = Message("Computer Hit", 25, 0, 0, 0)
            elif 19 < self.score <= 20 and random.randint(1, 100) <= 1:
                self.stand = False
                self.dealing(cardpack)
                ai_condition = Message("Computer Hit", 25, 0, 0, 0)
            elif player.score - player.handcard[0].value >= 21:
                self.stand = True
                ai_condition = Message("Computer Stand", 25, 0, 0, 0)
            else:
                self.stand = True
                ai_condition = Message("Computer Stand", 25, 0, 0, 0)
            self.hit = False
            self.hidefirst(cardback)
        return turn_surface, ai_condition
