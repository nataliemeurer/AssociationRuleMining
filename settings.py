# USED TO STORE GLOBAL / ENVIRONMENTAL VARIABLES

# GENERAL SETTINGS
PROGRESS_BAR = True 							# BOOLEAN: set whether a progress bar is used to show output.  Should be turned off when writing to files


# DATA SETTINGS
PRODUCT_NAMES_SRC = './data/products'				# STRING: The path to the data file
ITEM_QUANTITY_SRC = './data/small_basket.dat'


# ASSOCIATION CONSTRUCTION SETTINGS
MIN_SUPPORT = .3
MIN_CONFIDENCE = .5


# CLUSTERING SETTINGS
USE_RANDOM_SAMPLE = False 						# BOOLEAN: Determines whether the algorithm will sample the whole data set or a fixed size
SAMPLE_SIZE = 1000 								# INT: Sets the sample size that the algorithm will cluster, which is randomly sampled without replacement
SAMPLE_WITH_REPLACEMENT = False 				# BOOLEAN: If true, samples data with replacement.  Otherwise, does not replace
K = 10											# INT: number of clusters desired
DISTANCE_MEASURE = "euclidian"					# STRING: formula used to measure distance, currently only supports euclidian
MERGING_CRITERIA = "single-link"				# STRING: single-link, complete-link, centroid, wards
USE_INTRA_CLUSTER_SHORTCUT = True 				# BOOLEAN: sets whether shortcut used in intra-cluster distance calculations.  The shortcut calculates distance from centroid instead of from all other points, making it O(n)
MAX_SIMILARITY_THRESHOLD = 5.0					# FLOAT: sets the maximum distance threshold to merge two clusters

# VALIDATOR SETTINGS
NUM_OF_FOLDS = 10