from psaw import PushshiftAPI
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
##  Add if time field is important
# from datetime import datetime, timezone, timedelta 

def submissionParser(keyword): 
    
    api = PushshiftAPI()
    subs = api.search_submissions(
        subreddit="college",
        q=keyword,
        filter = [ 'author', 'selftext', 'url', 'permalink', 'subreddit', 'title'],
        # metadata = "false", 
        # max_results_per_request= 500
        )

    # Set display
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)

    df = pd.DataFrame([thing.d_ for thing in subs])
    
    from pathlib import Path 
    filepath = Path('Data Dumb/Reddit/'+keyword +'.csv')
    filepath.parent.mkdir(parents = True, exist_ok = True)
    df.to_csv(filepath)
