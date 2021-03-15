from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from kanban.db import get_db

bp = Blueprint('kanban', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    # Returns the main page

    # fetches the tasks by grouping and creates the main page when the page is viewed
    if request.method == 'GET':
        db = get_db()
        todo_tasks = db.execute(
            'SELECT *'
            ' FROM task p'
            ' WHERE category == "todo"'
            ' ORDER BY created ASC'
        ).fetchall()
        doing_tasks = db.execute(
            'SELECT *'
            ' FROM task p'
            ' WHERE category == "doing"'
            ' ORDER BY created ASC'
        ).fetchall()
        done_tasks = db.execute(
            'SELECT *'
            ' FROM task p'
            ' WHERE category == "done"'
            ' ORDER BY created ASC'
        ).fetchall()
        return render_template('index.html', todo_tasks=todo_tasks, doing_tasks=doing_tasks, done_tasks=done_tasks)
    # When a task is created, adds it to the database
    else:
        title = request.form['title']
        description = request.form['desc']

        db = get_db()
        db.execute(
            'INSERT INTO task (category, title, description)'
            ' VALUES (?, ?, ?)',
            ("todo", title, description)
        )
        db.commit()
        return redirect(url_for('kanban.index'))


@bp.route('/update', methods=('POST',))
def update():
    # Updates the status of a task
    category = request.form['status']
    id = request.form['id']
    db = get_db()
    db.execute(
        'UPDATE task'
        ' SET category == ?'
        ' WHERE id == ?'
        ,
        (category, id)
    )
    db.commit()
    return redirect(url_for('kanban.index'))


@bp.route('/delete', methods=('POST',))
def delete():
    # Deletes a task
    id = request.form['id']
    db = get_db()
    db.execute(
        'DELETE FROM task'
        ' WHERE id == ?'
        ,
        (id)
    )
    db.commit()
    return redirect(url_for('kanban.index'))
