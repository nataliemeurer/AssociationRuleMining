# NOTE: This runs on Python 2.7.6

import sys
sys.path.insert(0, 'src')

import fileProcessor as fp
import settings as ENV

products = fp.getProducts(ENV.PRODUCT_NAMES_SRC)
transactions =  fp.getTransactions(ENV.ITEM_QUANTITY_SRC, products)
for idx, item in enumerate(products):
	print item[0] + ": " + str(transactions[5][idx])