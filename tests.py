import unittest

from bank_system import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self) -> None:
        self.customer = Customer("Zaki")

    def tearDown(self) -> None:
        self.customer = None

    def test_init(self):
        self.assertEqual(self.customer.name, "Zaki")
        self.assertEqual(self.customer.get_outstanding_debt(), 0)
        self.assertEqual(self.customer.get_total_repayments(), 0)

    def test_borrow(self):
        self.customer.borrow(1000, 0.1)
        self.assertEqual(self.customer.get_outstanding_debt(), 1100)

    def test_borrow_invalid_amount(self):
        self.assertRaises(ValueError, self.customer.borrow, 0, 0.1)

    def test_repay(self):
        self.customer.borrow(1000, 0.1)
        self.customer.repay(500)
        self.assertEqual(self.customer.get_outstanding_debt(), 600)
        self.assertEqual(self.customer.get_total_repayments(), 500)

    def test_repay_more_than_outstanding_debt(self):
        self.customer.borrow(1000, 0.1)
        self.assertRaises(ValueError, self.customer.repay, 1200)

    def test_repay_invalid_amount(self):
        self.assertRaises(ValueError, self.customer.repay, 0)


if __name__ == "__main__":
    unittest.main()
