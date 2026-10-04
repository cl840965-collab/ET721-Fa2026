import unittest

from bankaccount import BankAccount

class TestBank(unittest.TestCase):
    def setUp(self):
        self.emp1 = BankAccount("Claudio", 1000)
    def test_Balance(self):
        self.assertEqual(self.emp1.get_balance(), 1000)
    def test_Deposit(self):
        self.emp1.deposit(100)
        self.assertEqual(self.emp1.get_balance(), 1100)
    def test_Withdraw(self):
        self.emp1.withdraw(100)
        self.assertEqual(self.emp1.get_balance(), 900)
    def test_Withdraw_error(self):
        with self.assertRaises(ValueError):
            self.emp1.withdraw(5000)
    def test_bunch(self):
        self.emp1.deposit(1000)
        self.emp1.withdraw(500)
        self.emp1.deposit(1000)
        self.emp1.withdraw(900)
        self.assertEqual(self.emp1.get_balance(), 1600)

if __name__ =="__main__":
    unittest.main()