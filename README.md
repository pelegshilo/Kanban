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

## Project Structure
- The folder kanban contains the main application files
    - The folder static contains the static css code
    - The folder templates contains the html code. Index.html is the base template and task.html is the code for every task
    - \_\_init__.py initializes the app, db.py handles the db, and schema.sql has the database schema
    - kanban.py is the main file containing the website method implementations
- test.py contains the project tests
- Otherwise, we have the usual readme, requirements and .gitignore files

## Extra Features
- Warnings on deletion of tasks
- Updating via drop-down with appropriate default selected for each column
- Lots of CSS to make the site look better