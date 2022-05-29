#Author: Aarush Modi
#Date: March 15, 2021
#Purpose: To play the game Red Dog
import random

class TwoCard:
    def __init__(self,card1=2,card2=2):
        self.card1 = card1
        self.card2 = card2

#Author: Aarush Modi
#Date: March 15, 2021
#Purpose: To return a random number that represents a card between 2 and 14
#Input: N/A
#Output: The random number
def getCard():
    rndNumber = random.randrange(2,14)
    return rndNumber

#Author: Aarush Modi
#Date: March 15, 2021
#Purpose: To return the two integers of a given TwoCard object
#Input: TwoCard Object
#Output: Two integers between 2 and 14
def getHand():
    playerHand = TwoCard
    playerHand.card1 = getCard()
    playerHand.card2 = getCard()
    return playerHand

#Author: Aarush Modi
#Date: March 15, 2021
#Purpose: To determine the type of hand given the integer values of the cards
#Input: playerHand
#Output: Type of hand
def handType (playerHand):
    if playerHand.card1 == playerHand.card2:
        handType = "Pair"
    elif playerHand.card1 - playerHand.card2 == 1 or playerHand.card2 - playerHand.card1 == 1:
        handType = "Consecutive"
    else:
        handType = "Non-Consecutive"
    return handType

#Author: Aarush Modi
#Date: March 15, 2021
#Purpose: To determine the spread of the hand
#Input: Integer values of cards in hand
#Output: Spread of hand
def spread (card1,card2):
    if card1 - card2 == 0:
        spread = 0
    else:
        spread = ((card1 + 1) - card2)
        while spread < 0:
            spread = (spread * -1)
    return spread

#Author: Aarush Modi
#Date: March 15, 2021
#Purpose: To determine the payout of the spread
#Input: Spread
#Output: Payout
def payout(card1,card2):
    if spread(card1,card2) == 1:
        payout = 5
    elif spread(card1,card2) == 2:
        payout = 4
    elif spread(card1,card2) == 3:
        payout = 2
    else:
        payout = 1
    return payout

#Author: Aarush Modi
#Date: March 15, 2021
#Purpose: To determine if the third carde is between a given TwoCard Object
#Input: TwoCard Object, third card
#Output: True or False
def between(card1,card2,card3):
    if (card3 > card1 and card3 < card2) or (card3 > card2 and card3 < card1):
        return True
    else:
        return False

#MAIN
while True:
    purse = 100
    if purse > 0:
        firstBet = int(input("Enter bet amount: "))
        if firstBet > 1 and firstBet < purse:
            playerHand = getHand()
            print (playerHand.card1)
            print (playerHand.card2)
            if handType(playerHand) == "Pair":
                card3 = getCard()
                print("Your third card:" ,card3)
                if card3 == playerHand.card1:
                    print("YOU WIN")
                    purse = purse + (firstBet*11)
                    print ("Your Purse is: $", purse)
                else:
                    print ("TIE")
            elif handType(playerHand) == "Consecutive":
                print("Consecutive")
                print("Tie")
                print ("Your Purse is: $", purse)
            else:
                secondBet = int(input("Enter Second Bet: "))
                if secondBet < firstBet and secondBet < purse:
                    firstBet += secondBet
                    card3 = getCard()
                    print("Your third card:", card3)
                    if between(playerHand.card1,playerHand.card2,card3) == True:
                        print ("YOU WIN")
                        purse = purse + firstBet * payout(playerHand.card1,playerHand.card2)
                        print ("Your Purse is: $", purse)
                    else:
                        print("YOU LOSE")
                        purse -= firstBet
                        print ("Your Purse is: $", purse)
                    
                
    
