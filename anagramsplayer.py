''' ANAGRAMS PROGRAM v2.0: PlayerOne
# Play a complete (perfect) solitaire game of anagrams!
# -------------------------------------------------------------- '''

# Access the command line input
import sys
# randomizer
import random


# Each Word has a string, a code number, and a list of all possible steals,
# which are generated when the Word is instantiated.
class Word:
    def __init__(self, chstring):
        self.mystring = chstring
        self.length = len(chstring)
        self.codenum = encode(chstring)
        self.mysteals = find_steals(chstring)
        #set of the individual characters
        self.mylist = [ch for ch in chstring]
        # keep track of the word's evolution
        self.myhistory = [chstring]

    # history goes present-->future. So 1st entry is the word itself
    def addhistory(self,string):
        self.myhistory.append(string)


# Return a list of the first n prime numbers
def list_primes(n):
	# note: this alrorithm could be much for efficient (sieve)
	# but we don't need very many primes so it doesn't much matter
	primelist = []
	count = 0
	k = 2	# k tracks which number we're checking for primeness
	while count < n:
		divisorfound = False
		d = 2	# d tracks which divisor we're checking
		while d <= k**(0.5) and divisorfound == False:
			if k%d == 0:
				divisorfound = True  # we found a divisor for k. k is not prime!
			d += 1
		# end inner while loop
		if divisorfound == False: # if we never found one...
			count += 1            # we got a prime!
			primelist.append(k)   # add it to the list
		k += 1
	#end outer while loop
	return primelist


# Takes a character string and a list of numbers (primes), and returns an integer.
# The string is encoded as the product of the prime numbers associated with each letter:
# 'a' -> 2, 'b' -> 3, 'c' -> 5,..., 'z' -> 103.
def encode(chstring):
	codenumber = 1
	for ch in chstring:
		k = (ord(ch) - 97) #ascii number. ord(a) = 97, ord(b) = 98...
		p = theprimes[k]
		codenumber *= p
	return codenumber


# Return a list of all valid steals of the keyword
def find_steals(keyword):
	steal_list = []  # list starts empty
	codenumber = encode(keyword)  #encode the word as a number
	# open the dictionary and begin checking
	for word in dictionary:
		# for each potential steal, first check that it's longer than the keyword.
		if len(word) > len(keyword):
			# if so, encode it
			# then check if it is divisible by the keyword's codenumber.
			if encode(word) % codenumber == 0:
				# if so, add it to the steal_list
				steal_list.append(word)
	# end for loop
	return steal_list


# Return a list of all valid words contained within the keyword
def find_subwords(keyword):
	sub_list = []  # list starts empty
	codenumber = encode(keyword)  #encode the word as a number
	# open the dictionary and begin checking.
	for word in dictionary:
		# for each potential subword, first check that it's shorter *or equal* in length to the keyword.
		if min_word_length <= len(word) <= len(keyword):
			# if so, encode it, then check if it divides the keyword's codenumber.
			if codenumber % encode(word) == 0:
				# if so, add it to the sub_list
				sub_list.append(word)
	# end for loop
	return sub_list


# Take a file name, open it, and return a list of the words in that file
def load_dictionary(filename):
	txtfile = open(filename, 'r')  # 'r' is the "read" mode, as opposed to "write" or something else
	# Exactly how this is handled depends on the formatting of the dictionary.
	# For the engmix_84k word list, python's read() function interprets it as
	# a single character string, with spaces (rather than linebreaks) between each word.
	# The split() function creates a new list item every time it hits a space.
	word_list = txtfile.read().split()
	txtfile.close()
	return word_list


# Return a stack of the tiles in a random order
def load_tiles(filename):
    txtfile = open(filename, 'r')
    tile_stack = txtfile.read().split()
    random.shuffle(tile_stack)
    return tile_stack


# Subtract list a from list b
def subtract_lists(a,b):
    '''super important! cannot just write "remainder = b" or it will modify the actual list b!
    Must use list() to make a copy instead. Dammit python... '''
    remainder = list(b)
    for element in a:
        remainder.remove(element)
    return remainder


# Main function, called upon launch
def main():

    print 'Game Start:'

    global min_word_length
    min_word_length = 5
    # Normally we'd only need 26 primes for encoding, but there might be weird characters
    # in the dictionary like accents or capitals, so this way we catch them all
    global theprimes
    theprimes = list_primes(200)
    # right now we're using an 84,000-word list from this website:
	# http://www.gwicks.net/dictionaries.htm
    global dictionary
    dictionary = load_dictionary('engmix_84k.txt') #formats it as a list of strings
    center_tiles = []
    word_list = []
    bag = []
    #option to multiply the number of scrabble sets for longer game
    number_of_tile_sets = 1
    for k in range(number_of_tile_sets):
        # default tile distribution is that of scrabble (98 tiles)
        bag += load_tiles('tiles_scrabble.txt')

    '''game on!'''
    while len(bag) > 0:
    # can also write "while not bag". An empty list is False

        '''# 1) Flip                                        '''
        center_tiles.append(bag.pop()) #pop() removes the top one from the bag,
        # which has already been randomized
        print 'flip: ' + center_tiles[-1]

        ''' #2) Search for steals                           '''
        # create a Word version of the center tiles for convenience
        centerword = Word(center_tiles)
        # best_steal will be a 2-item list containing a word(Word) and a steal(string)
        best_steal = []

        # search for steals:
        for word in word_list:
            for steal in word.mysteals:
                # require steals to rearrange some letters! This prevents plurals, verb + 'ed', etc
                if word.mystring not in steal:
                    # if (word+center) contains steal, and steal contains word, we've found one
                    if (word.codenum * centerword.codenum) % encode(steal) == 0 and encode(steal) % word.codenum == 0:
                        # we found a steal! check if it's the best one yet
                        if not best_steal:
                            best_steal.append(word)
                            best_steal.append(steal)
                        elif len(steal) > len(best_steal[1]):
                            best_steal[0] = word
                            best_steal[1] = steal
        # end search loop for steals

        # if we found a steal: replace the old word, add the new, remove tiles used from the center
        if best_steal:
            old_word = best_steal[0]
            # turn the steal string into a new Word
            new_word = Word(best_steal[1])

            print 'steal: ' + str(old_word.mystring) + ' --> ' + str(new_word.mystring)

            tiles_used = subtract_lists(old_word.mylist, new_word.mylist)
            for tile in tiles_used: center_tiles.remove(tile)

            # update the new word's history
            for forefathers in old_word.myhistory:
                new_word.addhistory(forefathers)

            word_list.remove(old_word)
            word_list.append(new_word)

        else:
            ''' #3) If no steals, search for new words      '''
            possible_new_words = find_subwords(center_tiles)
            if possible_new_words:  #if it's not empty
                # make the longest word possible
                s = max(possible_new_words, key=len)
                new_word = Word(s) #the new word's steal list is auto-generated now
                word_list.append(new_word)

                print 'new word: ' + str(new_word.mystring)

                # REMOVE tiles from the center that we used
                for letter in new_word.mystring:
                    center_tiles.remove(letter)
            # otherwise do nothing, the turn is over.

        ''' #4) Print game state                            '''
        # print 'center: ' + str(center_tiles)
        # print 'words: ' + str([w.mystring for w in word_list])
        # print ' '
    # end master while loop
    print 'Game Over. '
    print '--------------------------------------'
    print 'Word Evolutions: '
    for word in word_list:
        history = ''
        for forefather in reversed(word.myhistory): history += (forefather + ' --> ')
        print history[:-5]
# end of main()


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
