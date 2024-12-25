import tkinter as tk
import requests

def fdata():
    id_value = id_entry.get()
    if not id_value.isdigit():
        result_label.config(text="Введите корректный ID!")
        return
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_value}")
    if response.status_code == 200:
        data = response.json()
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, data)
        result_label.config(text="Данные получены!")
    else:
        result_label.config(text="Данные не найдены.")

def save_data():
    data = result_text.get("1.0", tk.END).strip()
    if not data:
        result_label.config(text="Нечего сохранять!")
        return
    with open("result.json", "w", encoding="utf-8") as file:
        file.write(data)
    result_label.config(text="Данные сохранены в result.json!")

root = tk.Tk()
root.title("JSON Viewer")
root.geometry("400x400")

tk.Label(root, text="Введите ID:").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Button(root, text="Получить данные", command=fdata).pack()

result_text = tk.Text(root, height=15, width=50)
result_text.pack()

tk.Button(root, text="Сохранить в файл", command=save_data).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()