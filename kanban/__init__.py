import os
from flask import Flask
import sqlite3

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'kanban.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import and initialize the db
    from . import db
    db.init_app(app)
    db_conn = sqlite3.connect(
        app.config['DATABASE'],
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    db_conn.row_factory = sqlite3.Row
    with app.open_resource('schema.sql') as f:
        db_conn.executescript(f.read().decode('utf8'))

    #import and register the main page and its functions
    from . import kanban
    app.register_blueprint(kanban.bp)
    app.add_url_rule('/', endpoint='index')

    return app
