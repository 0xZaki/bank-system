class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__outstanding_debt = 0
        self.__total_repayments = 0

    def borrow(self, amount: float, interest_rate: float) -> None:
        """
            borrow an amount from the bank
        :param amount :
        :param interest_rate: a percentage written as a decimal (0.1 for 10%)
        :return:
        """
        if amount <= 0:
            raise ValueError("Amount should be greater than 0")
        self.__outstanding_debt += amount + amount * interest_rate

    def repay(self, amount: float) -> None:
        """
            repay an amount of the outstanding debt
        :param amount:
        :return:
        """
        if amount > self.__outstanding_debt:
            raise ValueError("Amount can't be more than the outstanding debt")
        elif amount <= 0:
            raise ValueError("Amount should be greater than 0")
        self.__total_repayments += amount
        self.__outstanding_debt -= amount

    def get_outstanding_debt(self) -> float:
        return self.__outstanding_debt

    def get_total_repayments(self) -> float:
        return self.__total_repayments


class Bank:
    """
        A bank class that manages customers and their debts
    """

    def __init__(self) -> None:
        self.customers = {}

    def __validate_customer_exists(self, customer_name: str) -> None:
        """
            validate if the customer exists
        :param customer_name:
        :return:
        """
        if customer_name not in self.customers:
            raise ValueError("Customer does not exist")

    def add_customer(self, customer: Customer) -> None:
        """
            add a customer to the bank
        :param customer:
        :return:
        """
        if customer.name in self.customers:
            raise ValueError("Customer already exists")
        self.customers[customer.name] = customer

    def lend(self, customer_name: str, amount: float, interest_rate: float) -> None:
        """
            lend an amount to customer
        :param customer_name:
        :param amount:
        :param interest_rate:
        :return:
        """
        self.__validate_customer_exists(customer_name)
        self.customers[customer_name].borrow(amount, interest_rate)

    def receive_repayment(self, customer_name: str, amount: float) -> None:
        """
            receive repayment amount from customer
        :param customer_name:
        :param amount:
        :return:
        """
        self.__validate_customer_exists(customer_name)
        self.customers[customer_name].repay(amount)

    def get_customer_outstanding_debt(self, customer_name: str) -> float:
        self.__validate_customer_exists(customer_name)
        return self.customers[customer_name].get_outstanding_debt()

    def get_customer_total_repayments(self, customer_name: str) -> float:
        self.__validate_customer_exists(customer_name)
        return self.customers[customer_name].get_total_repayments()


if __name__ == '__main__':
    zaki = Customer("Zaki")
    bank = Bank()
    bank.add_customer(zaki)
    bank.lend("Zaki", 1000, 0.1)
    print("Outstanding debt: ", bank.get_customer_outstanding_debt("Zaki"))
    bank.receive_repayment("Zaki", 500)
    print("Outstanding debt: ", bank.get_customer_outstanding_debt("Zaki"))
    print("Total repayments: ", bank.get_customer_total_repayments("Zaki"))
