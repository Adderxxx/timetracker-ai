from __future__ import annotations

import csv
import tkinter as tk
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date
from tkinter import filedialog, messagebox, ttk
from typing import List


class TimeTrackerError(Exception):
    pass


class InvalidHoursError(TimeTrackerError):
    pass


class InvalidRateError(TimeTrackerError):
    pass


@dataclass
class WorkDay:
    hours_worked: float
    hourly_rate: float
    date_label: str = field(default_factory=lambda: date.today().isoformat())

    def __post_init__(self) -> None:
        if not (0 < self.hours_worked <= 24):
            raise InvalidHoursError("Horas inválidas")
        if not (0 < self.hourly_rate <= 10000):
            raise InvalidRateError("Tarifa inválida")

    @property
    def overtime_hours(self) -> float:
        return max(0.0, self.hours_worked - 8)

    @property
    def regular_hours(self) -> float:
        return min(self.hours_worked, 8)


class PaymentStrategy(ABC):
    @abstractmethod
    def calculate(self, day: WorkDay) -> float:
        pass


class StandardStrategy(PaymentStrategy):
    def calculate(self, day: WorkDay) -> float:
        return (day.regular_hours * day.hourly_rate) + (
            day.overtime_hours * day.hourly_rate * 1.5
        )


class PayrollService:
    def __init__(self):
        self.strategy = StandardStrategy()

    def process(self, day: WorkDay) -> float:
        return self.strategy.calculate(day)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TimeTracker AI")
        self.geometry("400x300")

        self.service = PayrollService()

        tk.Label(self, text="Horas trabajadas").pack()
        self.hours = tk.Entry(self)
        self.hours.pack()

        tk.Label(self, text="Tarifa por hora").pack()
        self.rate = tk.Entry(self)
        self.rate.pack()

        self.result = tk.Label(self, text="")
        self.result.pack()

        tk.Button(self, text="Calcular", command=self.calculate).pack()

    def calculate(self):
        try:
            h = float(self.hours.get())
            r = float(self.rate.get())
            day = WorkDay(h, r)
            total = self.service.process(day)
            self.result.config(text=f"Total: ${total:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = App()
    app.mainloop()