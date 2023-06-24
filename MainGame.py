from memoryGame import memoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRoulette




def welcome():
    print ("Hello and welcome to the World of Games (WoG).Here you can find many cool games to play.")
def load_game():
    game= int(input( "Please choose a game to play:\n 1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back\n 2. Guess Game - guess a number and see if you chose like the computer \n 3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
    while (game>3 or game<1):
        game=(input("wrong value please insert again between 1-3 only"))
    level=int(input("Please choose game difficulty from 1 to 5:\n"))
    while (level > 5 or game < 1):
        level=(input("wrong value please insert again between 1-2 only"))
    return game,level

def playGame(game, level):
    print("selected game number", game)
    if game == 1:
        memoryGame(level)
    elif game == 2:
        GuessGame(level)
    elif game == 3:
        CurrencyRoulette(level)
    else:
        print("Invalid game number")

welcome()
game,level=load_game()
playGame(game,level)