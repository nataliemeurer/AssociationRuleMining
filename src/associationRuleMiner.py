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

	# main ARM function.  Calls functions to calculate frequent item sets and build rules
	def generateRules(self):
		print "Calculating Frequent Item Sets:"
		# calculate item sets
		itemSets = self.generateFrequentItemsets()
		# display our item sets
		print "\nFrequent item sets:"
		for idx, mySet in enumerate(itemSets):
			print "Set " + str(idx + 1) + ":"
			listSet = list(mySet)
			listSet.sort()
			for item in listSet:
				print self.products[item][0] + " "
			print ""

		print "Building Rules:\n"
		# build rules based on our item sets
		rules = self.buildRules(itemSets)
		# display and return our generated rules
		self.displayRules(rules)
		return rules


	def generateFrequentItemsets(self):
		# start with a value of k = 1 and add everything to our item sets and prune (because it is a breadth first approach)
		finalItemSets = []
		freqItemSets = []
		badEntries = []
		goodBases = []

		# Create a set with each item
		for idx, item in enumerate(self.products):
			support = calculateSupport(len(self.reverseLookup[item[0]]), len(self.transactions))
			if support >= ENV.MIN_SUPPORT:
				freqItemSets.append(set([idx]))
				goodBases.append(idx)
			else:
				badEntries.append(set([idx]))

		kVal = 2
		while len(freqItemSets) != 0:
			print "\n\nProcessing item sets of length " + str(kVal) + "\n"
			util.updateProgress(0)
			# set our finalItemSets in case we cannot calculate them all
			finalItemSets = freqItemSets[:]
			freqItemSets = []
			# find all combinations possible
			combinations = it.combinations(goodBases, kVal)
			combinations = list(combinations)
			# for every combination...
			for idx, combination in enumerate(combinations):
				util.updateProgress(float(idx) / float(len(combinations)))
				# turn the combination(tuple) into a set
				comboSet = set(combination)
				# set a bool to determine if it's bad
				isBad = False
				# for each potential set of the given k value, test if it contains any eliminated entries
				for badSet in badEntries:
					# if the badSet is a part of the comboSet...
					if badSet.issubset(comboSet):
						# Add our comboSet to the list of bad entries
						# badEntries.append(comboSet)
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
					# Calculate support for our combinations
					support = calculateSupport(len(superSet), len(self.transactions))
					if support < ENV.MIN_SUPPORT:
						# add it to our bad entries
						badEntries.append(comboSet)
					else:
						# Count it as a frequent item set
						freqItemSets.append(comboSet)
			util.updateProgress(1)
			kVal += 1
		return finalItemSets

	# Main Function to create rules from a list of frequent item sets
	def buildRules(self, sets):
		# For each set...
		rules = []
		print "Extracting Rules from Frequent Sets:\n"
		for ruleSet in sets:
			potentialRules = []			# store all potential rules in the form [set(conditions), set(result)]
			badRules = []
			# Generate potential rules
			iter = len(ruleSet) - 1
			while iter >= 1:
				# generate every combination
				combos = it.combinations(list(ruleSet), iter)
				for combo in combos:
					comboSet = set(combo)
					# add the rule and its result to our potential rules
					potentialRules.append([comboSet, ruleSet.difference(comboSet)])
				# decrement our iterator
				iter -= 1

			
			util.updateProgress(0)
			# for every potential rule
			for idx, rule in enumerate(potentialRules):
				util.updateProgress( float(idx) / float(len(potentialRules)))
				# eliminate rules via apriori principle
				low_confidence_via_apriori = False
				for badRule in badRules:
					if badRule[1].issubset(rule[1]):
						low_confidence_via_apriori = True
				if low_confidence_via_apriori == False:
					# test confidence level
					superSet = None
					totalCount = None
					for productId in rule[0]:
						# if we haven't defined our superset yet, we set it to the entire space of reverse lookup
						if superSet == None:
							superSet = self.reverseLookup[self.products[productId][0]]
						# Otherwise, we find the intersection between the two sets
						else:
							superSet = self.reverseLookup[self.products[productId][0]].intersection(superSet)
					ruleSetCount = len(superSet)
					for productId in rule[1]:
						superSet = self.reverseLookup[self.products[productId][0]].intersection(superSet)
					totalCount = len(superSet)
					# get our confidence
					confidence = calculateConfidence(totalCount, ruleSetCount)
					# if it meets our threshold, add it to our list of rules
					if confidence >= ENV.MIN_CONFIDENCE:
						rule.append(confidence)
						rules.append(rule)
					else:
						badRules.append(rule)
			util.updateProgress(1)
			print "\n"
		return rules

	# displays the rules
	def displayRules(self, rules):
		print str(len(rules)) + " rules were generated:\n"
		for rule in rules:
			ruleStr = ""
			ruleList = [list(rule[0]), list(rule[1])]
			ruleList[0].sort()
			ruleList[1].sort()
			for idx, item in enumerate(ruleList[0]):
				ruleStr += self.products[item][0]
				if idx != (len(ruleList[0]) - 1):
					ruleStr += ", "
			ruleStr += " ---> "
			for idx, item in enumerate(ruleList[1]):
				ruleStr += self.products[item][0]
				if idx != (len(ruleList[1]) - 1):
					ruleStr += ", "
			ruleStr += "\nConfidence: " + str(rule[2]) + "\n"
			print ruleStr
				
def calculateSupport(supportCount, totalEntries):
	return float(supportCount) / float(totalEntries)

def calculateConfidence(totalCount, ruleSetCount):
	return float(totalCount) / float(ruleSetCount)