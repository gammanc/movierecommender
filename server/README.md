# Movie recommended server

**Requirements:**

- Python 3.6 or later

**_Start a terminal in this directory_**

## Project setup (first time)

### Create a Python virtualenv

We need a virtual environment in order to isolate our project dependencies. To create one, run the following command:

```
python -m venv env
```

**Note**: _env_ is the name of your virtual environment, you can change it if you want.

### Activate the virtualenv

Linux/MacOS:

```
source env/bin/activate
```

Windows:

```
.\env\bin\activate.bat
```

Make sure your terminal prompt starts with the name of your virtual environment in parentheses. Something like this:

`(env) [user@hostname]$`

**Note:** to exit the virtual environment just run the command `deactivate`, after that your terminal prompt should be back to normal.

## Running the server

Make sure you [activated the virtualenv](#activate-the-virtualenv).

### Restore project dependencies

`pip install -r requirements.txt`

### Start the server

```
python main.py
```

The server should be running successfully on: [localhost:5000](http://localhost:5000)

# Endpoints

- **`GET /api/movies/popular`** - List the most popular movies.
  - Returns array of full movie objects (all properties)
  - Query parameters:
    - **`max`** - int, optional, default value is 10.  
      Number of movie objects to return. Minimum accepted value is 5.
- **`GET /api/movies/names`** - List the movie titles.
  - Returns array of simple movie objects (properties: id, title, score).
  - Query parameters:
    - **`max`** - int, optional, default value is total available.  
      Number of movie objects to return. Minimum accepted value is 5.
- **`GET /api/movies/recommend`** - List of recommended movies given a movie title.
  - Returns array of full movie objects (all properties).
  - Query parameters:
    - **`title`** - string, **required**.  
      Movie title that will be used to get similar recommendations.
    - **`max`** - int, optional, default value is 5.  
      Number of movie objects to return. Minimum accepted value is 5.
