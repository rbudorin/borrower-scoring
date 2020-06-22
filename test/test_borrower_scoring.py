#!/usr/bin/python
# encoding: utf8

import pytest
from enums import *
from exceptions import *
from borrower_scoring import BorrowerScoring


class TestBorrowerScoring:

    __required_params = (
        'age',
        'income_amount',
        'loan_rating',
        'loan_amount',
        'credit_term',
        'sex',
        'income_source',
        'purpose'
    )

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 30,
                 'income_amount': 10,
                 'loan_rating': LoanRating.LOW,
                 'loan_amount': 1,
                 'credit_term': 5,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             0.2975
            ),
            ({
                 'age': 30,
                 'income_amount': 10,
                 'loan_rating': LoanRating.NORMAL,
                 'loan_amount': 1,
                 'credit_term': 5,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.BUSINESS_DEVELOPMENT
            },
             0.29500000000000004
            ),
            ({
                 'age': 30,
                 'income_amount': 10,
                 'loan_rating': LoanRating.MIDDLE,
                 'loan_amount': 1,
                 'credit_term': 5,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.CAR_LOAN
            },
             0.3025
            ),
            ({
                 'age': 30,
                 'income_amount': 10,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 1,
                 'credit_term': 5,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.LOAN
            },
             0.31
            )
        ]
    )
    def test_positive_rate_according_loan_rating_purpose_and_income_source_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 30,
                 'income_amount': 10,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 0.1,
                 'credit_term': 5,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             0.028500000000000004
            ),
            ({
                 'age': 30,
                 'income_amount': 10,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 5,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             1.3400514997831992
            ),
            ({
                 'age': 30,
                 'income_amount': 10,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 10,
                 'credit_term': 5,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             2.65
            )
        ]
    )
    def test_positive_rate_according_loan_amount_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 30,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 10,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             0.815051499783199
            ),
            ({
                 'age': 30,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 10,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.BUSINESS_DEVELOPMENT
            },
             0.8900514997831991
            ),
            ({
                 'age': 30,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 10,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.CAR_LOAN
            },
             0.9150514997831991
            ),
            ({
                 'age': 30,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 10,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.LOAN
            },
             0.9900514997831991
            )
        ]
    )
    def test_positive_purpose_rate_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 0,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 4,
                 'credit_term': 10,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             0.6559176003468815
            )
        ]
    )
    def test_positive_min_age_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 0.1,
                 'credit_term': 2,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.PASSIVE,
                 'purpose': Purpose.MORTGAGE
            },
             0.058750000000000004
            )
        ]
    )
    def test_positive_min_loan_amount_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 25,
                 'income_amount': 16,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 1,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             5.315051499783198
            ),
            ({
                 'age': 25,
                 'income_amount': 10,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             0.565051499783199
            )
        ]
    )
    def test_positive_credit_term_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 1.000001,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.PASSIVE,
                 'purpose': Purpose.MORTGAGE
            },
             None
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5.000001,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             None
            )
        ]
    )
    def test_negative_available_loan_amount_less_than_loan_amount_income_source_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 1,
                 'credit_term': 2,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.PASSIVE,
                 'purpose': Purpose.MORTGAGE
            },
             0.5775
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 6,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             1.1483848331165325
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 10,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             1.15
            )
        ]
    )
    def test_positive_available_loan_amount_equals_loan_amount_income_source_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.LOW,
                 'loan_amount': 1.000001,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             None
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.MIDDLE,
                 'loan_amount': 5.000001,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             None
            )
        ]
    )
    def test_negative_available_loan_amount_less_than_loan_amount_loan_rating_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.LOW,
                 'loan_amount': 1,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             0.14750000000000002
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.MIDDLE,
                 'loan_amount': 5,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             0.627551499783199
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.NORMAL,
                 'loan_amount': 10,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             1.2000000000000002
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 10,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            },
             1.15
            )
        ]
    )
    def test_positive_available_loan_amount_equals_loan_amount_loan_rating_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.MIDDLE,
                 'loan_amount': 1.000001,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.PASSIVE,
                 'purpose': Purpose.MORTGAGE
            },
             None
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.LOW,
                 'loan_amount': 1.000001,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             None
            )
        ]
    )
    def test_negative_available_loan_amount_less_than_loan_amount_loan_rating_and_income_source_min_condition(
            self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.MIDDLE,
                 'loan_amount': 1,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.PASSIVE,
                 'purpose': Purpose.MORTGAGE
            },
             0.135
            ),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.LOW,
                 'loan_amount': 1,
                 'credit_term': 20,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             0.14250000000000002
            )
        ]
    )
    def test_positive_available_loan_amount_more_than_loan_amount_loan_rating_and_income_source_min_condition(
            self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                'age': 25,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.UNEMPLOYED,
                'purpose': Purpose.MORTGAGE
            },
             None
            )
        ]
    )
    def test_negative_unemployed_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                'age': 30,
                'income_amount': 1,
                'loan_rating': LoanRating.NORMAL,
                'loan_amount': 1,
                'credit_term': 2,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.BUSINESSMAN,
                'purpose': Purpose.CAR_LOAN
            },
             None
            )
        ]
    )
    def test_negative_year_payment_more_than_half_income_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                'age': 25,
                'income_amount': 5,
                'loan_rating': LoanRating.PROHIBITED,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            },
             None
            )
        ]
    )
    def test_negative_unreliable_borrower_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                'age': (Sex.FEMALE.value - 19),
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            },
             None
            ),
            ({
                 'age': (Sex.MALE.value - 1),
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 2,
                 'sex': Sex.MALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             None
            ),
            ({
                 'age': Sex.FEMALE.value,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 1,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             None
            )
        ]
    )
    def test_negative_retirement_age_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                'age': (Sex.FEMALE.value - 20),
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            },
             0.565051499783199
            ),
            ({
                 'age': Sex.MALE.value - 2,
                 'income_amount': 10,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 2,
                 'sex': Sex.MALE,
                 'income_source': IncomeSource.EMPLOYEE,
                 'purpose': Purpose.MORTGAGE
            },
             2.815051499783199
            )
        ]
    )
    def test_positive_last_payment_age_equals_retirement_age_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                'age': 25,
                'income_amount': 9,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 9.000003,
                'credit_term': 3,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.BUSINESSMAN,
                'purpose': Purpose.MORTGAGE
            },
             None
            )
        ]
    )
    def test_negative_income_amount_credit_term_ratio_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        ('testdata', 'expected'), [
            ({
                'age': 25,
                'income_amount': 9,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 9,
                'credit_term': 3,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.BUSINESSMAN,
                'purpose': Purpose.MORTGAGE
            },
             3.5891181741504607
            )
        ]
    )
    def test_positive_third_of_income_amount_equals_net_payment_condition(self, testdata, expected):
        assert self.__exec_score(params=testdata) == expected

    @pytest.mark.parametrize(
        'testdata', [
            ({
                'age': 25,
                'income_amount': 5,
                'loan_rating': 2,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.BUSINESSMAN,
                'purpose': Purpose.MORTGAGE
            })
        ]
    )
    def test_invalid_loan_rating_exception(self, testdata):
        with pytest.raises(InvalidLoanRatingException):
            self.__exec_score(params=testdata)

    @pytest.mark.parametrize(
        'testdata', [
            ({
                'age': 25,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 0,
                'sex': Sex.FEMALE,
                'income_source': IncomeSource.BUSINESSMAN,
                'purpose': Purpose.MORTGAGE
            }),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 21,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            }),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 0.999999,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            }),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 20.000001,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            }),
            ({
                 'age': 25,
                 'income_amount': 5,
                 'loan_rating': LoanRating.HIGH,
                 'loan_amount': 5,
                 'credit_term': 10.5,
                 'sex': Sex.FEMALE,
                 'income_source': IncomeSource.BUSINESSMAN,
                 'purpose': Purpose.MORTGAGE
            })
        ]
    )
    def test_invalid_credit_term_exception(self, testdata):
        with pytest.raises(InvalidCreditTermException):
            self.__exec_score(params=testdata)

    @pytest.mark.parametrize(
        'testdata', [
            ({
                'age': -1,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            }),
            ({
                'age': -0.000001,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            }),
            ({
                'age': 0.000001,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            })
        ]
    )
    def test_invalid_age_exception(self, testdata):
        with pytest.raises(InvalidAgeException):
            self.__exec_score(params=testdata)

    @pytest.mark.parametrize(
        'testdata', [
            ({
                'age': 20,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 10.000001,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            }),
            ({
                'age': 20,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 0.099999,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            })
        ]
    )
    def test_invalid_loan_amount_exception(self, testdata):
        with pytest.raises(InvalidLoanAmountException):
            self.__exec_score(params=testdata)

    @pytest.mark.parametrize(
        'testdata', [
            ({
                'age': 20,
                'income_amount': 0,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            }),
            ({
                'age': 20,
                'income_amount': 0.999999,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            }),
            ({
                'age': 20,
                'income_amount': 1.000001,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            }),
        ]
    )
    def test_invalid_income_amount_exception(self, testdata):
        with pytest.raises(InvalidIncomeAmountException):
            self.__exec_score(params=testdata)

    @pytest.mark.parametrize(
        'testdata', [
            ({
                'age': 25,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': 1,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': Purpose.MORTGAGE
            })
        ]
    )
    def test_invalid_sex_exception(self, testdata):
        with pytest.raises(InvalidSexException):
            self.__exec_score(params=testdata)

    @pytest.mark.parametrize(
        'testdata', [
            ({
                'age': 25,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': IncomeSource.EMPLOYEE,
                'purpose': ''
            })
        ]
    )
    def test_invalid_purpose_exception(self, testdata):
        with pytest.raises(InvalidPurposeException):
            self.__exec_score(params=testdata)

    @pytest.mark.parametrize(
        'testdata', [
            ({
                'age': 25,
                'income_amount': 5,
                'loan_rating': LoanRating.HIGH,
                'loan_amount': 5,
                'credit_term': 20,
                'sex': Sex.MALE,
                'income_source': None,
                'purpose': Purpose.MORTGAGE
            })
        ]
    )
    def test_invalid_income_source_exception(self, testdata):
        with pytest.raises(InvalidIncomeSourceException):
            self.__exec_score(params=testdata)

    def __exec_score(self, params):
        if not self.__is_params_valid(params=params):
            raise ValueError

        borrower_scoring = BorrowerScoring(
            age=params['age'],
            income_amount=params['income_amount'],
            loan_rating=params['loan_rating'],
            loan_amount=params['loan_amount'],
            credit_term=params['credit_term'],
            sex=params['sex'],
            income_source=params['income_source'],
            purpose=params['purpose']
        )

        return borrower_scoring.score()

    def __is_params_valid(self, params):
        for param in self.__required_params:
            if param not in params:
                return False

        return True
