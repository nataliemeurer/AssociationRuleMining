# USED TO STORE GLOBAL / ENVIRONMENTAL VARIABLES

# GENERAL SETTINGS
PROGRESS_BAR = True 							# BOOLEAN: set whether a progress bar is used to show output.  Should be turned off when writing to files


# DATA SETTINGS
PRODUCT_NAMES_SRC = './data/products'				# STRING: The path to the data file
ITEM_QUANTITY_SRC = './data/small_basket.dat'


# ASSOCIATION CONSTRUCTION SETTINGS
MIN_SUPPORT = .35
MIN_CONFIDENCE = .6
A_PRIORI_METHOD = "generate_all"				# STRING: "generate_all" or "use_tree"

