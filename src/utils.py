#  STORES ACCESSORY CLASSES AND FUNCTIONS
import bisect
import time, sys
import numpy as np
import math
import random
import settings as ENV

# NORMALIZATION FUNCTIONS
# scale using min-max
def scaleMinMax(value, oldMin, oldMax, minimum=0, maximum=1):
	return ((value - oldMin)/(oldMax - oldMin))*(maximum - minimum) + minimum

# scale using z-score
def scaleZScore(value, mean, stdev):
	return (value - mean) / stdev

# SAMPLING FUNCTIONS
# choose w/out replacement and return it
def chooseOneWithoutReplacement(list):
	randIdx = math.floor(len(list) * random.random())
	removedVal = list.pop(int(randIdx))
	return removedVal

# choose one w/ replacement and return it
def chooseOneWithReplacement(list):
	randIdx = math.floor(len(list) * random.random())
	val = list[int(randIdx):int(randIdx) + 1]
	return val

# DICTIONARY FUNCTIONS
# returns true if dictionary is empty, else returns false
def dictIsEmpty(dict):
	for key in dict:
		return False
	return True

# Merges Two dictionaries that use integers as values
def mergeDicts(dict1, dict2):
	newDict = {}
	for key in dict1:
		if key in dict2:
			newDict[key] = dict1[key] + dict2[key]
		else:
			newDict[key] = dict1[key]
	for key in dict2:
		if key in newDict:
			continue
		else:
			newDict[key] = dict2[key]
	return newDict


# MISCELLANEOUS
# Returns whether the string can be converted to a number
def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# Progress bar function -- Some functions inspired by this: http://stackoverflow.com/questions/3160699/python-progress-bar
def updateProgress(progress):
    barLength = 20 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Pausing...\r\n"
    if progress >= 1:
        progress = 1
        status = "Processing complete..."
    block = int(round(barLength*progress))
    text = "\rProgress: [{0}] {1}% {2}".format( "#" * block + "-" * (barLength - block), progress * 100, status)
    sys.stdout.write(text)
    sys.stdout.flush()
