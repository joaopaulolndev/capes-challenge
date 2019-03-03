import unittest

import settings


class TestConfig(unittest.TestCase):

    def test_config_loading(self):
        assert settings.FLASK_DEBUG is True
        assert settings.SQLALCHEMY_DATABASE_URI == 'sqlite:///db.sqlite'


if __name__ == '__main__':
    unittest.main()
