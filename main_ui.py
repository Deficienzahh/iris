import tkinter as tk
from tkinter import messagebox
import webbrowser
import socket
import subprocess
import psutil
import requests

access_code = 'viapcampagna'


def open_premiere_pro():
    try:
        subprocess.Popen([
                             "/Applications/Adobe Premiere Pro 2022/Adobe Premiere Pro 2022.app/Contents/MacOS/Adobe Premiere Pro 2022"])
    except FileNotFoundError:
        messagebox.showerror("Errore", "Adobe Premiere Pro non trovato. Assicurati di aver installato il programma.")


def open_after_effects():
    try:
        subprocess.Popen(
            ["/Applications/Adobe After Effects 2022/Adobe After Effects 2022.app/Contents/MacOS/After Effects"])
    except FileNotFoundError:
        messagebox.showerror("Errore", "Adobe After Effects non trovato. Assicurati di aver installato il programma.")


def open_photoshop():
    try:
        subprocess.Popen(
            ["/Applications/Adobe Photoshop 2022/Adobe Photoshop 2022.app/Contents/MacOS/Adobe Photoshop 2022"])
    except FileNotFoundError:
        messagebox.showerror("Errore", "Adobe Photoshop non trovato. Assicurati di aver installato il programma.")


def open_spotify():
    try:
        subprocess.Popen(["/Applications/Spotify.app/Contents/MacOS/Spotify"])
    except FileNotFoundError:
        messagebox.showerror("Errore", "Spotify non trovato. Assicurati di aver installato il programma.")


def open_discord():
    try:
        subprocess.Popen(["/Applications/Discord.app/Contents/MacOS/Discord"])
    except FileNotFoundError:
        messagebox.showerror("Errore", "Discord non trovato. Assicurati di aver installato il programma.")


def open_telegram():
    try:
        subprocess.Popen(["/Applications/Telegram.localized/Telegram.app/Contents/MacOS/Telegram"])
    except FileNotFoundError:
        messagebox.showerror("Errore", "Telegram non trovato. Assicurati di aver installato il programma.")


def open_whatsapp():
    try:
        subprocess.Popen(["/Applications/WhatsApp.app/Contents/MacOS/WhatsApp"])
    except FileNotFoundError:
        messagebox.showerror("Errore", "WhatsApp non trovato. Assicurati di aver installato il programma.")


def open_browser(url):
    webbrowser.open(url)


def get_weather(city):
    api_key = 'YOUR_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = base_url + 'q=' + city + '&appid=' + api_key

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main_data = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        temperature_celsius = temperature - 273.15
        messagebox.showinfo("Meteo",
                            f"A {city} il tempo è {main_data} ({description}) con una temperatura di {temperature_celsius:.2f}°C")
    else:
        messagebox.showerror("Errore", "Impossibile ottenere informazioni meteo per la città specificata.")


def login():
    access_window = tk.Tk()
    access_window.title("Accesso a IRIS")

    def check_access():
        access_attempt = password_entry.get()
        if access_attempt == access_code:
            access_window.destroy()
            main_window()
        else:
            messagebox.showerror("Errore", "Le credenziali di accesso sono errate, riprova.")

    password_label = tk.Label(access_window, text="IRIS è protetto da una password, inseriscila per continuare:")
    password_label.pack()

    password_entry = tk.Entry(access_window, show="*")
    password_entry.pack()

    login_button = tk.Button(access_window, text="Accedi", command=check_access)
    login_button.pack()

    access_window.mainloop()


def main_window():
    main_window = tk.Tk()
    main_window.title("IRIS")

    def on_task_request():
        task = task_entry.get().lower()

        if 'google' in task:
            open_browser("https://www.google.com")
        elif 'gmail' in task:
            open_browser("https://www.gmail.com")
        # Aggiungi altri task qui...
        elif 'premiere' in task:
            open_premiere_pro()
        elif 'after effect' in task:
            open_after_effects()
        elif 'photoshop' in task:
            open_photoshop()
        elif 'spotify' in task:
            open_spotify()
        elif 'discord' in task:
            open_discord()
        elif 'telegram' in task:
            open_telegram()
        elif 'whatsapp' in task:
            open_whatsapp()
        elif 'meteo' in task:
            city = input("Per quale città vuoi conoscere il meteo?")
            get_weather(city)
        else:
            messagebox.showerror("Errore", "Comando non riconosciuto.")

    task_label = tk.Label(main_window, text="Cosa desideri fare?")
    task_label.pack()

    task_entry = tk.Entry(main_window)
    task_entry.pack()

    task_button = tk.Button(main_window, text="Esegui", command=on_task_request)
    task_button.pack()

    main_window.mainloop()


if __name__ == '__main__':
    login()
