#this function takes in a file and returns
# all the birth year and death year in an array
# to excute , call the function bdYears() and 
# name your targeted file 
# attached is the data.txt file , feel free to 
# use and test the code
def bdYears(nameofthefile):
	import re
	fileobject=open(nameofthefile,'r')
	fileContent=fileobject.read()
	linesOfFile=fileContent.split('\n')
	result=[]
	for element in linesOfFile:
		years=re.findall(r"(\d{4})", element)
		if len(years)==2:
			result.append(years)
			result[-1][0]=int(result[-1][0])
			result[-1][1]=int(result[-1][1])
	if len(result)==0:
		print "we didn't find the birth and death year"
		return False
	return result
