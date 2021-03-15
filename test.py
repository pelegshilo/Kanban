import unittest
from kanban import create_app
from kanban.db import get_db
import sqlite3
import requests

class MyTestCase(unittest.TestCase):
    url = "http://localhost:5000/"
    def setUp(self):
        self.app = create_app()

    def test_mainpage(self):
        # Check that we have a functional main page
        r = requests.get(self.url)
        assert r.status_code == 200
        # Check that the output is correct
        assert "My Kanban Board" in r.text
        assert "Add Task:" in r.text
        assert "To do" in r.text

    def test_get_close_db(self):
        with self.app.app_context():
            db = get_db()
            assert db is get_db()

        with self.assertRaises(sqlite3.ProgrammingError):
            db.execute('SELECT 1')

    def test_task_lifecycle(self):
        # Test task creation
        create = requests.post(self.url, data={"title": "test", "desc": "this is a test"})
        assert create.status_code == 200
        # Check that the task was created
        with self.app.app_context():
            assert get_db().execute(
                "SELECT * from task where title = 'test'"
            ).fetchone() is not None
        #Check that the task is visible
        assert "this is a test" in create.text
        # Test task updating
        update = requests.post(self.url + "update", data={"status": "done", "id": 1})
        assert update.status_code == 200
        # Check that the task was updated correctly
        with self.app.app_context():
            assert get_db().execute(
                "SELECT * from task where id = 1 and category = 'done'"
            ).fetchone() is not None
        # Test task deletion
        delete = requests.post(self.url + "delete", data={"id": "1"})
        assert delete.status_code == 200
        # Check that the task was deleted properly
        with self.app.app_context():
            assert get_db().execute(
                "SELECT * from task where id = 1"
            ).fetchone() is None


if __name__ == '__main__':
    unittest.main()
