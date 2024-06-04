import unittest

from bank_system import Customer, Bank


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


class TestBank(unittest.TestCase):

    def setUp(self) -> None:
        self.bank = Bank()
        self.customer = Customer("Zaki")
        self.bank.add_customer(self.customer)

    def tearDown(self) -> None:
        self.bank = None
        self.customer = None

    def test_add_customer(self):
        self.assertRaises(ValueError, self.bank.add_customer, self.customer)

    def test_lend(self):
        self.bank.lend("Zaki", 1000, 0.1)
        self.assertEqual(self.customer.get_outstanding_debt(), 1100)

    def test_lend_invalid_customer(self):
        self.assertRaises(ValueError, self.bank.lend, "Zak", 1000, 0.1)

    def test_receive_repayment(self):
        self.bank.lend("Zaki", 1000, 0.1)
        self.bank.receive_repayment("Zaki", 500)
        self.assertEqual(self.customer.get_outstanding_debt(), 600)
        self.assertEqual(self.customer.get_total_repayments(), 500)


if __name__ == "__main__":
    unittest.main()
