import os
import random

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

class Player:
    playercards = []
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
    def countcards(self):
        print(self.__str__())
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

    def __str__(self):
        return f"Player's cards: \n {' '.join(map(str, self.playercards))}"
        # + " " + str(len(self.playercards)

currentplayer = Player()
print(currentplayer.countcards())  # Calls __str__() implicitly