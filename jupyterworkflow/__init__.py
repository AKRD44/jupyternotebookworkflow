from urllib.request import urlretrieve
import pandas as pd
import os

#If I want to just refer to it on my computer
my_file = "data.csv"
URL="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_data(filename,url):
    if not os.path.exists(filename):
        print("downloading data")
        urlretrieve(url,filename)
    data=pd.read_csv(my_file, index_col="Date", parse_dates=True) #for time series, make sure that the index is properly set
    data.columns=["West","East"] # so as to shorten the legend
    data["Total"]=data["West"]+data["East"]
    return data