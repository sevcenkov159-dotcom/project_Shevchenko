import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Sign Up Form")
root.geometry("600x750")
root.resizable(False, False)

gender_var = IntVar(value=1)
agree_var = IntVar(value=0)


def close_window():
    root.destroy()


def submit_form():
    if agree_var.get() == 0:
        messagebox.showwarning(
            "Внимание", "Вы должны согласиться с Условиями использования!"
        )
        return

    f_name = entry_fn.get()
    if f_name == "Enter First Name...":
        f_name = ""

    l_name = entry_ln.get()
    if l_name == "Enter Last Name...":
        l_name = ""

    s_name = entry_sn.get()
    if s_name == "Enter Screen Name...":
        s_name = ""

    email = entry_em.get()
    if email == "Enter E-mail......":
        email = ""

    phone = entry_ph.get()
    if phone == "Enter Phone......":
        phone = ""

    password = entry_pass.get()
    confirm_password = entry_cpass.get()

    dob = f"{day_combo.get()} {month_combo.get()} {year_combo.get()}"
    gender = "Male" if gender_var.get() == 1 else "Female"
    country = country_combo.get()

    log_file = "data.txt"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("--- Данные пользователя ---\n")
        f.write(f"First Name: {f_name}\n")
        f.write(f"Last Name: {l_name}\n")
        f.write(f"Screen Name: {s_name}\n")
        f.write(f"Date of Birth: {dob}\n")
        f.write(f"Gender: {gender}\n")
        f.write(f"Country: {country}\n")
        f.write(f"E-mail: {email}\n")
        f.write(f"Phone: {phone}\n")
        f.write(f"Password: {password}\n")
        f.write("---------------------------\n\n")

    messagebox.showinfo("Успех", "Анкета успешно добавлена в документ.")


def fn_in(event):
    if entry_fn.get() == "Enter First Name...":
        entry_fn.delete(0, END)
        entry_fn.configure(fg="black")


def fn_out(event):
    if entry_fn.get() == "":
        entry_fn.insert(0, "Enter First Name...")
        entry_fn.configure(fg="gray")


def ln_in(event):
    if entry_ln.get() == "Enter Last Name...":
        entry_ln.delete(0, END)
        entry_ln.configure(fg="black")


def ln_out(event):
    if entry_ln.get() == "":
        entry_ln.insert(0, "Enter Last Name...")
        entry_ln.configure(fg="gray")


def sn_in(event):
    if entry_sn.get() == "Enter Screen Name...":
        entry_sn.delete(0, END)
        entry_sn.configure(fg="black")


def sn_out(event):
    if entry_sn.get() == "":
        entry_sn.insert(0, "Enter Screen Name...")
        entry_sn.configure(fg="gray")


def em_in(event):
    if entry_em.get() == "Enter E-mail......":
        entry_em.delete(0, END)
        entry_em.configure(fg="black")


def em_out(event):
    if entry_em.get() == "":
        entry_em.insert(0, "Enter E-mail......")
        entry_em.configure(fg="gray")


def ph_in(event):
    if entry_ph.get() == "Enter Phone......":
        entry_ph.delete(0, END)
        entry_ph.configure(fg="black")


def ph_out(event):
    if entry_ph.get() == "":
        entry_ph.insert(0, "Enter Phone......")
        entry_ph.configure(fg="gray")


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=12)
root.rowconfigure(2, weight=1)

frame1 = Frame(
    root, bg="#e67e22", highlightbackground="white", highlightthickness=1
)
frame1.grid(row=0, column=0, sticky="nsew")

lbl_title = Label(
    frame1, text="Sign Up", fg="white", bg="#e67e22", font=("Arial", 16, "bold")
)
lbl_title.pack(side="left", padx=20, pady=10)

frame2 = Frame(
    root, bg="#1e2238", highlightbackground="white", highlightthickness=1
)
frame2.grid(row=1, column=0, sticky="nsew")
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=2)

lbl_fn = Label(
    frame2, text="First Name", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_fn.grid(row=0, column=0, sticky="e", padx=20, pady=10)
entry_fn = Entry(frame2, bg="white", fg="gray", font=("Arial", 11), relief="flat")
entry_fn.insert(0, "Enter First Name...")
entry_fn.grid(row=0, column=1, sticky="we", padx=(0, 40), pady=10)
entry_fn.bind("<FocusIn>", fn_in)
entry_fn.bind("<FocusOut>", fn_out)

lbl_ln = Label(
    frame2, text="Last Name", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_ln.grid(row=1, column=0, sticky="e", padx=20, pady=10)
entry_ln = Entry(frame2, bg="white", fg="gray", font=("Arial", 11), relief="flat")
entry_ln.insert(0, "Enter Last Name...")
entry_ln.grid(row=1, column=1, sticky="we", padx=(0, 40), pady=10)
entry_ln.bind("<FocusIn>", ln_in)
entry_ln.bind("<FocusOut>", ln_out)

lbl_sn = Label(
    frame2, text="Screen Name", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_sn.grid(row=2, column=0, sticky="e", padx=20, pady=10)
entry_sn = Entry(frame2, bg="white", fg="gray", font=("Arial", 11), relief="flat")
entry_sn.insert(0, "Enter Screen Name...")
entry_sn.grid(row=2, column=1, sticky="we", padx=(0, 40), pady=10)
entry_sn.bind("<FocusIn>", sn_in)
entry_sn.bind("<FocusOut>", sn_out)

lbl_dob = Label(
    frame2, text="Date of Birth", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_dob.grid(row=3, column=0, sticky="e", padx=20, pady=10)

dob_container = Frame(frame2, bg="#1e2238")
dob_container.grid(row=3, column=1, sticky="w", pady=10)

month_combo = ttk.Combobox(
    dob_container,
    values=[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
    width=10,
)
month_combo.set("May")
month_combo.pack(side="left", padx=(0, 10))

day_combo = ttk.Combobox(
    dob_container, values=[str(i) for i in range(1, 32)], width=5
)
day_combo.set("5")
day_combo.pack(side="left", padx=10)

year_combo = ttk.Combobox(
    dob_container, values=[str(i) for i in range(1980, 2026)], width=8
)
year_combo.set("1985")
year_combo.pack(side="left", padx=10)

lbl_gender = Label(
    frame2, text="Gender", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_gender.grid(row=4, column=0, sticky="e", padx=20, pady=10)

gender_container = Frame(frame2, bg="#1e2238")
gender_container.grid(row=4, column=1, sticky="w", pady=10)

rb_male = Radiobutton(
    gender_container,
    text="Male",
    variable=gender_var,
    value=1,
    fg="#ffd700",
    bg="#1e2238",
    selectcolor="#1e2238",
    activebackground="#1e2238",
)
rb_male.pack(side="left", padx=(0, 20))
rb_female = Radiobutton(
    gender_container,
    text="Female",
    variable=gender_var,
    value=2,
    fg="#ffd700",
    bg="#1e2238",
    selectcolor="#1e2238",
    activebackground="#1e2238",
)
rb_female.pack(side="left")

lbl_country = Label(
    frame2, text="Country", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_country.grid(row=5, column=0, sticky="e", padx=20, pady=10)
country_combo = ttk.Combobox(
    frame2,
    values=[
        "USA",
        "China",
        "Japan",
        "Albania",
        "Andorra",
        "Austria",
        "Belarus",
        "Belgium",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Iceland",
        "Ireland",
        "Italy",
        "Latvia",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Malta",
        "Moldova",
        "Monaco",
        "Montenegro",
        "Netherlands",
        "North Macedonia",
        "Norway",
        "Poland",
        "Portugal",
        "Romania",
        "Russia",
        "San Marino",
        "Serbia",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden",
        "Switzerland",
        "Ukraine",
        "United Kingdom",
        "Vatican City",
    ],
    font=("Arial", 11),
)
country_combo.set("USA")
country_combo.grid(row=5, column=1, sticky="we", padx=(0, 40), pady=10)

lbl_em = Label(
    frame2, text="E-mail", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_em.grid(row=6, column=0, sticky="e", padx=20, pady=10)
entry_em = Entry(frame2, bg="white", fg="gray", font=("Arial", 11), relief="flat")
entry_em.insert(0, "Enter E-mail......")
entry_em.grid(row=6, column=1, sticky="we", padx=(0, 40), pady=10)
entry_em.bind("<FocusIn>", em_in)
entry_em.bind("<FocusOut>", em_out)

lbl_ph = Label(
    frame2, text="Phone", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_ph.grid(row=7, column=0, sticky="e", padx=20, pady=10)
entry_ph = Entry(frame2, bg="white", fg="gray", font=("Arial", 11), relief="flat")
entry_ph.insert(0, "Enter Phone......")
entry_ph.grid(row=7, column=1, sticky="we", padx=(0, 40), pady=10)
entry_ph.bind("<FocusIn>", ph_in)
entry_ph.bind("<FocusOut>", ph_out)

lbl_pass = Label(
    frame2, text="Password", fg="#ffd700", bg="#1e2238", font=("Arial", 11)
)
lbl_pass.grid(row=8, column=0, sticky="e", padx=20, pady=10)
entry_pass = Entry(
    frame2, bg="white", fg="black", font=("Arial", 11), relief="flat", show="*"
)
entry_pass.grid(row=8, column=1, sticky="we", padx=(0, 40), pady=10)

lbl_cpass = Label(
    frame2,
    text="Confirm Password",
    fg="#ffd700",
    bg="#1e2238",
    font=("Arial", 11),
)
lbl_cpass.grid(row=9, column=0, sticky="e", padx=20, pady=10)
entry_cpass = Entry(
    frame2, bg="white", fg="black", font=("Arial", 11), relief="flat", show="*"
)
entry_cpass.grid(row=9, column=1, sticky="we", padx=(0, 40), pady=10)

chk_agree = Checkbutton(
    frame2,
    text="I agree to the Terms of Use",
    variable=agree_var,
    fg="#ffd700",
    bg="#1e2238",
    selectcolor="#1e2238",
    activebackground="#1e2238",
    font=("Arial", 10, "bold"),
)
chk_agree.grid(row=10, column=0, columnspan=2, pady=20)

frame3 = Frame(
    root, bg="#e67e22", highlightbackground="white", highlightthickness=1
)
frame3.grid(row=2, column=0, sticky="nsew")

btn_submit = Button(frame3,text="submit",bg="#2ecc71",fg="white",font=("Arial", 10, "bold"),relief="flat",width=10,command=submit_form,)
btn_submit.pack(side="right", padx=10, pady=10)
btn_cancel = Button(frame3,text="Cancel",bg="#e74c3c",fg="white",font=("Arial", 10, "bold"),relief="flat",width=10,command=close_window,)
btn_cancel.pack(side="right", padx=10, pady=10)

root.mainloop()