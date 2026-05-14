import tkinter as ttk


def calculation():
    try:
        distance = float(entry_distance.get())
        consumption = float(consumption_per_km.get())
        price = float(price_per_liter.get())
        amount = consumption / 100 * distance
        full_cost = amount * price
        result_label.config(
            text=f"Понадобится: {amount:.2f} л.\nСтоимость: {full_cost:.2f} руб.",
            fg="green",
        )
    except ValueError:
        result_label.config(text="Не валидное значение", fg="red")


calc = ttk.Tk()
calc.geometry("400x400")
calc.title("Calculator")


ttk.Label(calc, text="Расстояние км:").pack()
entry_distance = ttk.Entry(calc)
entry_distance.pack(pady=5)

ttk.Label(calc, text="Расход топлива на 100км:").pack()
consumption_per_km = ttk.Entry(calc)
consumption_per_km.pack(pady=5)

ttk.Label(calc, text="Цена за 1 литр").pack()
price_per_liter = ttk.Entry(calc)
price_per_liter.pack(pady=5)

ttk.Button(calc, text="Рассчитать", command=calculation).pack()

result_label = ttk.Label(calc, text="")
result_label.pack()


calc.mainloop()
