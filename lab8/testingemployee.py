import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee("Peter", "Pan", 90000)

    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, "p.pan@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Peter Pan")

    def test_applt_raise(self):
        self.emp1.apply_raise()

        self.assertEqual(self.emp1.salary, 94500)
if __name__ =="__main__":
    unittest.main()