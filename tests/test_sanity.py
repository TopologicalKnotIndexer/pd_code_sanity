import unittest

from pd_code_sanity import sanity


class SanityTests(unittest.TestCase):
    def test_accepts_integer_string_and_empty_codes(self):
        self.assertTrue(sanity([[1, 1, 2, 2]]))
        self.assertTrue(sanity([["a", "a", "b", "b"]]))
        self.assertTrue(sanity([]))

    def test_rejects_invalid_shapes_counts_and_types(self):
        self.assertFalse(sanity(((1, 1, 2, 2),)))
        self.assertFalse(sanity([(1, 1, 2, 2)]))
        self.assertFalse(sanity([[1, 2, 3, 4]]))
        self.assertFalse(sanity([[True, 1, True, 1]]))
        self.assertFalse(sanity([[1, 1, "2", "2"]]))


if __name__ == "__main__":
    unittest.main()
