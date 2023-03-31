import sys, os, os.path
from stat import *
# The following prints a random card from a card deck.
#
# cribbed from the ksh93 book, example from page 70
#
# chet@po.cwru.edu
#
os.system('declare -i i=0')
# load the deck
for suit in [clubs, diamonds, hearts, spades]:
    for n in [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]:
            card[i]="" + n + " of " + suit + ""
        i=i+1
        # let is not required with integer variables
# and print a random card
print("${card[RANDOM%52]}")
