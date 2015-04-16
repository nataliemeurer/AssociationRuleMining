# NOTE: This runs on Python 2.7.6

import sys
sys.path.insert(0, 'src')

import fileProcessor as fp
import settings as ENV

products = fp.getProducts(ENV.PRODUCT_NAMES_SRC)
print products