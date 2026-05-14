import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(1.0)


class Ritual(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("R I T U A L K A")
        self.geometry("600x900")
        self.resizable(False, False)

        self.label_title = ctk.CTkLabel(
            self,
            text="🕯 РАСЧЕТ УСЛУГ",
            font=("Arial", 24, "bold"),
            text_color="#3a7ebf",
        )
        self.label_title.pack(pady=15)

        self.loc_frame = ctk.CTkFrame(self, corner_radius=15)
        self.loc_frame.pack(pady=10, padx=30, fill="x")

        self.location_var = ctk.StringVar(value="г")
        self.rb_city = ctk.CTkRadioButton(
            self.loc_frame,
            text="Город",
            variable=self.location_var,
            value="г",
            font=("Arial", 14),
        )
        self.rb_city.pack(side="left", padx=50, pady=15)
        self.rb_district = ctk.CTkRadioButton(
            self.loc_frame,
            text="Район",
            variable=self.location_var,
            value="р",
            font=("Arial", 14),
        )
        self.rb_district.pack(side="left", padx=10, pady=15)

        self.input_frame = ctk.CTkFrame(self, corner_radius=15)
        self.input_frame.pack(pady=10, padx=30, fill="both", expand=True)

        def create_entry(parent, placeholder):
            entry = ctk.CTkEntry(
                parent,
                placeholder_text=placeholder,
                width=250,
                height=35,
                border_width=1,
            )
            entry.pack(pady=6)
            return entry

        self.entry_catafalk = create_entry(self.input_frame, "Катафалк")
        self.entry_preparation = create_entry(
            self.input_frame, "🧼 Подготовка умершего"
        )
        self.entry_delivery_d = create_entry(self.input_frame, "Доставка умершего")
        self.entry_delivery_g = create_entry(self.input_frame, "Доставка товаров")
        self.entry_takeaway = create_entry(self.input_frame, "Бригада на вынос")
        self.entry_digging = create_entry(self.input_frame, "Копка могилы")
        self.entry_bury = create_entry(self.input_frame, "⚰ Закопка")

        ctk.CTkLabel(
            self.input_frame, text="Удаленность (если район):", font=("Arial", 12)
        ).pack(pady=(10, 0))
        self.act_option = ctk.CTkOptionMenu(
            self.input_frame, values=["До 20 км", "До 50 км", "До 100 км"], width=250
        )
        self.act_option.pack(pady=10)

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=10)

        self.btn_calc = ctk.CTkButton(
            self.btn_frame,
            text="РАССЧИТАТЬ",
            command=self.calculate,
            width=180,
            height=45,
            font=("Arial", 14, "bold"),
            fg_color="#2d8a4e",
            hover_color="#1e5c34",
        )
        self.btn_calc.grid(row=0, column=0, padx=10)

        self.btn_clear = ctk.CTkButton(
            self.btn_frame,
            text="ОЧИСТИТЬ",
            command=self.clear_fields,
            width=120,
            height=45,
            font=("Arial", 14),
            fg_color="#a13d3d",
            hover_color="#7a2e2e",
        )
        self.btn_clear.grid(row=0, column=1, padx=10)

        self.result_text = ctk.CTkTextbox(
            self,
            width=540,
            height=180,
            corner_radius=15,
            border_width=2,
            border_color="#3a7ebf",
            font=("Courier New", 13),
        )
        self.result_text.pack(pady=15, padx=30)
        self.result_text.insert("0.0", "Итоговая стоимость будет отображена здесь")

    def clear_fields(self):
        entries = [
            self.entry_catafalk,
            self.entry_preparation,
            self.entry_delivery_d,
            self.entry_delivery_g,
            self.entry_takeaway,
            self.entry_digging,
            self.entry_bury,
        ]
        for e in entries:
            e.delete(0, "end")
        self.result_text.delete("0.0", "end")
        self.result_text.insert("0.0", "Поля очищены.")

    def save_to_file(self, content):
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(
                f"\n--- Расчет от {datetime.now().strftime('%Y-%m-%d %H:%M')} ---\n"
            )
            f.write(content + "\n")

    def calculate(self):
        try:

            vals = {
                "Катафалк": self.entry_catafalk.get(),
                "Подготовка": self.entry_preparation.get(),
                "Доставка у": self.entry_delivery_d.get(),
                "Доставка т": self.entry_delivery_g.get(),
                "Вынос": self.entry_takeaway.get(),
                "Копка": self.entry_digging.get(),
                "Закопка": self.entry_bury.get(),
            }

            nums = {k: float(v if v else 0) for k, v in vals.items()}
            base_sum = sum(nums.values())

            location = self.location_var.get()
            act_level = self.act_option.get()
            multipliers = {"До 20 км": 1.2, "До 50 км": 1.55, "До 100 км": 1.725}
            k = multipliers[act_level]

            if location == "г":
                final_price = base_sum
                loc_name = "Город"
            else:
                final_price = base_sum * k
                loc_name = f"Район ({act_level})"

            res_str = f"ИТОГО: {round(final_price, 2)} BYN\n"
            res_str += f"Тип: {loc_name}\n"
            res_str += "-" * 30 + "\n"
            for k, v in nums.items():
                if v > 0:
                    res_str += f"{k}: {v} BYN\n"

            if location == "р":
                res_str += f"Применен коэфф.: {k}\n"

            self.result_text.delete("0.0", "end")
            self.result_text.insert("0.0", res_str)

            self.save_to_file(res_str)

        except ValueError:
            self.result_text.delete("0.0", "end")
            self.result_text.insert("0.0", "❌ Ошибка: Вводите только цифры!")


if __name__ == "__main__":
    app = Ritual()
    app.mainloop()
