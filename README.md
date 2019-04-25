# **EE551 Project**
Wlecome to play Blackjack!
*(This Blackjack is a simplified version)*<br>
**Note:**  You need to install `pygame` to play this game. If you don't have, please follow the link:[Install pygame](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation)
## **Rules:**
1. Player and computer both have 5000$. Your goal is simple: win the money!
2. There are 13 cards, from 1 to 13. At the begining, player and computer will get 2 cards. The first card of computer is darkcard(which means it's invisiable).
3. In each round, player and computer will choose hit or stand in turn. When both of you choose stand, the game will count the point of the card in your hand and show the result.<br>
**Note:** You can not hit when your score is equal to or larger than 21. In that case you will automatically stand.
4. Results: <br>

|Win|Loose|Draw|
|:---|:---|:---|
|Both scores are smaller than 21 and your score is lager than computer's score|Both scores are smaller than 21 and your score is smaller than computer's score|Your socre is equal to computer's score, whether or not smaller or larger than 21|
|Your score is equal to or samller than 21 and computer's score is larger than 21|Your score is larger than 21 and computer's score is equal to or smaller than 21|Both scores are larger than 21|

5. When one loose all the money or player choose quit, the game is end.
## **How to play:**
1. Click on a chip to start game. Chip worth 100$, 200$, 500$, 1000$.
2. After get the initial 2 cards, left click on hit or stand in your turn, and then wait for the computer choose hit or stand.
3. After the game shows the result of each round, you can click continue to play next round or click quit.
4. If you choose quit, the game will show the final result. You can click New Game to start a new game.
