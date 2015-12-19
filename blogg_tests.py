import os
import blogg
import unittest
import tempfile

class BloggTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, blogg.app.config['DATABASE'] = tempfile.mkstemp()
        blogg.app.config['TESTING'] = True
        self.app = blogg.app.test_client()
        blogg.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(blogg.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()