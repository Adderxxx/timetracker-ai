class TimeTrackerError(Exception):
    """Excepción base del sistema"""
    pass


class InvalidHoursError(TimeTrackerError):
    """Error cuando las horas no son válidas"""
    pass


class WorkDay:
    def __init__(self, hours_worked: float, hourly_rate: float):
        self.validate(hours_worked, hourly_rate)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def validate(self, hours, rate):
        if hours < 0 or hours > 24:
            raise InvalidHoursError("Las horas deben estar entre 0 y 24.")
        if rate <= 0:
            raise ValueError("La tarifa debe ser positiva.")