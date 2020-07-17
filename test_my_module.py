import unittest

import my_module

from unittest import mock


class TestMyModule(unittest.TestCase):
    def test_foo(self):
        client = mock.MagicMock()
        client.query = mock.MagicMock(return_value=[])
        query = "SELECT 1"
        y = my_module.foo(client, query)
        self.assertEqual(y, [3])
        client.query.assert_called_with(query)  # will raise an error if false

    @mock.patch('my_module.bigquery.Client', return_value=mock.MagicMock(return_value=[]))
    def test_bar(self, mock_client_factory):
        query = "SELECT 1"
        y = my_module.bar("project_mayhem", query)
        self.assertEqual(y, [3])
        mock_client_factory.assert_called_with("project_mayhem")

