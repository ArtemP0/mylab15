import tkinter as tk
import json

def save_data():
    workers = {}
    while True:
        name = input("Введіть ім'я робітника або 'ext: ")
        if name.lower() == 'exit':
            break
        try:
            sick_leave_count = int(input(f"Скільки лікарняних було у {name} за місяць? "))
            workers[name] = sick_leave_count
        except ValueError:
            print("Будь ласка, введіть число для лікарняних.")    
    with open("workers.json", "w") as file:
        json.dump(workers, file, indent=4)
    workers_text = ""
    for name, sick_leave in workers.items():
        workers_text += f"{name}: {sick_leave} лікарняних\n"
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, workers_text)
window = tk.Tk()
window.title("Дані про лікарняні робітників")
window.geometry("300x220")
window.config(bg="green")
button = tk.Button(window, text="Ввести дані", command=save_data)
button.pack(pady=10)
text_widget = tk.Text(window, width=30, height=10)
text_widget.pack(pady=10)
window.mainloop()
