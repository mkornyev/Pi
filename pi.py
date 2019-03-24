
import random
from matplotlib import pyplot
from statistics import variance

def ratio(n):
	inCount = 0

	for i in range(n): 
		#Get coordinates in range [0,1]
		xGuess = random.random()
		yGuess = random.random()
		
		#Count if inside the unit circle 
		if (((.5-xGuess)**2) + ((.5-yGuess)**2))**.5 <= .5:
			inCount+=1

	return inCount/n
	
def mean(L):
	s = 0
	for i in range(len(L)):
		s+=L[i]
	return s/len(L)

def work(n):
	print("----------------------------------------")
	print("Computed Sn w/n=" + str(n) + ": " + str(ratio(n)))

	#Compute Sn 1000 times 
	valList = []
	for i in range(1000): 
		valList.append(ratio(n))
	sMean = mean(valList)
	print("Mean Sn: " + str(sMean))	

	#Compute Variance
	sVar = variance(valList, sMean)
	print("Var Sn: " + str(sVar))	

	#Compute Sigma
	sSig = (sVar)**.5
	print("Sig Sn: " + str(sSig))	

	pyplot.hist(valList, histtype='bar', align='mid', orientation='vertical')
	pyplot.show()

	print("----------------------------------------")


work(100)
work(1000)
work(10000)
