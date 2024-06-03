import unittest


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__outstanding_debt = 0
        self.__total_repayments = 0

    def borrow(self, amount: float, interest_rate: float) -> None:
        """
            borrow an amount from the bank
        """
        if amount <= 0:
            raise ValueError("Amount should be greater than 0")
        self.__outstanding_debt += amount + amount * interest_rate

    def repay(self, amount: float) -> None:
        """
            repay an amount from the customer's outstanding debt
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
    def __init__(self) -> None:
        self.customers = {}

    def add_customer(self, customer: Customer) -> None:
        if customer.name in self.customers:
            raise ValueError("Customer already exists")
        self.customers[customer.name] = customer

    def lend(self, customer_name: str, amount: float, interest_rate: float) -> None:
        if customer_name not in self.customers:
            raise ValueError("Customer does not exist")
        self.customers[customer_name].borrow(amount, interest_rate)

    def receive_repayment(self, customer_name: str, amount: float) -> None:
        if customer_name not in self.customers:
            raise ValueError("Customer does not exist")
        self.customers[customer_name].repay(amount)

    def get_customer_outstanding_debt(self, customer_name: str) -> float:
        if customer_name not in self.customers:
            raise ValueError("Customer does not exist")
        return self.customers[customer_name].get_outstanding_debt()

    def get_customer_total_repayments(self, customer_name: str) -> float:
        if customer_name not in self.customers:
            raise ValueError("Customer does not exist")
        return self.customers[customer_name].get_total_repayments()

# TODO :
# 1- test cases
# 2- write a method to validate that the customer exists
