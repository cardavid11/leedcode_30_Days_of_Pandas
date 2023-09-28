import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # A regular expression pattern is crafted to match the criteria for a valid email.
    # ^[a-zA-Z] asserts position at start of the string and ensures the first character is a letter.
    # [\w.-]* allows for any word character (alphanumeric + underscore), period, or dash, 
    # appearing zero or more times. This forms the prefix name.
    # @leetcode.com$ asserts position at the end of the string and ensures the domain is '@leetcode.com'.
    pattern = r'^[a-zA-Z][\w.-]*@leetcode.com$'
    
    # The str.match() function is used to check whether the 'mail' column entries 
    # match the regular expression pattern.
    valid_email_mask = users['mail'].str.match(pattern)
    
    # Filtering the DataFrame using the boolean mask to retain only rows 
    # with valid email addresses.
    valid_email_users = users[valid_email_mask]
    
    return valid_email_users

# In this solution:
# A regular expression pattern is crafted to match the criteria for a valid email.
# str.match() is used to check whether the 'mail' column entries match the regular expression pattern.
# The DataFrame is filtered using the boolean mask generated by str.match() to retain only rows with valid email addresses.
# The function returns the filtered DataFrame containing users with valid emails.
# Regular expressions are a powerful tool for matching patterns in text, and the str.match() function in pandas provides a vectorized way to apply these patterns to each element of a series.

# breakdown of how learn to work with regular expressions:

# 1. Basic Characters:
# Literal Characters: The most basic regular expression consists of a single literal character, such as a. It will match the first occurrence of that character in the string.
# Example: a will match "apple" at the first character.
# 2. Meta Characters:
# . (Dot): Matches any character except a new line.
# Example: h.t will match "hat", "hit", "hot", etc.
# * (Star): Matches 0 or more repetitions of the preceding character or group.
# Example: ho* will match "h", "ho", "hoo", "hooo", etc.
# + (Plus): Matches 1 or more repetitions of the preceding character or group.
# Example: ho+ will match "ho", "hoo", "hooo", etc., but not "h".
# ? (Question Mark): Makes the preceding character optional. It matches 0 or 1 occurrence of the preceding character.
# Example: ho? will match "h" and "ho".
# 3. Character Classes:
# [] (Square Brackets): Matches any one of the enclosed characters.
# Example: h[aeiou]t will match "hat", "het", "hit", "hot", "hut".
# 4. Quantifiers:
# {n}: Matches exactly n occurrences of the preceding character.
# Example: ho{2} will match "hoo".
# 5. Positional Anchors:
# ^: Matches the start of a string.
# Example: ^h will match the 'h' in "hello".
# $: Matches the end of a string.
# Example: end$ will match the 'end' in "This is the end".
# 6. Groups and Alternation:
# () (Parentheses): Groups expressions together.
# | (Pipe): Acts as an OR operator.
# Example: h(a|i|o)t will match "hat", "hit", "hot".
# 7. Predefined Character Classes:
# \d: Matches any decimal digit, equivalent to [0-9].
# \w: Matches any word character, equivalent to [a-zA-Z0-9_].
# 8. Boundary Matchers:
# \b: Matches a word boundary.
# 9. Escape Special Characters:
# \ (Backslash): Used to escape any of the metacharacters.

# The re module in Python provides support for regular expressions.

# import re

# pattern = re.compile(r'\d{3}')  # matches 3 digits
# match = pattern.search("123")
# print(match.group())  # Output: '123'





    