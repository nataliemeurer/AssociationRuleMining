import Queue as qu
import settings as ENV
import itertools as it
import utils as util


class AssociationRuleMiner:

	def __init__(self, products, transactions, reverseLookup):
		self.products = products
		self.transactions = transactions
		self.reverseLookup = reverseLookup
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
		badEntries = []
		supports = {}
		# Create a set with each item
		for idx, item in enumerate(self.products):
			support = calculateSupport(len(self.reverseLookup[item[0]]), len(self.transactions))
			supports[str(idx)] = support
			if support >= ENV.MIN_SUPPORT:
				currentItemSets.append(set([idx]))
			else:
				badEntries.append(set([idx]))

		kVal = 2
		while len(currentItemSets) != 0:
			# find all combinations possible
			combinations = itertools.combinations(range(len(products)), kVal)
			# for every combination...
			for combination in combinations:
				print combination
				# turn the combination into
				comboSet = set(combination)
				# set a bool to determine if it's bad
				isBad = False
				# for each potential set of the given k value, test if it contains any eliminated entries
				for badSet in badEntries:
					# if the badSet is a part of the comboSet...
					if badSet.issubset(comboSet):
						# Add our comboSet to the list of bad entries
						badEntries.append(comboSet)
						isBad = True
						break
				# if it should be included
				if isBad == False:
					# test support
					superSet = None
					for productId in combination:
						# if we haven't defined our superset yet, we set it to the entire space of reverse lookup
						if superSet == None:
							superSet = self.reverseLookup[self.products[productId][0]]
						# Otherwise, we find the intersection between the two sets
						else:
							superSet = self.reverseLookup[self.products[productId][0]].intersection(superSet)
					support = calculateSupport(len(superSet), len(self.transactions))
					print "SUPPORT IS" + str(support)
					if support < ENV.MIN_SUPPORT:
						# add it to our bad entries
						badEntries.append(comboSet)
						





		# kVal = 1
		# while len(currentItemSets) != 0:
		# 	# Determine which item sets are frequent within itemSets
		# 	print "\nDetermining support for itemsets of length " + str(kVal)
		# 	util.updateProgress(0)
		# 	freqItemSets = []
		# 	# for every item in our itemsets, C_k
		# 	for idx, currentSet in enumerate(currentItemSets):
		# 		util.updateProgress(float(idx) /float(len(currentItemSets)))
		# 		# set count to zero
		# 		count = 0
		# 		for trans in self.transactions:
		# 			# If our set is in the transaction
		# 			if currentSet.issubset(trans):
		# 				count += 1
		# 		support = calculateSupport(count, len(self.transactions))
		# 		listSet = list(item)
		# 		listSet.sort()
		# 		key = ""
		# 		for num in listSet:
		# 			key += str(num)
		# 		supports[key] = support
		# 		# check if it is within the range we're looking for
		# 		if support > ENV.MIN_SUPPORT:
		# 			freqItemSets.append(currentSet)

		# 	util.updateProgress(1)
		# 	# Recalculate our currentItemSets
		# 	currentItemSets = []
		# 	i = 0

		# 	print "\nCombining frequent item sets for next stage"
		# 	util.updateProgress(0)
			
		# 	while i < len(freqItemSets):
		# 		util.updateProgress(float(i) / float(len(freqItemSets)))
		# 		j = i + 1
		# 		while j < len(freqItemSets):
		# 			# self-join our two sets
		# 			unionSet = freqItemSets[i].union(freqItemSets[j])
		# 			if unionSet not in currentItemSets and len(unionSet) == kVal + 1:
		# 				currentItemSets.append(unionSet)
		# 			# increment j
		# 			j += 1
		# 		# increment i
		# 		i += 1
		# 	# prune our tree
		# 	indicesToRemove = []
		# 	for idx, currentSet in enumerate(currentItemSets):
		# 		for iterObj in it.combinations(list(currentSet), kVal):
		# 			if set(iterObj) not in freqItemSets:
		# 				# Add the index to our list of indices to be removed
		# 				indicesToRemove.insert(0, idx)
		# 				# break and exit
		# 				break
		# 	for index in indicesToRemove:
		# 		if len(currentItemSets) > 0:
		# 			currentItemSets.pop(index)
		# 	kVal += 1
		# return freqItemSets


	def buildRules(self):
		print "rules"


def calculateSupport(supportCount, totalEntries):
	return float(supportCount) / float(totalEntries)

def calculateConfidence(totalCount, ruleSetCount):
	return float(toatlCount) / float(ruleSetCount)