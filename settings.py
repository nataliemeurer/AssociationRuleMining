# USED TO STORE GLOBAL / ENVIRONMENTAL VARIABLES

# GENERAL SETTINGS
PROGRESS_BAR = True 							# BOOLEAN: set whether a progress bar is used to show output.  Should be turned off when writing to files


# DATA SETTINGS
PRODUCT_NAMES_SRC = './data/products'			# STRING: The path to the data file
ITEM_QUANTITY_SRC = './data/small_basket.dat'	# STRING: The path to the data file


# ASSOCIATION CONSTRUCTION SETTINGS
MIN_SUPPORT = .3
MIN_CONFIDENCE = .5
APRIORI_METHOD = "partial"							# STRING: Either "full" or "partial".  Both yield the same results, although partial is considerably faster.  Full is a more set-based/iterable.combination implementation that does not conform perfectly to Apriori principles

