class codingProblem4:
	def __init__(self,list):
		self.list = list
	def firstMissingPositiveInteger(self):
		#Lowest positive integer possible
		number = 1;
		while number in self.list:
			 #Keep increasing counter until it doesn't exists in the list
			number = number + 1
		return number