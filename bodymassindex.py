import tkinter as tk

def hitung_bmi():
    berat = float(entry_berat.get())
    tinggi = float(entry_tinggi.get())
    bmi = berat / (tinggi ** 2)
    label_hasil["text"] = f"BMI Anda adalah: {bmi:.2f}"

def kategori_bmi():
    bmi = float(entry_berat.get()) / (float(entry_tinggi.get()) ** 2)
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Gemuk"
    else:
        return "Obesitas"

def tampilkan_kategori():
    label_kategori["text"] = f"Kategori BMI Anda: {kategori_bmi()}"

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator BMI")

frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=10)

label_berat = tk.Label(frame_input, text="Berat (kg):")
label_berat.grid(row=0, column=0)
entry_berat = tk.Entry(frame_input)
entry_berat.grid(row=0, column=1)

label_tinggi = tk.Label(frame_input, text="Tinggi (m):")
label_tinggi.grid(row=1, column=0)
entry_tinggi = tk.Entry(frame_input)
entry_tinggi.grid(row=1, column=1)

button_hitung = tk.Button(root, text="Hitung BMI", command=lambda: [hitung_bmi(), tampilkan_kategori()])
button_hitung.pack()

label_hasil = tk.Label(root, text="")
label_hasil.pack()

label_kategori = tk.Label(root, text="")
label_kategori.pack()

root.mainloop()
