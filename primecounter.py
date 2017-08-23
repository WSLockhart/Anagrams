import sys
import math

#finds all the prime numbers less than n
def primecount(n):
	count = 0
	primelist = []
	k = 2 #variable counting which number we're checking for primality
	while k <= n: 
	
		i = 2 # variable counting through all potential divisors from 2 to sqrt(k)
		divisorfound = False
		while i <= k**(0.5) and divisorfound == False:
		
			if k%i == 0:
				divisorfound = True  # we found a divisor for k. K is not prime!
			i += 1
		# end inner while loop	
		if divisorfound == False: # if we never found one...
			count += 1            # we got a prime!
			primelist.append(k)   # add it to the list
			
		k +=1
	#end for loop
#	return count
	return primelist


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Define a main() function
def main():
	if len(sys.argv) == 2:	  #check that there is only one item entered
		input = sys.argv[1]
		if is_number(input):  # check that it's a valid integer
			n = int(input)
			output = primecount(n)
			print str(len(output)) + ' primes found: ' + str(output)
	else:
		print 'entry invalid: NaN'



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()


