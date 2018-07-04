# ANAGRAMS

A program that plays a solitaire game of *Anagrams*, a fun word game you can play in real life with any number of players. 


## The Game:

The game starts with a set of Scrabble tiles spread out on the table, all face down. On your turn, you choose a tile and flip it face up into the center of the table for everyone to see. If at any time you see a word that can be made from the tiles in the center, you can call it out - regardless of whose turn it is - and claim that word. You then take the tiles and form the word in front of you, and it is your turn. (Usually you play with a minimum word length, say 4 or 5 letters.) 

Now the fun part: if you see a way to add one or more tiles from the center to an existing word (of yours or someone else's) and rearrange the letters to form a new word, you can *steal* the original word, transforming it and making it longer. For example, if a someone has the word "clap", and there is an "e" in the center, you could steal their tiles and make the word "place". If someone had "galleries" and there was a "u" and a "t" in the center, you could make "legislature"! 

In the real game you must also change the *root* of the word, so simply adding an *s* to a noun or an *ed* to a verb is not allowed. (In the program, this is mimicked by requiring that the order of the letters change in some way during the steal.)

The game ends when all the tiles are flipped up and nobody sees any more words or steals they can make. The player with the most tiles is front of them wins (so longer words are worth more points).  


## The Code:

There are two scripts here: anagrams.py and anagramsplayer.py. The former executes a search for all possible steals of a given word that you input. The latter is the main program, a perfect 1-person anagrams player. The player uses a 5-letter minimum. 

tiles_scrabble.txt is the set of tiles used in the game (which you could of course cutsomize). 
engmix_84k.txt is a dictionary of 84,000 English words (including pluralizations, conjugations etc) that the program uses. 
Make sure all these files are in the same directory. 

To run the anagrams.py search, just navigate to the directory and type: "python anagrams.py" and then the word you want to look for. For example, "python anagrams.py cozy" returns:

> 29 possible steals found for cozy: ['coenzyme', 'coenzymes', 'cognizably', 'cozily', 'crystallization', 'desynchronize', 'desynchronized', 'desynchronizes', 'desynchronizing', 'electrolyze', 'electrolyzed', 'electrolyzing', 'piezoelectricity', 'psychoanalyze', 'psychoanalyzed', 'psychoanalyzing', 'recognizably', 'synchronization', 'synchronize', 'synchronized', 'synchronizer', 'synchronizers', 'synchronizes', 'synchronizing', 'unrecognizably', 'unsynchronized', 'zoologically', 'zootechny', 'zygotic']

To run the anagrams player, no input is required. Just type "python anagramsplayer.py" and let it rip! The order of the tiles is random, so every game will be different. At the end it will print out a summary of all the words and steals that it made. Enjoy!

