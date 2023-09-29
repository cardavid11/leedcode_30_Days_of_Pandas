import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    # Create regular expressions for 'bull' and 'bear' as standalone words.
    # \b is a word boundary, which matches the position between a word character and a non-word character.
    # \s is a whitespace character, which matches any whitespace character such as spaces, tabs, and line breaks.
    bull_regex = r'\sbull\s'
    bear_regex = r'\sbear\s'
    
    # Use str.contains() with the regular expressions to get a boolean mask indicating
    # which rows in the DataFrame contain the words 'bull' and 'bear'.
    # case=False makes the search case-insensitive.
    bull_mask = files['content'].str.contains(bull_regex, case=False)
    bear_mask = files['content'].str.contains(bear_regex, case=False)
    
    # Sum up the boolean values to get the count of occurrences for each word.
    bull_count = bull_mask.sum()
    bear_count = bear_mask.sum()
    
    # Create a new DataFrame to store the words 'bull' and 'bear' along with their respective counts.
    result_df = pd.DataFrame({
        'word': ['bull', 'bear'],
        'count': [bull_count, bear_count]
    })
    
    return result_df
    