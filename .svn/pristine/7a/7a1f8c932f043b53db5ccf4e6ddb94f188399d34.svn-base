__author__ = 'Jessica'

import unittest
from flask import jsonify
import server
import os
import tempfile
import json

class Database_Test(unittest.TestCase):

    def setUp(self):
        self.db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        server.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(server.app.config['DATABASE'])

    def test_insert_vocab(self):
        sentence = "The birds ran away from the mouse."
        rv = self.app.post('/submit', data=dict(
            sentence=sentence
        ), follow_redirects=True)
        data_string = rv.data.decode('ascii')
        data_dict = json.loads(data_string)
        self.assertEqual(data_dict['word_cats']['NOUN'][0], 'birds')
        self.assertEqual(data_dict['word_cats']['NOUN'][1], 'mouse')
        self.assertEqual(data_dict['word_cats']['VERB'][0], 'ran')
        self.assertEqual(data_dict['word_cats']['.'][0], '.')
        self.assertEqual(data_dict['word_cats']['DET'][0], 'the')
        self.assertEqual(data_dict['word_cats']['ADV'][0], 'away')
        self.assertEqual(data_dict['word_cats']['ADP'][0], 'from')

if __name__ == '__main__':
    unittest.main()