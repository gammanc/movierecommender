import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

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
    json_string = pd.DataFrame.to_json(q_movies[['id', 'title', 'imdb_id', 'genres', 'overview', 'vote_count', 'vote_average', 'score']].head(how_many), orient='records')
    return json.loads(json_string)
    
def retrieve_names(how_many):
    if how_many is None:
        json_string = pd.DataFrame.to_json( q_movies[['id', 'title', 'score']], orient = 'records' )
    else:
        json_string = pd.DataFrame.to_json( q_movies[['id', 'title', 'score']].head(how_many), orient = 'records' )
    return json.loads(json_string)                    	
	

# ----- Segment 4: Word similarity calculations -----

tfidf = TfidfVectorizer(stop_words='english')
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

def get_recommendations(title, how_many, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the how_many most similar movies
    sim_scores = sim_scores[1:how_many+1]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    rdf = df2.copy().iloc[movie_indices]
    rdf['score'] = rdf.apply(weighted_rating, axis=1)
    rdf['genres'] = rdf['genres'].apply(json.loads)
    
    json_string = pd.DataFrame.to_json(rdf[['id', 'title', 'imdb_id', 'genres', 'overview', 'vote_count', 'vote_average', 'score']].head(how_many), orient='records')
    return json.loads(json_string)
    
