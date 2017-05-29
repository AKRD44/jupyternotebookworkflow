from urllib.request import urlretrieve
import pandas as pd
import os


#If I want to just refer to it on my computer
my_file = "data.csv"
URL="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_data(filename=my_file,url=URL):
	"""if you type get_data? in the ipython notebook this text should pop up, so you define your stuff here
	"""
	if not os.path.exists(filename):
		print("downloading data")
		urlretrieve(url,filename)
	#data=pd.read_csv(my_file, index_col="Date", parse_dates=True) #for time series, make sure that the index is properly set
	data=pd.read_csv(my_file, index_col="Date") #for time series, make sure that the index is properly set
	try:
		data.index=pd.to_datetime(data.index,format="%m/%d/%Y %H:%M:%S %p")
	except TypeError:
		data.index=pd.to_datetime(data.index)
	data.columns=["West","East"] # so as to shorten the legend
	data["Total"]=data["West"]+data["East"]
	return data