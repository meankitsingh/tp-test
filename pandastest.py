import pandas as pd
import requests
import pprint 



# setting dataframe display options
pd.set_option('max_colwidth',10)
pd.set_option('chop_threshold',10)
pd.set_option('show_dimensions','truncate')
pd.set_option('column_space',10)



# Fetching Response From News Api 
def fetch_data():
    _apikey = '8fdcebe8ebef4f2c839b1ff941518ff0'
    _baseurl = "http://newsapi.org/v2/top-headlines"
    _payload = {'apiKey':_apikey,'country':'us'}
    _response = requests.get(url=_baseurl,params=_payload).json()
    print("Fetching data from the api..........")

    return {
        "response":_response['articles']
    }


# Making Pandas DataFrame From Fetched Response
def data_manipulator(data_source):
    news_df = None
    try:
        news_df = pd.DataFrame.from_dict(data=data_source, orient="columns", dtype=None, columns=None)
    except BaseException as execption:
        print(execption) 
    print("Filling pandas dataframe with data............")
    return news_df

# Obtaining The First And Last Five Rows
def data_visualizer(frames):
    first_five = frames.head(5)
    last_five  = frames.tail(5)
    print("The First Five Rows Are",end="\n")
    pprint.pprint(first_five, indent=1, width=200,compact=False)
    print("The Last Five Rows Are",end="\n")
    pprint.pprint(last_five, indent=1, width=200,compact=False)


def executor():
    print("initiating program.........")
    data_source = fetch_data()["response"]
    news_frames = data_manipulator(data_source)
    data_visualizer(news_frames)
    

if __name__ == "__main__":
    executor()


