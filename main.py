import requests
import tkinter as tk

response = requests.get("https://api.covid19api.com/summary")
w = tk.Tk()
w.geometry("800x400")
w.title("Covid Stats")


def show_data(cn):
    try:
        for i in response.json()["Countries"]:
            if i["Country"] == cn:
                cal = tk.Label(w, font="Arial 20", text=cn)
                cal.pack()
                tc = i["TotalConfirmed"]
                tcl = tk.Label(w, text="Total Confirmed Cases: " + str(tc))
                tcl.pack()
                tr = i["TotalRecovered"]
                trl = tk.Label(w, text="Total Recovered Cases: " + str(tr))
                trl.pack()
                nc = i["NewConfirmed"]
                ncl = tk.Label(w, text="New Confirmed Cases: " + str(nc))
                ncl.pack()
                nr = i["TotalRecovered"]
                nrl = tk.Label(w, text="New Recovered Cases: " + str(nr))
                nrl.pack()
    except:
        print("Try again after a few minutes, the json file is up=dating......")
        return "l"


ci = input("Input A Country Name: ")
lol = show_data(ci)
if not lol == "l":
    print("Thank you for your input. Check your taskbar. When you find the window named Covid Stats, \nclick it. if "
          "it is "
          "blank, it means your country name is invalid.")
w.mainloop()
