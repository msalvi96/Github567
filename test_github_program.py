import unittest
from github_program import get_user
from unittest.mock import patch
from nose.tools import assert_is_not_none
from unittest.mock import Mock, patch

class TestGetUser(unittest.TestCase):
    def test_get_user(self):

        with self.assertRaises(TimeoutError):
            x = get_user('fwekfbewhkfbhkewfsdvdscdsc')

    def test_output(self):
        
        expected = [
            'Software-Testing',
            'delicious_food_blog',
            'CCAssist',
            'Triangle-567',
            'Portfolio',
            'Twitter-Sentiment-Analysis',
            'crypto_site',
            'flask_RESTful',
            'StevensRepo',
            'GEDCOM_Project'
        ]

        output_list = get_user('msalvi96', debug=True)
        for i in expected:
            self.assertIn(i, output_list)

    def test_request_response(self):

        response = get_user('msalvi96')
        assert_is_not_none(response)

    def test_mock_get_user(self):
        with patch('github567.github_program.requests.get') as mock_get:
            mock_get.return_value.ok = True
            response = get_user('msalvi96')

        assert_is_not_none(response)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)