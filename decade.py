#import pandas as pd


def decade(year):

	'''
	given a year return decade
	>>> decade(1986)
	1980
	'''
	return 10 * (year//10)

	pass



if __name__ == '__main__':
	import doctest
	doctest.testmod()

