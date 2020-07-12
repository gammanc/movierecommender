# Movie 

**Requirements:**
* Python 3.6 or later


## How to run

Go to this path in your terminal before continuing.

### Create Python virtualenv (just the first time)
We need a virtual environment in order to isolate our project dependencies. To create one, run the following command:
```
python -m venv env
```
Windows
```
py -3 -m venv .env
```

**Note**: *env* is the name of your virtual environment, you can change it if you want.

### Activate the virtualenv
```
source env/bin/activate
```
Windows
```
.env\scripts\activate
```

Make sure your terminal prompt starts with the name of your virtual environment in parentheses. Something like this:

`(env) [user@hostname]$`

**Note:** to exit the virtual environment just run the command `deactivate`, after that your terminal prompt should be back to normal.

### Restore project dependencies

`pip install -r requirements.txt`

Windows

`python -m pip install -r requirements.txt`

### Start the server
```
python main.py
```

The server should be running successfully on: [localhost:5000](http://localhost:5000)
