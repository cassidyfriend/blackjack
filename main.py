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

class Player:
    playercards = []
    wins = 0
    stillin = True
    def __init__(self):
        self.status = 0  # 0: nothing, 1: hitting, 2: out
        self.playercards = []  # Use instance-level attributes
        self.deal(2)

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
    def playplayer(self, playerID):
        print('player' + str(playerID) + '\'s cards: ')
        print(f"\n{''.join(map(str, self.playercards))}")
        print(str(self.countcards))
        playerstatus = ''
        while True:
            currentinput = input('hit(h) or stand(s): ')
            if currentinput[0].lower == 'h':
                playerstatus = 'h'
                break
            elif currentinput[0].lower == 's':
                playerstatus = 's'
                break
            print('that was not a playable input \n')
        
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

while True:
    playercount = 0
    players = []
    while True:
        current = input('amount of players: ')
        iscurrent = is_castable_to_number(current)
        if iscurrent and int(current) > 1:
            playercount = int(current)
            break
    for i in range(playercount - 1):
        players.append(Player())
    standcount = 0
    counter = 0
    while True:
        if standcount == playercount - 1:
            bestforwin = [players[0]]
            for i in players:
                if bestforwin[0].countcards() < i.countcards():
                    bestforwin[0] = i
                elif bestforwin[0].countcards() == i.countcards() and doesarraycontainat(bestforwin, i, 0):
                    bestforwin.append(i)
                i.reset()
            for i in bestforwin:
                i.wins += 1
            print(f"winner(s): \n{''.join(map(str, bestforwin))}")
            nextinput = ''
            counter = 0
            while True:
                nextinput = input('continue game(c) or reset(r)')
                if nextinput == 'continue' or nextinput == 'continue game' or nextinput == 'c' or nextinput == 'reset' or nextinput == 'r':
                    break
                print('that was not a usable input')
            if nextinput == 'reset' or nextinput == 'r':
                break
        if not players[(counter % playercount) - 1].stillin:
            continue
        while True:
            print('player ' + str(counter % playercount) + ':')
            print(str(players[(counter % playercount) - 1]))
            print(str(players[(counter % playercount) - 1].countcards()))
            currentstatus = input('hit(h) or stand(s) player ' + str((counter % playercount) - 1) + ':')
            if currentstatus == 'hit' or currentstatus == 'h':
                players[(counter % playercount) - 1].deal(1)
                print(str(players[(counter % playercount) - 1]))
                print(str(players[(counter % playercount) - 1].countcards()))
                if players[(counter % playercount) - 1].countcards() == 21:
                    players[(counter % playercount) - 1].wins += 1
                    counter = 0
                    for i in players:
                        i.reset()
                elif players[(counter % playercount) - 1].countcards() > 21:
                    print('bust')
                    players[(counter % playercount) - 1].stillin = False
                break
            elif currentstatus == 'stand' or currentstatus == 's':
                print(str(players[(counter % playercount) - 1]))
                print(str(players[(counter % playercount) - 1].countcards()))
                standcount += 1
                break
            print('that was not a playable input')
        
        #time.sleep(2)
        #clear_terminal()
        counter += 1