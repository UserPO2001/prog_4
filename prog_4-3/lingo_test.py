import unittest
from lingo import LingoApp

class TestLingoApp(unittest.TestCase):
    def test_selecteer_woord(self):
        app = LingoApp()
        word = app.selecteer_woord()
        self.assertEqual(len(word), 5)
        self.assertIsInstance(word, str)

if __name__ == "__main__":
    unittest.main()
