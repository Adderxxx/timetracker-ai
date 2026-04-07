from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def calculate(self, hours: float, rate: float) -> float:
        pass


class OvertimePaymentStrategy(PaymentStrategy):
    STANDARD_LIMIT = 8
    OVERTIME_MULTIPLIER = 1.5

    def calculate(self, hours: float, rate: float) -> float:
        if hours <= self.STANDARD_LIMIT:
            return hours * rate * 1.2

        regular_pay = self.STANDARD_LIMIT * rate
        overtime_hours = hours - self.STANDARD_LIMIT
        overtime_pay = overtime_hours * (rate * self.OVERTIME_MULTIPLIER)

        return regular_pay + overtime_pay