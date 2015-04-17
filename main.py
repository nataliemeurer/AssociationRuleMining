# NOTE: This runs on Python 2.7.6

import sys
sys.path.insert(0, 'src')

import fileProcessor as fp
import settings as ENV
import associationRuleMiner as ARM

products = fp.getProducts(ENV.PRODUCT_NAMES_SRC)
transactions =  fp.getTransactions(ENV.ITEM_QUANTITY_SRC, products)
transEntries = transactions[0]
reverseItemLookup = transactions[1]

# print transactions
miner = ARM.AssociationRuleMiner(products, transEntries)
miner.generateRules()