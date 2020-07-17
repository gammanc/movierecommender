# Movie recommender server

If you need more detail, you can visit our [wiki](https://github.com/gammanc/movierecommender/wiki/Quick-start#server-rest-api)

**Requirements:**

- Python 3.6 or later

**_Start a terminal in this directory_**

### Create a python virtual environment (first time)

```
python -m venv env
```

### Activate the virtualenv

```
#Linux and Mac OS
source env/bin/activate

# Windows
env\scripts\activate
```

**Note:** to exit the virtual environment just run the command `deactivate`.

### Restore project dependencies

`python -m pip install -r requirements.txt`

### Start the server

```
python main.py
```

The server should be running successfully on: [localhost:5000](http://localhost:5000). Here is a list of [available endpoints](https://github.com/gammanc/movierecommender/wiki/Endpoints#available-endpoints)
