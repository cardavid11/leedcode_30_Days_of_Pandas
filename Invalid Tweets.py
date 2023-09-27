import pandas as pd  # Importing the pandas library and aliasing it as pd for convenience.

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:  # Function definition with type hints for argument and return type.
    # Filtering invalid tweets:
    # - tweets["content"].str.len() computes the length of each string in the 'content' column.
    # - > 15 creates a boolean mask where True indicates the length of content is greater than 15.
    # - tweets[...][["tweet_id"]] filters the DataFrame and selects only the 'tweet_id' column.
    invalid_tweets = tweets[tweets["content"].str.len() > 15][["tweet_id"]]
    
    return invalid_tweets  # Returning the DataFrame containing IDs of invalid tweets.
