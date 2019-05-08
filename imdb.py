import numpy as np
import modin.pandas as pd

# Read the delimited file
imdb_basic_data = pd.read_csv('data/imdb-basics.tsv', delimiter = '\t', encoding = 'utf-8')

# Reading a dataframe in a temporary object so we can fix the data
 # before we put it into the 'df' object.
fix_df = pd.DataFrame(imdb_basic_data)

# In the dataset given, NULL or N/A is denoted as \N in the file.
# Replacing it with string '0' for now. Will look for something better.
df = fix_df.replace('\\N', '0')

# Change the datatype of the startyear Column
# This is needed as we want to compare the data between the dates
df.startYear = df.startYear.astype(int)

################################################################################################

# Unique Title Types

print('-'*200)
print(' '*80 + 'Unique Title Types\n')
unique_title_types = df['titleType'].unique()
print(unique_title_types)
print('-'*200)

################################################################################################

# Display total number of titles

print('-'*200)
print(' '*80 + 'Total Number of Title Types\n')
total_titles = df['titleType'].value_counts()
print(total_titles)
print('-'*200)

################################################################################################

# Getting the list of total number of adult movies using DF

print('-'*200)
print(' '*60 + 'Total Number of Adult Movies irrespective of the Genre\n')

# Below is a way to set conditions in 'df'.
# You can have as many conditions as you want to filter the data.
# In the below conditions, I am trying to filter out only 'movie' and 
# where the 'isAdult' flag is set to true. 
# With the below condition, the data returns all the movies irrespective of their genre.
# We will filter out more thing on this data at later stage.
only_movies = df['titleType'] == 'movie'
is_adult = df['isAdult'] == True

adult_movies = df[only_movies & is_adult]

# Here is another way of writing the above condition.

# adult_movies = df[(df['titleType'] == 'movie') & (df['isAdult'] == True)]

# The below print statement will return only the count.
# The output of the below command will look something like this
# isAdult    8594

print(adult_movies[['isAdult']].count())

# Use the below statement if you want to see the entire dataframe
# print(adult_movies.count())

################################################################################################


