import tkinter as tk

def find_divisors():
        number = int(entry_number.get())
        if number <= 0:
            result_entry.insert(0, "Введіть додатне число!")
            return
        divisors = ""
        for i in range(1, number + 1):
            if number % i == 0:
                divisors += str(i) + ", "
        result_entry.insert(0, divisors.rstrip(", "))
window = tk.Tk()
label = tk.Label(window, text="Введіть число:", fg='black', bg='white', width=20)
label.pack()
entry_number = tk.Entry(window, fg='black', bg='white', width=20)
entry_number.pack()
result_entry = tk.Entry(window, fg='black', bg='white', width=80)
result_entry.pack()
button = tk.Button(window, text="Знайти дільники", width=10, height=1, background="blue", foreground="yellow", command=find_divisors)
button.pack()
window.mainloop()
