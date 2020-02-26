import unittest
from github_program import get_user
from unittest.mock import patch
from nose.tools import assert_is_not_none
from unittest import mock

class TestGetUser(unittest.TestCase):
    def test_get_user(self):
        requests = mock.Mock()
        requests.get.side_effect = TimeoutError

        with self.assertRaises(TimeoutError):
            x = get_user('fwekfbewhkfbhkewfsdvdscdsc')

        response = get_user('msalvi96')
        assert_is_not_none(response)

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
            'GEDCOM_Project',
            'PeekList'
        ]

        output_list = get_user('msalvi96', debug=True)
        for i in expected:
            self.assertIn(i, output_list)
    
    def test_mock_get_user(self):

        response_mock = mock.Mock()
        response_mock.status_code = 200

        response_mock.json.return_value = {
            'Software-Testing': 11,
            'delicious_food_blog': 10,
            'CCAssist': 9,
            'Triangle-567': 8,
            'Portfolio': 7,
            'Twitter-Sentiment-Analysis': 6,
            'crypto_site': 5,
            'flask_RESTful': 4,
            'StevensRepo': 3,
            'GEDCOM_Project': 2,
            'LinkSocial': 5,
            'Github567': 7,
            'PeekList': 7
        }

        return response_mock

    @mock.patch('requests.get')
    def test_mock_user(self, mock_get):
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
            'GEDCOM_Project',
            'LinkSocial',
            'Github567',
            'PeekList'
        ]
        requests = mock.Mock()
        requests.get.side_effect = self.test_mock_get_user
        x = get_user('msalvi96')
        output = {}
        for i in x:
            output[i[0]] = i[1]

        for key, values in output.items():
            self.assertIn(key, expected)
            self.assertIsInstance(values, int)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
