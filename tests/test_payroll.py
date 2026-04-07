print("🔥 EJECUTANDO TEST 🔥")
import unittest
from src.models.workday import WorkDay, InvalidHoursError
from src.strategies.payment_strategy import OvertimePaymentStrategy
from src.services.payroll_service import PayrollService


class TestPayroll(unittest.TestCase):

    def setUp(self):
        self.service = PayrollService(OvertimePaymentStrategy())

    def test_overtime_calculation(self):
        day = WorkDay(10, 20)
        self.assertEqual(self.service.process_day(day), 220.0)

    def test_normal_hours(self):
        day = WorkDay(5, 20)
        self.assertEqual(self.service.process_day(day), 100.0)

    def test_invalid_hours(self):
        with self.assertRaises(InvalidHoursError):
            WorkDay(25, 20)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPayroll)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)