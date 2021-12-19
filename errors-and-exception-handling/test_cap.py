import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_two_word(self):
        text = 'another python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Another Python')


if __name__ == "__main__":
    unittest.main()
