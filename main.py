import requests
import tkinter as tk
response = requests.get("https://api.covid19api.com/summary")
w = tk.Tk()
w.geometry("800x400")
w.title("Covid Stats")
for i in response.json()["Countries"]:
    if i["Country"] == "Canada":
        print(i)
w.mainloop()
