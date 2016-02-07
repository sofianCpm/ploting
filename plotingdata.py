
#Creating the graph

from graph import *
import plotly 
from plotly.graph_objs import Scatter, Layout

print 'enter the name of the targeted file'
nameofthefile = raw_input("")
raw_data=bdYears(nameofthefile)
parsed_data=ageGenerator(raw_data)
ordered_data= orderByYear(parsed_data)
result=ordered_data
data_final_x=result.keys()
data_final_y=[sum([element['age'] for element in result[year]])/len (result[year])   for year in data_final_x]

plotly.offline.plot({
	'data':[Scatter(x=data_final_x, y=data_final_y)],
	'layout': Layout(title='demographics')
	})
