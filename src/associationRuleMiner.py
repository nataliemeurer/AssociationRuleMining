import Queue as qu
import settings as ENV


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
		# start with a value of k = 1 and add everything to our item sets and prune (because it is a breadth first approach)
		currentItemSets = []
		freqItemSets = []
		supports = {}
		# Create a set with each item
		for idx, item in enumerate(self.products):
			itemSets.append(set([idx]))

		kVal = 1
		while len(itemSets) != 0
			# Determine which item sets are frequent within itemSets
			# for every item in our itemsets, C_k
			for idx, set in enumerate(currentItemSets):
				# set count to zero
				count = 0
				for trans in self.transactions:
					# If our set is in the transaction
					if set.issubset(trans)
						count += 1
				support = calculateSupport(count, len(self.transactions))
				if support > ENV.MIN_SUPPORT:
					freqItemSets.append(set)
			# Recalculate our currentItemSets
			currentItemSets = []
			

			kVal += 1
			
			# for idx, item in self.products:


	def buildRules(self):
		print "rules"


def calculateSupport(supportCount, totalEntries):
	return float(supportCount) / float(totalEntries)

def calculateConfidence(totalCount, ruleSetCount):
	return float(toatlCount) / float(ruleSetCount)