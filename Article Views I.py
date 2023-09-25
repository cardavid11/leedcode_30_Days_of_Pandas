import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    viewers_id = views[["viewer_id"]]
    unique_viewers = viewers_id.drop_duplicates().sort_values(by=['viewer_id'])
    authors_ids = views
    print(unique_viewers)

    # Filter the rows where author_id is equal to viewer_id
    self_views = views[views['author_id'] == views['viewer_id']]
    
    # Get unique author_ids who viewed their own articles
    # The method .reset_index(drop=True) is used to reset the index of a DataFrame or Series, and start the index again from 0. When you reset the index, the old index is added as a column, unless you specify drop=True, which discards the old index.
    unique_authors = self_views['author_id'].drop_duplicates().sort_values().reset_index(drop=True)
    # Convert to DataFrame to match expected output format
    unique_authors_df = unique_authors.to_frame(name='id')
    return unique_authors_df

#The expression unique_authors[['author_id']] assumes that unique_authors is a DataFrame with a column named 'author_id'. However, in the provided code, unique_authors is a Series, not a DataFrame. The [['column_name']] syntax is used to select columns from a DataFrame, but it's not applicable when dealing with a Series.

# On the other hand, unique_authors.to_frame(name='author_id') is converting the Series unique_authors to a DataFrame with a single column named 'author_id'. The to_frame() method is a way to convert a Series to a DataFrame, and the name argument allows you to specify the name of the column in the resulting DataFrame.

# import pandas as pd

# Assume unique_authors is a Series
# unique_authors = pd.Series([1, 2, 3], name='author_id')

# Converting the Series to a DataFrame using to_frame()
# unique_authors_df = unique_authors.to_frame(name='author_id')
# print(unique_authors_df)

# Output:
#    author_id
# 0          1
# 1          2
# 2          3