# ANAGRAMS PROGRAM v1.0
# Finds all words in the dictionary that are valid steals of the input word
# Algorithm uses a map from letters to primes
# to convert stealability into divisibility!
# --------------------------------------------------------------

# Access the command line input
import sys


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
def encode(chstring, theprimes):
	codenumber = 1
	for ch in chstring:
		k = (ord(ch) - 97) #ascii number. ord(a) = 97, ord(b) = 98...
		# if 0 <= k and k <= 25:   #make sure it's a regular lower-case letter
		p = theprimes[k]
		# else: p = 107	# z-->103. So the next prime, 107, will be our
		# catch-all code for an unrecognized character.
		codenumber *= p
	return codenumber


# Return a list of all valid steals of the input word ("keyword")
def findsteals(keyword):
	steal_list = []  # list starts empty

	theprimes = list_primes(200)
	# should only need 26, but there might be weird characters in the dictionary
	# like accents or capitals or whatever, so this way we get them all
	# and we don't have to bother checking that every character is valid ( commented out in encode() )

	codenumber = encode(keyword, theprimes)  #encode the word as a number

	# open the dictionary and begin checking.
	# right now we're using an 84,000-word list from this website:
	# http://www.gwicks.net/dictionaries.htm
	dictionary = load_dictionary('engmix_84k.txt') #formats it as a list

	for word in dictionary:
		# for each potential steal, first check that it's longer than the keyword.
		if len(word) > len(keyword):
			# if so, encode it
			# then check if it is divisible by the keyword's codenumber.
			if encode(word, theprimes) % codenumber == 0:
				# if so, add it to the steal_list
				steal_list.append(word)
	# end for loop

	return steal_list


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


# Check if input is a valid character string
def is_string(s):
	try:
		str(s)
		return True
	except ValueError:
		return False


# Main function, called upon launch
def main():
	# check that only a single word has been entered
	if len(sys.argv) == 2:
		input = sys.argv[1]
		# check that it's a valid character string
		if is_string(input):
			inputword = str(input)
			#find the steals
			final_list = findsteals(inputword)
			print str(len(final_list)) + ' possible steals found for ' + inputword + ': ' + str(final_list)
		else:
			print 'invalid entry!'


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
