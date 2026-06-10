import tkinter as tk
from tkinter import ttk


def submit_form():
    pass


root = tk.Tk()
root.title("All Fields Form")
root.geometry("600x850")
root.configure(bg="white")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="white", font=("Arial", 11))
style.configure("TEntry", fieldbackground="white")
style.configure("TRadiobutton", background="white", font=("Arial", 10))
style.configure("TCheckbutton", background="white", font=("Arial", 10))

main_frame = tk.Frame(root, bg="white", padx=40, pady=20)
main_frame.pack(fill="both", expand=True)

title_label = tk.Label(
    main_frame,
    text="ALL FIELDS FORM",
    font=("Arial", 16, "bold"),
    fg="#2c6cb0",
    bg="white",
)
title_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 20))


def create_label(text, row):
    lbl = ttk.Label(main_frame, text=text)
    lbl.grid(row=row, column=0, sticky="nw", pady=10, padx=(0, 20))
    return lbl


create_label("Textfield", 1)
entry_text = ttk.Entry(main_frame, width=50)
entry_text.grid(row=1, column=1, sticky="w", pady=10)

create_label("Textarea", 2)
textarea = tk.Text(
    main_frame,
    width=50,
    height=6,
    bd=1,
    relief="solid",
    highlightthickness=1,
    highlightbackground="#ccc",
)
textarea.grid(row=2, column=1, sticky="w", pady=10)

create_label("Email Address", 3)
entry_email = ttk.Entry(main_frame, width=50)
entry_email.grid(row=3, column=1, sticky="w", pady=10)

create_label("Dropdown", 4)
combo_var = tk.StringVar(value="Option 1")
dropdown = ttk.Combobox(
    main_frame, textvariable=combo_var, values=["Option 1", "Option 2"], width=25
)
dropdown.grid(row=4, column=1, sticky="w", pady=10)

create_label("Radio Button", 5)
radio_frame = tk.Frame(main_frame, bg="white")
radio_frame.grid(row=5, column=1, sticky="w", pady=10)

radio_var = tk.StringVar(value="Option 1")
r1 = ttk.Radiobutton(
    radio_frame, text="Option 1", variable=radio_var, value="Option 1"
)
r2 = ttk.Radiobutton(
    radio_frame, text="Option 2", variable=radio_var, value="Option 2"
)
r1.pack(anchor="w", pady=2)
r2.pack(anchor="w", pady=2)

create_label("Checkbox", 6)
check_frame = tk.Frame(main_frame, bg="white")
check_frame.grid(row=6, column=1, sticky="w", pady=10)

ch_var1 = tk.BooleanVar()
ch_var2 = tk.BooleanVar()
ch_var3 = tk.BooleanVar()

c1 = ttk.Checkbutton(check_frame, text="Option 1", variable=ch_var1)
c2 = ttk.Checkbutton(check_frame, text="Option 2", variable=ch_var2)
c3 = ttk.Checkbutton(check_frame, text="Option 3", variable=ch_var3)
c1.pack(anchor="w", pady=2)
c2.pack(anchor="w", pady=2)
c3.pack(anchor="w", pady=2)

create_label("Password", 7)
entry_password = tk.Entry(
    main_frame,
    width=50,
    show="•",
    bg="#ffffcc",
    bd=1,
    relief="solid",
    highlightthickness=1,
    highlightbackground="#ccc",
)
entry_password.insert(0, "password123")
entry_password.grid(row=7, column=1, sticky="w", pady=10)

create_label("Number Field", 8)
entry_number = ttk.Entry(main_frame, width=25)
entry_number.grid(row=8, column=1, sticky="w", pady=10)

create_label("Mathematical\nCaptcha", 9)
captcha_frame = tk.Frame(main_frame, bg="white")
captcha_frame.grid(row=9, column=1, sticky="w", pady=10)

lbl_math = ttk.Label(captcha_frame, text="6 + 8 = ")
lbl_math.pack(side="left")
entry_captcha = tk.Entry(
    captcha_frame,
    width=20,
    bd=1,
    relief="solid",
    fg="#888",
    highlightthickness=1,
    highlightbackground="#ccc",
)
entry_captcha.insert(0, "Enter Sum")
entry_captcha.pack(side="left", padx=5)

create_label("Google Captcha", 10)
g_captcha_frame = tk.Frame(
    main_frame, bg="#f9f9f9", bd=1, relief="solid", padx=15, pady=10
)
g_captcha_frame.grid(row=10, column=1, sticky="w", pady=10)

recaptcha_var = tk.BooleanVar()
ch_recaptcha = ttk.Checkbutton(
    g_captcha_frame, text="I'm not a robot", variable=recaptcha_var
)
ch_recaptcha.pack(side="left")

lbl_logo = tk.Label(
    g_captcha_frame,
    text="♻\nreCAPTCHA\nPrivacy - Terms",
    font=("Arial", 7),
    bg="#f9f9f9",
    fg="#555",
    justify="center",
)
lbl_logo.pack(side="right", padx=(40, 0))

submit_btn = tk.Button(
    main_frame,
    text="Submit",
    bg="#63b3ed",
    fg="white",
    font=("Arial", 11, "bold"),
    bd=0,
    padx=20,
    pady=8,
    activebackground="#4299e1",
    activeforeground="white",
    command=submit_form,
)
submit_btn.grid(row=11, column=1, sticky="w", pady=20)

root.mainloop()
