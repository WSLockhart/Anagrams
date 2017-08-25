# ANAGRAMS PROGRAM
# Finds all words in the dictionary that are valid steals of the input word
# Algorithm uses a map from letters to primes
# to convert stealability into divisibility!
# --------------------------------------------------------------

# access the command line input
import sys


# return a list of the first n prime numbers.
# note: this alrorithm could be much for efficient (sieve)
# but we don't need very many primes so it doesn't much matter
def list_primes(n):
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


# returns an integer. This number will encode the input character string.
# It's the product of the primes associated with each letter:
# 'a' -> 2, 'b' -> 3, 'c' -> 5, 'd' -> 7...
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


# return a list of all valid steals on the input word ("keyword")
def findsteals(keyword):
	steal_list = []  # list starts empty

	theprimes = list_primes(200)
	# normally only need 26, but there might be weird characters in the dictionary
	# like accents or capitals or whatever, so this way we get them all
	# and we don't have to verify that every character is valid - commented out in encode()

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


# take a file name, open it, and return a list of the words in that file
def load_dictionary(filename):
	txtfile = open(filename, 'r')  # 'r' is the "read" mode, as opposed to "write" or something else
	# Exactly how this is handled depends on the formatting of the dictionary.
	# For the engmix_84k word list, python's read() function interprets it as
	# a single character string with spaces between each word (rather than linebreaks).
	# The split() function creates a new list item every time it hits a space.
	word_list = txtfile.read().split()
	txtfile.close()
	return word_list


# check if input is a valid character string
def is_string(s):
	try:
		str(s)
		return True
	except ValueError:
		return False


# main function, called at launch
def main():
	#check that there is only one item entered
	if len(sys.argv) == 2:
		input = sys.argv[1]
		# check that it's a valid character string
		if is_string(input):
			inputword = str(input)
			#find the steals
			final_list = findsteals(inputword)
			print str(len(final_list)) + ' possible steals found for ' + inputword + ': ' + str(final_list)
		else:
			print 'entry invalid'


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
