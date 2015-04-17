import Queue as qu
import settings as ENV
import itertools as it
import utils as util


class AssociationRuleMiner:

	def __init__(self, products, transactions):
		self.products = products
		self.transactions = transactions
		self.rules = []

	def generateRules(self):
		itemSets = self.generateFrequentItemsets()
		print "\n"
		print itemSets
		self.buildRules()
		print "hola"

	def generateFrequentItemsets(self):
		# start with a value of k = 1 and add everything to our item sets and prune (because it is a breadth first approach)
		currentItemSets = []
		freqItemSets = []
		supports = {}
		# Create a set with each item
		for idx, item in enumerate(self.products):
			currentItemSets.append(set([idx]))

		kVal = 1
		while len(currentItemSets) != 0:
			# Determine which item sets are frequent within itemSets
			print "\nDetermining support for itemsets of length " + str(kVal)
			util.updateProgress(0)
			freqItemSets = []
			# for every item in our itemsets, C_k
			for idx, currentSet in enumerate(currentItemSets):
				util.updateProgress(float(idx) /float(len(currentItemSets)))
				# set count to zero
				count = 0
				for trans in self.transactions:
					# If our set is in the transaction
					if currentSet.issubset(trans):
						count += 1
				support = calculateSupport(count, len(self.transactions))
				listSet = list(item)
				listSet.sort()
				key = ""
				for num in listSet:
					key += str(num)
				supports[key] = support
				# check if it is within the range we're looking for
				if support > ENV.MIN_SUPPORT:
					freqItemSets.append(currentSet)

			util.updateProgress(1)
			# Recalculate our currentItemSets
			currentItemSets = []
			i = 0

			print "\nCombining frequent item sets for next stage"
			util.updateProgress(0)
			
			while i < len(freqItemSets):
				util.updateProgress(float(i) / float(len(freqItemSets)))
				j = i + 1
				while j < len(freqItemSets):
					# self-join our two sets
					unionSet = freqItemSets[i].union(freqItemSets[j])
					if unionSet not in currentItemSets and len(unionSet) == kVal + 1:
						currentItemSets.append(unionSet)
					# increment j
					j += 1
				# increment i
				i += 1
			# prune our tree
			indicesToRemove = []
			for idx, currentSet in enumerate(currentItemSets):
				for iterObj in it.combinations(list(currentSet), kVal):
					if set(iterObj) not in freqItemSets:
						# Add the index to our list of indices to be removed
						indicesToRemove.insert(0, idx)
						# break and exit
						break
			for index in indicesToRemove:
				if len(currentItemSets) > 0:
					currentItemSets.pop(index)
			kVal += 1
		return freqItemSets


	def buildRules(self):
		print "rules"


def calculateSupport(supportCount, totalEntries):
	return float(supportCount) / float(totalEntries)

def calculateConfidence(totalCount, ruleSetCount):
	return float(toatlCount) / float(ruleSetCount)