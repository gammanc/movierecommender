from flask import Flask, jsonify, request
from flask_cors import CORS
from data_utils import retrieve_popular_movies, retrieve_names, get_recommendations

app = Flask(__name__)
app.config['ENV'] = "development"
CORS(app)

@app.route("/api/movies/popular")
def get_popular_movies():
    '''
    GET endpoint that list the most popular movies.

    Arguments
    ---------
    max : int, optional (query string) 
        Number of movie records to return (default: 10). If a number lower 
        than 5 is provided then the value will be set to 5.

    Raises
    ------
    ValueError
        If `max` is provided and its value cannot be converted to integer.

    Returns
    -------
    List of full movie objects serialized as JSON.
        example:
        [
            {
                id: int,
                title: string,
                imdb_id: string,
                genres: array,
                overview: string,
                vote_count: int,
                vote_average: float,
                score: float
            },
            ...,
            {...}
        ]
    '''

    list_size = int(request.args.get("max", "10"))
    list_size = 5 if list_size < 5 else list_size
    return jsonify(retrieve_popular_movies(list_size))

@app.route("/api/movies/names")
def get_movies_titles():
    '''
    GET endpoint that list the movie titles.

    Arguments
    ---------
    max : int, optional (query string) 
        Number of movie titles to return (default: total available). If a number lower
        than 5 is provided then the default value will be used.

    Raises
    ------
    ValueError
        If `max` is provided and its value cannot be converted to integer.
    
    Returns
    -------
    List of simple movie objects serialized as JSON.
        example:
        [
            {
                id: int,
                title: string,
                score: float
            },
            ...,
            {...}
        ]
    '''

    list_size = int(request.args.get("max", "1"))
    list_size = None if list_size < 5 else list_size
    return jsonify(retrieve_names(list_size))

@app.route("/api/movies/recommend")
def get_movie_recommendations():
    '''
    GET endpoint that list recommended movies given a movie title. 

    Arguments
    ---------
    title : str, required (query string)
        Movie title we will use to get similar recommendations.
    max : int, optional (query string)
        Number of movie objects to return (default: 5). If a number lower than 5 is
        provided then the default value will be used.

    Raises
    ------
    ValueError
        If `max` is provided and its value cannot be converted to integer.
    
    Returns
    -------
    Status code 200: 
        List of full movie objects serialized as JSON.
            example:
            [
                {
                    id: int,
                    title: string,
                    imdb_id: string,
                    genres: array,
                    overview: string,
                    vote_count: int,
                    vote_average: float,
                    score: float
                },
                ...,
                {...}
            ]
    
    Status code 400:
        Error message explaining why the request failed.
    '''

    title = request.args.get("title", None)
    if title is None:
        return jsonify({ "error": "Query param 'title' is required"}), 400
    list_size = int(request.args.get("max", "5"))
    list_size = 5 if list_size < 5 else list_size
    return jsonify(get_recommendations(title, list_size))

if __name__ == "__main__":
    app.run(debug=True)
