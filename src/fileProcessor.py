import codecs
import re
import utils as util
import settings

# readArff( fileSrc ): takes a file path for an arff and returns a list of dictionaries as well as a d
def getProducts(fileSrc):
	# main variables to be returned
	products = []
	dataFile = codecs.open(fileSrc, 'rb', 'utf-8') 	# specify utf-8 encoding
	print "Retrieving products..."
	lines = dataFile.readlines() 					# read all lines
	if settings.PROGRESS_BAR == True:
		util.updateProgress(0)						# create a progress bar
	# test every line and extract its relevant information
	for idx, line in enumerate(lines):				# test each line
		if settings.PROGRESS_BAR == True:
			util.updateProgress(float(idx) / float(len(lines)))
		lineList = line.split(", ")
		lineList[1] = float(lineList[1])
		products.append(lineList);
	if settings.PROGRESS_BAR == True:
		util.updateProgress(1)
		print "\n"
	# return our list of products
	return products

def getTransactions(fileSrc, products):
	# main variables to be returned
	transactions = []
	reverseItemLookup = {}
	for key in products:
		reverseItemLookup[key[0]] = set()
	dataFile = codecs.open(fileSrc, 'rb', 'utf-8') 	# specify utf-8 encoding
	print "Loading Transactions..."
	lines = dataFile.readlines() 					# read all lines
	if settings.PROGRESS_BAR == True:
		util.updateProgress(0)						# create a progress bar

	# test every line and extract its relevant information
	for idx, line in enumerate(lines):				# test each line
		if settings.PROGRESS_BAR == True:
			util.updateProgress(float(idx) / float(len(lines)))
		lineList = line.split(", ")
		# Remove first item in the list
		lineList.pop(0)
		lineSet = set()
		for idx2, item in enumerate(lineList):
			if item != "0":
				# Add the index to our list to indicate that the product has been bought
				reverseItemLookup[products[idx2][0]].add(idx)
				lineSet.add(idx2)
		# append our array to our transactions
		transactions.append(lineSet);
	if settings.PROGRESS_BAR == True:
		util.updateProgress(1)
		print "\n"
	# return our list of products
	return [transactions, reverseItemLookup]