
import requests
import tkinter as tk
from tkinter import messagebox
import json
import os

def fetch_repo_data():
    repo_name = entry_repo_name.get().strip()
    repo_url = entry_repo_url.get().strip()
    
    if not repo_name or not repo_url:
        messagebox.showerror("Ошибка", "Введите название и URL репозитория.")
        return
    
    try:
        # Преобразуем URL в API URL
        api_url = repo_url.replace("https://github.com/", "https://api.github.com/repos/")
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            # Извлекаем нужные данные
            result = {
                "company": data.get("owner", {}).get("company", None),
                "created_at": data.get("created_at", None),
                "email": data.get("owner", {}).get("email", None),
                "id": data.get("id", None),
                "name": data.get("name", None),
                "url": data.get("owner", {}).get("url", None)
            }
            
            # Определяем путь для сохранения файла
            file_name = f"{repo_name}.json"
            file_path = os.path.join(os.getcwd(), file_name)
            
            # Сохраняем в JSON файл
            with open(file_path, "w") as f:
                json.dump(result, f, indent=4)
            
            messagebox.showinfo("Успех", f"Данные успешно сохранены в файл: {file_path}")
        else:
            messagebox.showerror("Ошибка", f"Не удалось получить данные. Код ответа: {response.status_code}")
    
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Создаем интерфейс
root = tk.Tk()
root.title("GitHub Repo Data Fetcher")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Поле для ввода имени репозитория
tk.Label(frame, text="Введите название репозитория:").grid(row=0, column=0, sticky="w")
entry_repo_name = tk.Entry(frame, width=50)
entry_repo_name.grid(row=0, column=1, pady=5)

# Поле для ввода ссылки на репозиторий
tk.Label(frame, text="Введите ссылку на репозиторий:").grid(row=1, column=0, sticky="w")
entry_repo_url = tk.Entry(frame, width=50)
entry_repo_url.grid(row=1, column=1, pady=5)

# Кнопка для выполнения
fetch_button = tk.Button(frame, text="Получить данные", command=fetch_repo_data)
fetch_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()
