from src.strategies.payment_strategy import PaymentStrategy
from src.models.workday import WorkDay


class PayrollService:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_day(self, day: WorkDay) -> float:
        return self._strategy.calculate(day.hours_worked, day.hourly_rate)