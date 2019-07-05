## Flask Backend Server

#### For more info: http://flask.pocoo.org/docs/1.0/installation/

###### Prerequisites
- Python 3  
- Pip 19.1.1  

###### General commands:
- `pip install virtualenv` - Installs virtualenv so that our dependencies are kept locally  
- `python3 -m venv venv` - Create virtualenv in the folder  
- `. venv/bin/activate` - Activate virtualenv in Mac/Linux  

###### Pip Cheat-sheet

- `pip install -r requirements.txt` - Installs all the dependencies in the `requirements.txt`  
- `pip freeze > requirements.txt` - To install a new dependency  
- `pip list` - View all dependencies  
 
###### Mac/Linux: (development server)  
- `export FLASK_ENV=development`  
- `export FLASK_APP=init.py`  
- `flask run`  