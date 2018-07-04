# ANAGRAMS

This is a program that plays a solitaire game of *Anagrams*. This is a really fun word game you can play in person with any number of players (3-4 is best). 


## The Game:

The game starts with a set of Scrabble tiles spread out on the table, all face down. On your turn, you choose a tile and flip it face up into the center of the table for everyone to see. If at any time you see a word that can be made from the tiles in the center, you can call it out - regardless of whose turn it is - and claim that word. You then take the tiles and form the word in front of you, and it is your turn.

If - and this is the fun part - you see a way to take one or more tiles from the center and combine it with all the letters of an existing word (of yours or someone else's) to form a new word, you can *steal* that word, transforming it and making it longer. In the real game you must also change the *root* of the word, so simply adding an *s* to a noun or an *ed* to a verb is not allowed. (In the program, this is mimicked by requiring that the order of the letters change in some way during the steal.)

The game ends when all the tiles are flipped up and nobody sees any more words or steals they can make. The player with the most tiles is front of them wins (so longer words are worth more points).  


## The Code:

There are two scripts here: anagrams.py and anagramsplayer.py. The former is simply a search for all possible steals of a given word that you input. The latter is the main program, a perfect anagrams player. Watch all the amazing steals it can make! 

tiles_scrabble.txt is the set of tiles used in the game (which you could of course cutsomize). 

engmix_84k.txt is a dictionary of 84,000 English words (including pluralizations, conjugations etc) that the program uses. 

Enjoy!
