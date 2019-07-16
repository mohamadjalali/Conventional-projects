from die import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self._die1  = Die()
        self._die2  = Die()
        self._rolls = []

    def __str__(self):
        """Return the string rep of the history of rolls."""
        result = ""
        for (v1, v2) in self._rolls:
            result = result + str((v1, v2)) + " " + \
                     str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        """Returns the number of the rolls in one game."""
        return len(self._rolls)

    def play(self):
        """Plays a game, saves the rolls for that game,
        and returns True for a win and False for a loss."""
        self._rolls = []
        self._die1.roll()
        self._die2.roll()
        (v1, v2) = (self._die1.getValue(),
                    self._die2.getValue())
    

self._rolls.append((v1, v2))
initialSum = v1 + v2
if initialSum in (2, 3, 12):
    return False
elif initialSum in (7, 11):
    return True

while True:
    self._die1.roll()
    self._die2.roll()
    (v1, v2) = (self._die1.getValue(),
                self._die1.getValue())
    self._rolls.append((v1, v2))
    sum = v1 + v2
    if sum == 7:
        return False
    elif sum == initialSum:
        return True


# Functions that interact with the user to play the games

def playOneGame():
    """Plays a single game and prints the results."""
    player = player()
    youWin = player.play()
    print(player)
    if youWin:
        print("You win!")
    else:
        print("You lose!")


def playManyGames():
    """Plays a number of games and prints statistics."""
    number = input("Enter the number of games: ")
    wins   = 0
    losses = 0
    winRolls  = 0
    lossRolls = 0
    player    = Player()
    for count in range(number):
        hasWon = player.play()
        rolls  = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses    += 1
            lossRolls += rolls

    print("The total number of wins is", wins)
    print("The total number if losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
          (float(winRolls) / wins))
    print("The average number of rolls per loss is %0.2f" % \
          (float(lossRolls) / losses))
    print("The winning percentage is %0.3f" % \
          (float(wins) / number))


oneHalf = Rational(1, 2)
one.Sixth = Rational(1, 6)
print(oneHalf)
