from enum import Enum


class LoanRating(Enum):
    """Available loan amount and percent rate according rating from -2 to 2."""
    PROHIBITED = (0, 0)
    LOW = (1, 1.5)
    MIDDLE = (5, 0)
    NORMAL = (10, -0.25)
    HIGH = (10, -0.75)

    @property
    def amount(self):
        return self.value[0]

    @property
    def percent(self):
        return self.value[1]


class Purpose(Enum):
    """Loan rate according purpose."""
    MORTGAGE = -2
    BUSINESS_DEVELOPMENT = -0.5
    CAR_LOAN = 0
    LOAN = 1.5


class IncomeSource(Enum):
    """Available loan amount and percent rate according income source."""
    PASSIVE = (1, 0.5)
    EMPLOYEE = (5, -0.25)
    BUSINESSMAN = (10, 0.25)
    UNEMPLOYED = (0, 0)

    @property
    def amount(self):
        return self.value[0]

    @property
    def percent(self):
        return self.value[1]


class Sex(Enum):
    """Retirement age according sex."""
    MALE = 65
    FEMALE = 60
