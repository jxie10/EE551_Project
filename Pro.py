import random

pool=[1,2,3,4,5,6,7,8,9,10,11,12,13]
player_handcard=[]
ai_handcard=[]
def Dealing(pool):
    #release a poker and delete the card in the pool
    return pool.pop(random.randint(0,len(pool)-1))

def Conditional_Dealing(pool):
    #Make sure the initial cards are not larger than 21
    if player_handcard[0]+player_handcard[1]>21:
        pool.append(player_handcard[1])
        del player_handcard[1]
        player_handcard.append(Dealing(pool))
        Conditional_Dealing(pool)
    elif ai_handcard[0]+ai_handcard[1]>21:
        pool.append(ai_handcard[1])
        del ai_handcard[1]
        ai_handcard.append(Dealing(pool))
        Conditional_Dealing(pool)
    else:
        return player_handcard,ai_handcard

def game():
    #player and ai get initial 2 cards
    player_handcard.append(Dealing(pool))
    ai_handcard.append(Dealing(pool))
    player_handcard.append(Dealing(pool))
    ai_handcard.append(Dealing(pool))
    Conditional_Dealing(pool)
    ai_hide=['*',ai_handcard[1]]
    print('Your Cards:',player_handcard,'\n''PC\'s Cards:',ai_hide)
    Hit_or_Stand()
    judgement(player_handcard,ai_handcard)

def judgement(player_handcard,ai_handcard):

def Hit_or_Stand():


print(Dealing(pool))
