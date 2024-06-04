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
        self.customer.borrow("1000", "0.1")
        self.assertEqual(self.customer.get_outstanding_debt(), 1100)

    def test_borrow_invalid_amount(self):
        self.assertRaises(ValueError, self.customer.borrow, "0", "0.1")

    def test_borrow_invalid_interest_rate(self):
        self.assertRaises(ValueError, self.customer.borrow, "1000", "test")

    def test_repay(self):
        self.customer.borrow("1000", "0.1")
        self.customer.repay("500")
        self.assertEqual(self.customer.get_outstanding_debt(), 600)
        self.assertEqual(self.customer.get_total_repayments(), 500)

    def test_repay_invalid_amount(self):
        self.assertRaises(ValueError, self.customer.repay, "0")

    def test_repay_more_than_outstanding_debt(self):
        self.customer.borrow("1000", "0.1")
        self.assertRaises(ValueError, self.customer.repay, "1200")

    def test_convert_to_decimal(self):
        self.assertEqual(self.customer.convert_to_decimal("1000"), 1000)

    def test_convert_to_decimal_invalid(self):
        self.assertRaises(ValueError, self.customer.convert_to_decimal, "test")


class TestBank(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank()
        self.customer = Customer("Zaki")
        self.bank.add_customer(self.customer)

    def tearDown(self) -> None:
        self.bank = None
        self.customer = None

    def test_add_customer(self):
        self.assertEqual(self.bank.customers, {self.customer})

    def test_lend(self):
        self.bank.lend(self.customer, "1000", "0.1")
        self.assertEqual(self.customer.get_outstanding_debt(), 1100)

    def test_receive_repayment(self):
        self.bank.lend(self.customer, "1000", "0.1")
        self.bank.receive_repayment(self.customer, "500")
        self.assertEqual(self.customer.get_outstanding_debt(), 600)
        self.assertEqual(self.customer.get_total_repayments(), 500)

    def test_get_customer_outstanding_debt(self):
        self.bank.lend(self.customer, "1000", "0.1")
        self.assertEqual(self.bank.get_customer_outstanding_debt(self.customer), 1100)

    def test_get_customer_total_repayments(self):
        self.bank.lend(self.customer, "1000", "0.1")
        self.bank.receive_repayment(self.customer, "500")
        self.assertEqual(self.bank.get_customer_total_repayments(self.customer), 500)


if __name__ == '__main__':
    unittest.main()
