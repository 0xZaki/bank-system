from decimal import Decimal, getcontext

# set the precision to 2 decimal places
getcontext().prec = 2


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__outstanding_debt = Decimal('0.0')
        self.__total_repayments = Decimal('0.0')

    @staticmethod
    def convert_to_decimal(number_str: str) -> Decimal:
        """
            convert string to a decimal number and raise exception if the string is not a valid number
        :param number_str:
        :return Decimal: the number as a decimal
        """
        try:
            return Decimal(number_str)
        except Exception:
            raise ValueError(f"{number_str} is not a valid number")

    def borrow(self, amount: str, interest_rate: str) -> None:
        """
            borrow an amount from the bank
        :param amount :
        :param interest_rate: a percentage written as a decimal (0.1 for 10%)
        :return:
        """
        amount = self.convert_to_decimal(amount)
        interest_rate = self.convert_to_decimal(interest_rate)
        if amount <= 0:
            raise ValueError("Amount should be greater than 0")
        self.__outstanding_debt += amount + amount * interest_rate

    def repay(self, amount: str) -> None:
        """
            repay an amount of the outstanding debt
        :param amount:
        :return:
        """
        amount = self.convert_to_decimal(amount)
        if amount > self.__outstanding_debt:
            raise ValueError("Amount can't be more than the outstanding debt")
        elif amount <= 0:
            raise ValueError("Amount should be greater than 0")
        self.__total_repayments += amount
        self.__outstanding_debt -= amount

    def get_outstanding_debt(self) -> Decimal:
        return self.__outstanding_debt

    def get_total_repayments(self) -> Decimal:
        return self.__total_repayments


class Bank:
    """
        A bank class that manages customers and their debts
    """

    def __init__(self) -> None:
        self.customers = set()

    def __validate_customer_exists(self, customer: Customer) -> None:
        if customer not in self.customers:
            raise ValueError("Customer does not exist")

    def add_customer(self, customer: Customer) -> None:
        """
            add a customer to the bank
        :param customer:
        :return:
        """
        self.customers.add(customer)

    def lend(self, customer: Customer, amount: str, interest_rate: str) -> None:
        """
            lend an amount to customer
        :param customer:
        :param amount:
        :param interest_rate:
        :return:
        """
        self.__validate_customer_exists(customer)
        customer.borrow(amount, interest_rate)

    def receive_repayment(self, customer: Customer, amount: str) -> None:
        """
            receive a repayment from customer
        :param customer:
        :param amount:
        :return:
        """
        self.__validate_customer_exists(customer)
        customer.repay(amount)

    def get_customer_outstanding_debt(self, customer: Customer) -> Decimal:
        self.__validate_customer_exists(customer)
        return customer.get_outstanding_debt()

    def get_customer_total_repayments(self, customer: Customer) -> Decimal:
        self.__validate_customer_exists(customer)
        return customer.get_total_repayments()


if __name__ == '__main__':
    test_customer = Customer("test")
    test_customer.borrow(1000, 0.1)
    print("=== After borrowing 1000 with 10% interest ===")
    print(f"total repayments are {test_customer.get_total_repayments():.2f}")
    print(f"outstanding debt is {test_customer.get_outstanding_debt():.2f}")

    print(f"\n=== After paying 500 ===")
    test_customer.repay(500)
    print(f"total repayments are {test_customer.get_total_repayments():.2f}")
    print(f"outstanding debt is {test_customer.get_outstanding_debt():.2f}")
