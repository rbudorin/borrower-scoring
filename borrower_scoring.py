import math
from exceptions import *
from enums import *


class BorrowerScoring:

    __age = None
    __income_amount = None
    __loan_rating = None
    __loan_amount = None
    __credit_term = None
    __sex = None
    __income_source = None
    __purpose = None
    __base_rate = 10

    def __init__(self, age, income_amount, loan_rating, loan_amount, credit_term, sex, income_source, purpose):
        if age < 0 or type(age) is not int:
            raise InvalidAgeException

        if income_amount < 1 or type(income_amount) is not int:
            raise InvalidIncomeAmountException

        if not isinstance(loan_rating, LoanRating):
            raise InvalidLoanRatingException

        if loan_amount < 0.1 or loan_amount > 10:
            raise InvalidLoanAmountException

        if credit_term not in range(1, 21):
            raise InvalidCreditTermException

        if not isinstance(sex, Sex):
            raise InvalidSexException

        if not isinstance(income_source, IncomeSource):
            raise InvalidIncomeSourceException

        if not isinstance(purpose, Purpose):
            raise InvalidPurposeException

        self.__age = age
        self.__income_amount = income_amount
        self.__loan_rating = loan_rating
        self.__loan_amount = loan_amount
        self.__credit_term = credit_term
        self.__sex = sex
        self.__income_source = income_source
        self.__purpose = purpose

    def score(self):
        if self.__is_unreliable_borrower():
            return None

        if self.__is_loan_rating_prohibited():
            return None

        if self.__is_last_payment_date_more_than_retirement_age():
            return None

        if self.__is_payment_less_than_third_of_income():
            return None

        if self.__is_available_loan_amount_less_than_desired():
            return None

        payment = self.__get_payment()

        if payment > (self.__income_amount / 2):
            return None

        return payment

    def __is_unreliable_borrower(self):
        return self.__income_source == IncomeSource.UNEMPLOYED

    def __is_loan_rating_prohibited(self):
        return self.__loan_rating == LoanRating.PROHIBITED

    def __is_last_payment_date_more_than_retirement_age(self):
        return (self.__age + self.__credit_term) > self.__sex.value

    def __get_available_loan_amount(self):
        return min(self.__income_source.amount, self.__loan_rating.amount)

    def __is_payment_less_than_third_of_income(self):
        return self.__loan_amount / self.__credit_term > self.__income_amount / 3

    def __is_available_loan_amount_less_than_desired(self):
        return self.__get_available_loan_amount() < self.__loan_amount

    def __get_loan_amount_rate(self):
        return math.log10(self.__loan_amount)

    def __get_rate(self):
        rate = self.__base_rate
        rate += sum([self.__purpose.value, self.__loan_rating.percent, self.__income_source.percent])
        rate -= self.__get_loan_amount_rate()

        return rate

    def __get_payment(self):
        return (self.__loan_amount * (1 + self.__credit_term * (self.__get_rate() / 100))) / self.__credit_term
