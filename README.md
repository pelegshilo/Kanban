# Kanban Board

This is an application for a Kanban board built with flask. 

##Installation
To install the application, simply run
```
python3 -m venv .venv 
source .venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=app.py
flask run
```

## Testing
To run the unit tests, simply run
```
python3 -m unittest discover test
```

## How it looks
![site-image](https://imgur.com/TC5UXpe.png)

## Extra Features
- Warnings on deletion of tasks
- Updating via drop-down with appropriate default selected for each column
- Lots of CSS to make the site look better