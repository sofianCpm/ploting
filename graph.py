
# getting the data ready to plot

from generalextract import bdYears
import collections

# calculating the age from the years we have.
def ageGenerator(data):
	result=[]
	for element in data:
		if element[1]>element[0]:
			result.append({'birth':element[0],'death':element[1],'age':element[1]-element[0]})
	return result

# ordering the array by year	
def orderByYear(data):
	result= collections.OrderedDict()
	for element in data:
		if element['birth'] not in result:
			result[element['birth']]=[]
		result[element['birth']].append(element)
	data_ordered=collections.OrderedDict()
	for element in sorted(result):
		data_ordered[element]=result[element]
	result=data_ordered
	return result
# calling the functions and creating the two axes 


raw_data=bdYears('data.txt')
parsed_data=ageGenerator(raw_data)
ordered_data= orderByYear(parsed_data)
result=ordered_data
data_final_x=result.keys()
data_final_y=[sum([element['age'] for element in result[year]])/len (result[year])   for year in data_final_x]
