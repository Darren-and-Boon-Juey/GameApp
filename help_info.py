from colors import color

blackjack_info = f"""
The following are the conventions we are using:
Dx: x of Diamonds. eg D9 represents 9 of Diamonds
Cx: x of Clubs. eg C1 represents Ace/One of Clubs
Hx: x of Hearts. eg HJ represents Jack of Hearts
Sx: x of Spades. eg S10 represents 10 of Spades




Below are some information to help you use the bot for blackjack games:

**discard**
- syntax: <command> <cards>
- example: discard C9D7
- explanation: C9 is used to represent Clubs 9, D7 is Diamonds 7 etc

**stats**
- syntax: <command> <house's revealed card> <your cards>
- example: stats C9 C10DJ
- explanation: House has a revealed 9 of Clubs while your current hand consists of 10 of Clubs and Jack of Diamonds
"""


mahjong_info = f"""
The following are the conventions that we are using:
Suites (range from 1 to 9):
  Cx	Character. eg C3 represents 3 Character
  Dx	Dots. eg D9 represents 9 Dots
  Bx	Bamboo. eg B2 represents 2 Bamboo

Winds:
  N	North
  S	South
  E	East
  W	West

Dragons:
  Zhong	Red Zhong character
  Fa	Green Fa character
  Baiban	Blue Baiban image

Bonus Tiles:
  Chicken	Chicken bonus tile
  Cat	Cat bonus tile
  Worm	Worm bonus tile
  Mouse	Mouse bonus tile

  (range from 1 to 4)
  Fx	Flower. eg F2 represents 2 Flower
  Sx	Season. eg S1 represents 1 Season




Below are some information to help you use the bot for mahjong games:

**discard**
- syntax: mahjong <wind> <command> <tile>
- example: Mahjong N discard C2
- explanation: C2 is used to represent 2 Character. This represents the North player discarding C2 into the permanent discard pile. If C2 is eaten or pong by another player, do not use discard C2, but rather discard on the tile actually going into the discard pile after the interception. Note that you can only discard 1 tile at a time, and it cannot be a bonus tile

**eat**
- syntax: mahjong <wind> <command> <tile>
- example: Mahjong E eat B2B3B4
- explanation: B2B3B4 is a suite of consecutive Bamboo tiles. Eat is when a tile is taken from the immediate previous wind's discard. Note, the discard command should be used after this to note down what tile is permanently discarded.

**pong**
- syntax: mahjong <wind> <command> <tile>
- example: Mahjong W pong D9
- explanation: D9D9D9 is a suite of identical Dots tiles. Pong is when a tile is taken from any player's discard, as long as the person already has at least 2 identical tiles. Note, the discard command should be used after this to note down what tile is permanently discarded.

**gang**
- syntax: mahjong <wind> <command> <tile>
- example: Mahjong W gang D9
- explanation: D9D9D9D9 is a suite of identical Dots tiles. Gang is when a tile is taken from any player's discard as long as the person already has at least 3 identical tiles, or a player draws the tiles themselves and reveals this suit for immediate payout. Note, the discard command should be used after this to note down what tile is permanently discarded.

**bonus**
- syntax: mahjong <wind> <command> <tile>
- example: Mahjong W bonus F4
- example: Mahjong N bonus Chicken
- explanation: F4 and chicken are bonus tiles, that do not count into the player's suit. This function is to enable tracking of remaining bonus tiles to help make decisions (E.g. if one should go for pinghu).

"""

generic_info = f"""
'/start': Runs the program / Refreshes the program
'/startblackjack': Starts a blackjack game session
'/startmahjong': Starts a mahjong game session
'/helpmahjong': Provides more information about how to input data for a mahjong game
'/helpblackjack': Provides more information about how to input data for a blackjack game
"""
