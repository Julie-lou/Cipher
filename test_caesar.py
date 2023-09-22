import unittest
from caesar import caesar


class CAESAR(unittest.TestCase):

    def test_encrypt_caesar(self):
        self.assertEqual(caesar("hello", 20, "e"), "byffi")
        self.assertEqual(caesar("aupp", 90, "e"), "mgbb")
        self.assertEqual(caesar("aupp", 2, "e"), "cwrr")

    def test_decrypt_caesar(self):
        self.assertEqual(caesar("byffi", 20, "d"), "hello")
        self.assertEqual(caesar("mgbb", 90, "d"), "aupp")
        self.assertEqual(caesar("cwrr", 2, "d"), "aupp")

    def test_error_caesar(self):
        self.assertEqual(caesar("hello", 26, "e"), "invalid shift number")
        self.assertEqual(caesar("hello", -3, "e"), "invalid shift number")
        self.assertEqual(caesar("cwrr", -3, "d"), "invalid shift number")
        self.assertEqual(caesar("cwrr", 25, "g"), "invalid option")


if __name__ == '__main__':
    unittest.main()
