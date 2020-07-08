import pandas as pd
import numpy as np
import json

# --- Segment 1: Data Initialization -----

df1 = pd.read_csv('../datasets/tmdb_5000_credits.csv')
df2 = pd.read_csv('../datasets/tmdb_5000_movies.csv')
df3 = pd.read_csv('../datasets/movies_metadata_edited.csv')

df1 = df1.drop_duplicates()
df2 = df2.drop_duplicates()
df3 = df3.drop_duplicates()

df1.columns = ['id','tittle','cast','crew']
df3 = df3[['id', 'imdb_id']]
df1 = df1.merge(df3, on='id')
df2= df2.merge(df1,on='id')	

# ----- Segment 2: Calculating the score for each movie -----

C = df2['vote_average'].mean()
m = df2['vote_count'].quantile(0.9)

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies = df2.copy().loc[df2['vote_count'] >= m]
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

# ----- Segment 3: Functions for data retrieval -----

#The column genres is itself a JSON object, so we do this first
q_movies['genres'] = q_movies['genres'].apply(json.loads)

def retrieve_popular_movies(how_many):
	json_string = pd.DataFrame.to_json(q_movies[['title', 'imdb_id', 'genres', 'overview', 'vote_count', 'vote_average', 'score']].head(how_many), orient='table')
	parsed = json.loads(json_string)
	return json.dumps(parsed, indent=4, sort_keys=True)

#Example:	
print(retrieve_popular_movies(10))	
