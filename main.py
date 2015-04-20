# NOTE: This runs on Python 2.7.6

import sys
sys.path.insert(0, 'src')

import fileProcessor as fp
import settings as ENV
import associationRuleMiner as ARM
import datetime


print "Running mining algorithm for min support of " + str(ENV.MIN_SUPPORT) + " and min confidence of " + str(ENV.MIN_CONFIDENCE)
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
print "PROGRAM COMPLETED IN " + str(timeSpent.seconds) + " SECONDS\n\n\n--------------------------\n\n\n"