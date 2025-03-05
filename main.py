import os
import random
import time

class card:
    cardname = ''
    value = 0
    leftover = 4
    def __init__(self, cardname, value):
        self.cardname = cardname
        self.value = value
    def __str__(self):
        return self.cardname + "\n"

cards = [
card("Ace", 11),
card("King", 10),
card("Queen", 10),
card("Jack", 10),
card("Ten", 10),
card("Nine", 9),
card("Eight", 8),
card("Seven", 7),
card("Six", 6),
card("Five", 5),
card("Four", 4),
card("Three", 3),
card("Two", 2)
]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_castable_to_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def doesarraycontainat(array, value, loc):
    try:
        value_index = array.index(value)
    except:
        value_index = -1
    return value_index == loc
def makestringofwinners(winners):
    output = ''
    for i in winners:
        output += i.playerID + ', '

class Player:
    playercards = []
    wins = 0
    stillin = True
    def __init__(self, playerID):
        self.status = 0  # 0: nothing, 1: hitting, 2: out
        self.playercards = []  # Use instance-level attributes
        self.deal(2)
        self.playerID = playerID

    def deal(self, dealamount):
        cardcount = 0
        while True:
            if cardcount == dealamount:
                return
            current = random.randint(0, len(cards) - 1)
            if len(cards) > current and not cards[current].leftover == 0:
                self.playercards.append(cards[current])
                cards[current].leftover -= 1
                cardcount += 1
    def addcard(self):
        self.deal(1)
    def playplayer(self):
        if self.stillin == False:
            return 's'
        print('player' + str(self.playerID) + '\'s cards: ')
        print(f"\n{''.join(map(str, self.playercards))}")
        print(str(self.countcards()))
        playerstatus = ''
        while True:
            currentinput = input('hit(h) or stand(s): ')
<<<<<<< HEAD
            if currentinput == 'h' or currentinput == 's':
                playerstatus = currentinput
                break
            else:
                print('that was not a playable input \n')
        if playerstatus == 's':
            return 's'
        self.deal(1)
        print('player' + str(self.playerID) + '\'s cards: ')
        print(f"\n{''.join(map(str, self.playercards))}")
        if self.countcards() > 21:
            self.stillin = False
            print('bust')
            playerstatus = 'b'
        return playerstatus
=======
            if currentinput == 'h':
                playerstatus = 'h'
                self.addcard()
                print('player' + str(playerID) + '\'s cards: ')
                print(f"\n{''.join(map(str, self.playercards))}")
                if self.countcards() > 21:
                    playerstatus = 'b'
                break
            elif currentinput == 's':
                playerstatus = 's'
                break
            print('that was not a playable input \n')
        
>>>>>>> 8a5e007831689e8e0163aed879c8bbe6cedb9f69
    def countcards(self):
        #print(self.__str__())
        amount = 0
        countaces = 0
        for i in self.playercards:
            amount += i.value
            if i.cardname == "Ace":
                countaces += 1
        if amount > 21 and countaces > 0:
            for i in range(countaces):
                amount -= 10
                if amount < 21:
                    break
        return amount
    def reset(self):
        self.playercards = []
        self.deal(2)
        self.stillin = True
    def __str__(self):
        return f"Player's cards: \n{''.join(map(str, self.playercards))}"
        # + " " + str(len(self.playercards)

playercount = 0
players = []
shouldresetamount = True
while True:
    if shouldresetamount:
        while True:
            current = input('amount of players: ')
            iscurrent = is_castable_to_number(current)
            if iscurrent and int(current) > 1:
                print(current)
                playercount = int(current)
                break
    for i in range(playercount):
        players.append(Player(str(i)))
    standcount = 0
    counter = 0
    while True:
        if standcount == playercount:
            bestforwin = [players[0]]
            for i in players:
                if i.countcards() == bestforwin[0].countcards() and not i.playerID == players[0].playerID:
                    bestforwin.append(i)
                elif i.countcards() > bestforwin[0].countcards():
                    bestforwin = [i]
            if len(bestforwin) == 1:
                print(str(bestforwin[0].playerID) + ' wins!')
                break
<<<<<<< HEAD
            else:
                print(('tie between: ' + str(makestringofwinners(bestforwin)))[:-2])
            gamestatus = input('should the game be fully reset? (y) or (n) ')
            if gamestatus == 'y':
                shouldresetamount = True
            elif gamestatus == 'n':
                shouldresetamount = False
        for i in players:
            #print('currently on:' + str(i.playerID))
            if not i.stillin:
                continue
            currentoutput = i.playplayer()
            if currentoutput == 's':
                standcount += 1
            #time.sleep(3)
            #clear_terminal()
        #counter += 1
=======
        if not players[(counter % playercount) - 1].stillin:
            continue
        currentoutput = players[(counter % playercount) - 1].playplayer(counter % playercount)
        if currentoutput == 'b':
            players.remove((counter % playercount) - 1)
        #time.sleep(2)
        #clear_terminal()
        counter += 1
>>>>>>> 8a5e007831689e8e0163aed879c8bbe6cedb9f69
