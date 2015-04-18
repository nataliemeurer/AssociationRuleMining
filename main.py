# NOTE: This runs on Python 2.7.6

import sys
sys.path.insert(0, 'src')

import fileProcessor as fp
import settings as ENV
import associationRuleMiner as ARM
import datetime

testRunData = [ [.75, .5], [.9, .5], [.5, .5], [.4, .5], [.3, .5], [.2, .5], [.1, .5], [.05, .5], [.3, .6], [.3, .7], [.3, .8], [.3, .9], [.3, 1.0], [.3, .4] ]	# in the form of [min_Support, min_confidence]
for test in testRunData:
	ENV.MIN_SUPPORT = test[0]
	ENV.MIN_CONFIDENCE = test[1]
	print "Running test for min support of " + str(ENV.MIN_SUPPORT) + " and min confidence of " + str(ENV.MIN_CONFIDENCE)
	startTime = datetime.datetime.now()

	products = fp.getProducts(ENV.PRODUCT_NAMES_SRC)
	transactions =  fp.getTransactions(ENV.ITEM_QUANTITY_SRC, products)
	transEntries = transactions[0]
	reverseItemLookup = transactions[1]

	# print transactions
	miner = ARM.AssociationRuleMiner(products, transEntries, reverseItemLookup)
	miner.generateRules()

	endTime = datetime.datetime.now()
	timeSpent = endTime - startTime
	print "PROGRAM COMPLETED IN " + str(timeSpent.seconds) + " SECONDS"