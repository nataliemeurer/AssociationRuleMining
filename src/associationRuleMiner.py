import Queue as q


class AssociationRuleMiner:

	def __init__(self, products, transactions):
		self.products = products
		self.transactions = transactions
		self.rules = []

	def generateRules(self):
		itemSets = self.generateFrequentItemsets()
		self.buildRules()
		print "hola"

	def generateFrequentItemsets(self):
		# start with a value of k = 1 and add everything to our queue (because it is a breadth first approach)



def calculateSupport(supportCount, totalEntries):
	return float(supportCount) / float(totalEntries)

def calculateConfidence(supportCount, o)