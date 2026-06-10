import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class ApplicationForm(tk.Tk):
    """Класс для создания графического интерфейса формы заявки."""

    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.title("Форма заявки")
        self.geometry("620x530")
        self.resizable(False, False)
        self.configure(bg="#00a88f")  # Основной бирюзовый цвет рамки

        # Определение цветовой палитры
        self.bg_light_gray = "#f0f0f0"
        self.border_blue = "#6bb5ff"
        self.header_bg = "#00a88f"

        # Списки для хранения путей к файлам и текстовых полей для них
        self.file_entries = []

        # Инициализация интерфейса
        self.create_widgets()

    def create_widgets(self):
        """Создание и размещение всех элементов интерфейса."""

        # 1. Шапка формы
        header_frame = tk.Frame(self, bg=self.header_bg, bd=0)
        header_frame.pack(fill=tk.X, padx=10, pady=(10, 0))  # Исправлено: top=True -> pady

        header_label = tk.Label(
            header_frame,
            text="Форма заявки",
            font=("Arial", 14, "bold"),
            fg="white",
            bg=self.header_bg,
            pady=5,
        )
        header_label.pack()

        # 2. Информационный блок о вложениях
        info_frame = tk.Frame(
            self, bg=self.bg_light_gray, bd=1, relief=tk.SOLID
        )
        info_frame.pack(fill=tk.X, padx=10, pady=(10, 10))  # Исправлено: pady=(0,5)

        info_text = (
            "Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, "
            "odt, xml\n"
            "Макс. размер каждого файла: 1024kb.\n"
            "Макс. общий размер файла: 2048kb."
        )
        info_label = tk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 10),
            justify=tk.LEFT,
            bg=self.bg_light_gray,
            anchor="w",
            padx=10,
            pady=5,
        )
        info_label.pack(fill=tk.X)

        # 3. Основная сетка полей ввода
        main_frame = tk.Frame(self, bg=self.bg_light_gray)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))  # Исправлено: padx=5

        # Настройка весов столбцов для правильного растягивания полей
        main_frame.columnconfigure(0, weight=0)  # Исправлено: weight=0 (для меток)
        main_frame.columnconfigure(1, weight=1)  # Исправлено: weight=1 (для полей ввода)
        main_frame.columnconfigure(2, weight=0)  # Исправлено: weight=0 (для кнопок)

        # --- Строка 0: Ваше имя ---
        self.create_row_label(main_frame, "Ваше имя:", 0, required=True)
        self.entry_name = tk.Entry(main_frame, bd=1, relief=tk.SOLID)
        self.entry_name.grid(
            row=0, column=1, columnspan=2, sticky="ew", padx=5, pady=3, ipady=3
        )

        # --- Строка 1: Ваш Email ---
        self.create_row_label(main_frame, "Ваш Email:", 1, required=True)
        self.entry_email = tk.Entry(main_frame, bd=1, relief=tk.SOLID)
        self.entry_email.grid(
            row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=3, ipady=3
        )

        # --- Строка 2: Тема письма ---
        self.create_row_label(main_frame, "Тема письма:", 2, required=False)  # Исправлено: добавлен параметр required
        self.entry_subject = tk.Entry(main_frame, bd=1, relief=tk.SOLID)
        self.entry_subject.grid(
            row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=3, ipady=3
        )

        # --- Строки 3, 4, 5: Прикрепить файл ---
        for i in range(3):
            row_idx = 3 + i
            self.create_row_label(main_frame, "Прикрепить файл:", row_idx, required=False)  # Исправлено: добавлен параметр

            # Поле вывода пути к файлу
            file_entry = tk.Entry(
                main_frame, bd=1, relief=tk.SOLID, state="readonly"
            )
            file_entry.grid(
                row=row_idx, column=1, sticky="ew", padx=(5, 2), pady=3, ipady=3
            )
            self.file_entries.append(file_entry)

            # Кнопка "Обзор..."
            btn_browse = tk.Button(
                main_frame,
                text="Обзор...",
                font=("Arial", 9),
                bg="#e1e1e1",
                relief=tk.RAISED,
                command=lambda idx=i: self.browse_file(idx),
            )
            btn_browse.grid(
                row=row_idx, column=2, sticky="ew", padx=(2, 5), pady=3
            )

        # --- Строка 6: Ваше сообщение (метка с * над текстовым полем) ---
        # Исправлено: помещаем метку и текстовое поле в правильные позиции
        lbl_msg_frame = tk.Frame(main_frame, bg=self.bg_light_gray)
        lbl_msg_frame.grid(
            row=6, column=0, columnspan=3, sticky="w", padx=5, pady=(5, 2)
        )

        lbl_msg = tk.Label(
            lbl_msg_frame,
            text="Ваше сообщение:",
            font=("Arial", 10),
            bg=self.bg_light_gray,
        )
        lbl_msg.pack(side=tk.LEFT)

        lbl_asterisk = tk.Label(
            lbl_msg_frame, text="*", font=("Arial", 10), fg="red", bg=self.bg_light_gray
        )
        lbl_asterisk.pack(side=tk.LEFT)

        # Текстовое поле для сообщения
        self.text_message = tk.Text(main_frame, bd=1, relief=tk.SOLID, height=8)
        self.text_message.grid(
            row=7, column=0, columnspan=3, sticky="nsew", padx=5, pady=5
        )

        # Настройка расширения для строки с текстовым полем
        main_frame.rowconfigure(7, weight=1)  # Исправлено: добавлена настройка веса строки

        # 4. Нижняя панель с кнопками управления
        bottom_frame = tk.Frame(self, bg=self.header_bg, pady=10)
        bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)

        btn_send = tk.Button(
            bottom_frame,
            text="Отправить Email",
            font=("Arial", 10),
            bg="#e1e1e1",
            padx=10,
            command=self.send_email,
        )
        btn_send.pack(side=tk.LEFT, padx=(170, 10))

        btn_clear = tk.Button(
            bottom_frame,
            text="Очистить",
            font=("Arial", 10),
            bg="#e1e1e1",
            padx=15,
            command=self.clear_form,
        )
        btn_clear.pack(side=tk.LEFT, padx=10)

    def create_row_label(self, parent, text, row, required=False):
        """Вспомогательный метод для создания выровненных текстовых меток."""
        frame = tk.Frame(parent, bg=self.bg_light_gray)
        frame.grid(row=row, column=0, sticky="w", padx=5, pady=3)

        label = tk.Label(
            frame, text=text, font=("Arial", 10), bg=self.bg_light_gray
        )
        label.pack(side=tk.LEFT)

        if required:
            asterisk = tk.Label(
                frame, text="*", font=("Arial", 10), fg="red", bg=self.bg_light_gray
            )
            asterisk.pack(side=tk.LEFT)

    def browse_file(self, index):
        """Логика работы кнопки 'Обзор...' для выбора файла."""
        file_path = filedialog.askopenfilename()
        if file_path:
            # Изменяем состояние поля на normal, чтобы вписать путь, затем возвращаем readonly
            self.file_entries[index].config(state="normal")
            self.file_entries[index].delete(0, tk.END)
            self.file_entries[index].insert(0, file_path)
            self.file_entries[index].config(state="readonly")

    def send_email(self):
        """Валидация обязательных полей и имитация отправки формы."""
        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        message = self.text_message.get("1.0", tk.END).strip()

        if not name or not email or not message:
            messagebox.showwarning(
                "Ошибка заполнения",
                "Пожалуйста, заполните все обязательные поля (*):\n"
                "- Ваше имя\n"
                "- Ваш Email\n"
                "- Ваше сообщение"
            )
        else:
            messagebox.showinfo(
                "Успех", "Форма успешно заполнена и готова к отправке!"
            )

    def clear_form(self):
        """Очистка всех полей формы."""
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_subject.delete(0, tk.END)

        for entry in self.file_entries:
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.config(state="readonly")

        self.text_message.delete("1.0", tk.END)


if __name__ == "__main__":
    app = ApplicationForm()
    app.mainloop()