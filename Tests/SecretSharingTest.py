import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from Source import ShamirScheme


class SecretTestMethods(unittest.TestCase):
    def setUp(self):
        self.secret = "thisisasharedsecretvaluethatwillbesharedwithNusersandaTthreshold"
        self.threshold = 7
        self.num_shares = 9
        self.shamir = ShamirScheme.ShamirScheme()


    def test_split_of_secret(self):
        splitSecret = self.shamir.split_secret(self.secret, self.num_shares, self.threshold)
        self.assertEqual(9, len(splitSecret))


    def test_char_to_int_and_back_conversion(self):
        initString = "helloworld"
        stringAsInt = ShamirScheme.string_to_int(initString)
        backToString = ShamirScheme.int_to_string(stringAsInt)

        self.assertEqual(initString, backToString)


    def test_char_to_int_and_back_conversion_longer_string(self):
        initString = "thisisasharedsecretvaluethatwillbesharedwithNusersandaTthreshold"
        stringAsInt = ShamirScheme.string_to_int(initString)
        backToString = ShamirScheme.int_to_string(stringAsInt)

        self.assertEqual(initString, backToString)


    def test_split_and_recover_secret_1(self):
        self.secret = 'abc'
        shares = self.shamir.split_secret(self.secret, self.num_shares, self.threshold)
        recoveredSecret = self.shamir.recover_secret(shares)
        self.assertEqual(self.secret, recoveredSecret)


    def test_split_and_recover_secret_2(self):
        self.secret = 'thisisasharedsecretvaluethatwillbesharedwithNusersandaTthreshold'
        shares = self.shamir.split_secret(self.secret, self.num_shares, self.threshold)
        recoveredSecret = self.shamir.recover_secret(shares)
        self.assertEqual(self.secret, recoveredSecret)


    def test_split_and_recover_secret_3(self):
        self.secret = 'the nuclear code is 1234'
        shares = self.shamir.split_secret(self.secret, self.num_shares, self.threshold)
        recoveredSecret = self.shamir.recover_secret(shares)
        self.assertEqual(self.secret, recoveredSecret)


    def test_threshold_as_1_no_secrecy(self):
        shares = self.shamir.split_secret(self.secret, 2, 1)
        self.assertEqual(shares[0][1], shares[1][1])

# end Class SecretTestMethods


if __name__ == '__main__':
    unittest.main()
