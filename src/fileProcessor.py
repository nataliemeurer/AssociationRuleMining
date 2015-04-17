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
	transactionsObj = {}
	dataFile = codecs.open(fileSrc, 'rb', 'utf-8') 	# specify utf-8 encoding
	print "Loading Transactions..."
	lines = dataFile.readlines() 					# read all lines
	if settings.PROGRESS_BAR == True:
		util.updateProgress(0)					# create a progress bar
	# test every line and extract its relevant information
	for idx, line in enumerate(lines):				# test each line
		if settings.PROGRESS_BAR == True:
			util.updateProgress(float(idx) / float(len(lines)))
		lineList = line.split(", ")
		# Remove first item in the list
		lineList.pop(0)
		for idx2, item in enumerate(lineList):
			if item == "0":
				lineList[idx2] = 0
			else:
				lineList[idx2] = 1
		# append our array to our transactions
		transactions.append(lineList);
	if settings.PROGRESS_BAR == True:
		util.updateProgress(1)
		print "\n"
	# return our list of products
	return transactions