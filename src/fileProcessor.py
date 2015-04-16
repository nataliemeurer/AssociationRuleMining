import codecs
import re
import utils as util
import settings

# readArff( fileSrc ): takes a file path for an arff and returns a list of dictionaries as well as a d
def getProducts(fileSrc):
	# main variables to be returned
	relation = ""									# relation		
	attributes = []									# attribute list
	rawData = []									# main data storage
	reverseLookup = {}								# store by value for reverse lookup
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
		products.append(lineList);
	return products

def getTransactions(fileSrc, products):
	# main variables to be returned
	relation = ""									# relation		
	attributes = []									# attribute list
	rawData = []									# main data storage
	reverseLookup = {}								# store by value for reverse lookup
	continuousVariables = {}
	categoricalVariables = {}
	classIdx = None
	dataFile = codecs.open(fileSrc, 'rb', 'utf-8') 	# specify utf-8 encoding
	print "Reading file..."
	lines = dataFile.readlines() 					# read all lines
	if settings.PROGRESS_BAR == True:
		util.updateProgress(0)					# create a progress bar