from src.models.workday import WorkDay, InvalidHoursError
from src.strategies.payment_strategy import OvertimePaymentStrategy
from src.services.payroll_service import PayrollService


def main():
    print("=== TimeTracker AI ===")

    try:
        horas = float(input("Ingrese horas trabajadas: "))
        tarifa = float(input("Ingrese tarifa por hora: "))

        day = WorkDay(horas, tarifa)
        service = PayrollService(OvertimePaymentStrategy())

        total = service.process_day(day)

        print(f"Total a pagar: {total}")

    except InvalidHoursError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos")


if __name__ == "__main__":
    main()