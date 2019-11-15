# Link for YouTube: https://www.youtube.com/watch?v=skGwKh1dAdk
# from io import StringIO

import pandas as pd
from sentiment import analyse_comments

# making data frame from csv file
data = pd.read_excel("./bunsen_reviews.xlsx")

# retrieving just the comments.
rows = data.iloc[0:170, 1]

analyse_comments(rows)
# print("reviews.py")













