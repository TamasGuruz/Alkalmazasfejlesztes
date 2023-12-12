import tkinter as tk
from tkinter import messagebox

egesho = 35.11
valtoszam = 3.2419

def atvalt_m3():
    try:
        adat = float(adat_entry.get())
        eredmeny_MJ = adat * egesho
        eredmeny_kWh = eredmeny_MJ * valtoszam
        eredmeny_GJ = eredmeny_MJ / 1000
        eredmeny_MWh = eredmeny_kWh / 1000

        messagebox.showinfo("Átváltás eredménye",
                            f"{adat} m3 = {eredmeny_MJ:.2f} MJ\n"
                            f"{adat} m3 = {eredmeny_kWh:.2f} kWh\n"
                            f"{adat} m3 = {eredmeny_GJ:.2f} GJ\n"
                            f"{adat} m3 = {eredmeny_MWh:.2f} MWh")
    except ValueError:
        messagebox.showerror("Hiba", "Érvénytelen adat!")

def atvalt_MJ():
    try:
        adat = float(adat_entry.get())
        eredmeny_m3 = adat / egesho
        eredmeny_kWh = adat * valtoszam
        eredmeny_GJ = adat / 1000
        eredmeny_MWh = eredmeny_kWh / 1000

        messagebox.showinfo("Átváltás eredménye",
                            f"{adat} MJ = {eredmeny_m3:.2f} m3\n"
                            f"{adat} MJ = {eredmeny_kWh:.2f} kWh\n"
                            f"{adat} MJ = {eredmeny_GJ:.2f} GJ\n"
                            f"{adat} MJ = {eredmeny_MWh:.2f} MWh")
    except ValueError:
        messagebox.showerror("Hiba", "Érvénytelen adat!")

def atvalt_GJ():
    try:
        adat = float(adat_entry.get())
        eredmeny_m3 = adat * 1000 / egesho
        eredmeny_MJ = adat * 1000
        eredmeny_kWh = eredmeny_MJ * valtoszam
        eredmeny_MWh = eredmeny_kWh / 1000

        messagebox.showinfo("Átváltás eredménye",
                            f"{adat} GJ = {eredmeny_m3:.2f} m3\n"
                            f"{adat} GJ = {eredmeny_kWh:.2f} kWh\n"
                            f"{adat} GJ = {eredmeny_MJ:.2f} MJ\n"
                            f"{adat} GJ = {eredmeny_MWh:.2f} MWh")
    except ValueError:
        messagebox.showerror("Hiba", "Érvénytelen adat!")

def atvalt_kWh():
    try:
        adat = float(adat_entry.get())
        eredmeny_MJ = adat / valtoszam
        eredmeny_m3 = eredmeny_MJ / egesho
        eredmeny_GJ = eredmeny_MJ / 1000
        eredmeny_MWh = adat / 1000

        messagebox.showinfo("Átváltás eredménye",
                            f"{adat} kWh = {eredmeny_m3:.2f} m3\n"
                            f"{adat} kWh = {eredmeny_MJ:.2f} MJ\n"
                            f"{adat} kWh = {eredmeny_GJ:.2f} GJ\n"
                            f"{adat} kWh = {eredmeny_MWh:.2f} MWh")
    except ValueError:
        messagebox.showerror("Hiba", "Érvénytelen adat!")

def atvalt_MWh():
    try:
        adat = float(adat_entry.get())
        eredmeny_MJ = adat * 1000 / valtoszam
        eredmeny_m3 = eredmeny_MJ / egesho
        eredmeny_kWh = eredmeny_MJ * valtoszam
        eredmeny_GJ = eredmeny_MJ / 1000

        messagebox.showinfo("Átváltás eredménye",
                            f"{adat} MWh = {eredmeny_m3:.2f} m3\n"
                            f"{adat} MWh = {eredmeny_kWh:.2f} kWh\n"
                            f"{adat} MWh = {eredmeny_MJ} MJ\n"
                            f"{adat} MWh = {eredmeny_GJ:.2f} GJ")
    except ValueError:
        messagebox.showerror("Hiba", "Érvénytelen adat!")

ablak = tk.Tk()
ablak.title("ÁTVÁLTÓ")
ablak.geometry("400x200")

adat_label = tk.Label(ablak, text="Adja meg a mennyiséget:")
adat_label.pack(padx=10, pady=10)

adat_entry = tk.Entry(ablak)
adat_entry.pack(padx=10, pady=10)
adat_entry.focus()

me_label = tk.Label(ablak, text="Válasszon mértékegységet:")
me_label.pack(padx=10, pady=10)

gombok_frame = tk.Frame(ablak)
gombok_frame.pack()

m3_gomb = tk.Button(gombok_frame, text="m3", command=atvalt_m3, width=4, height=1)
m3_gomb.pack(side="left", padx=10, pady=5)
m3_gomb.configure(bg="lightblue")

MJ_gomb = tk.Button(gombok_frame, text="MJ", command=atvalt_MJ, width=4, height=1)
MJ_gomb.pack(side="left", padx=10, pady=5)
MJ_gomb.configure(bg="lightblue")

GJ_gomb = tk.Button(gombok_frame, text="GJ", command=atvalt_GJ, width=4, height=1)
GJ_gomb.pack(side="left", padx=10, pady=5)
GJ_gomb.configure(bg="lightblue")

kWh_gomb = tk.Button(gombok_frame, text="kWh", command=atvalt_kWh, width=4, height=1)
kWh_gomb.pack(side="left", padx=10, pady=5)
kWh_gomb.configure(bg="lightblue")

MWh_gomb = tk.Button(gombok_frame, text="MWh", command=atvalt_MWh, width=4, height=1)
MWh_gomb.pack(side="left", padx=10, pady=5)
MWh_gomb.configure(bg="lightblue")

ablak.mainloop()
