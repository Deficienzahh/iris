import webbrowser
import socket
import subprocess
import keyboard
import time
from pynput.keyboard import Key, Controller
import psutil
import secrets
import string
import datetime
import requests
import json
import os
KeyBoard = Controller()


#json file
script_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(script_dir, 'config.json')
with open('config.json') as config_file:
    config_data = json.load(config_file)
    access_code = config_data['access_code']
    weather_api_key = config_data['weather_api_key']
    psw_def_length = config_data['psw_def_length']

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and  hour <= 12:
        print('Buongiorno signore')
    elif hour >= 12 and  hour <= 18:
        print('Buonpomeriggio signore')
    elif hour >= 18 and  hour <= 24:
        print('Buonasera signore')
    else:
        print('Buonanotte signore')
# Hotkeys
def new_tab():
    with KeyBoard.pressed(Key.cmd):
        KeyBoard.press('t')
        KeyBoard.release('t')


def new_window():
    with KeyBoard.pressed(Key.cmd):
        KeyBoard.press('n')
        KeyBoard.release('n')


def hide_window():
    with KeyBoard.pressed(Key.cmd):
        KeyBoard.press('m')
        KeyBoard.release('m')

#Basic function
def screenshot():
    with KeyBoard.pressed(Key.cmd, Key.shift):
        KeyBoard.press('5')
        KeyBoard.release('5')

def date():
    day = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)
    print("Oggi è il "+day+"/"+month+"/"+year)

def orario():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Sono le "+time)


def Iris_modules(query):
    # Website saved
    if 'google' in query.lower():
        webbrowser.open("https://www.google.com")
    elif 'gmail' in query.lower():
        webbrowser.open("https://www.gmail.com")
    elif 'reddit'in query.lower():
        webbrowser.open("https://www.reddit.com")
    elif 'soundcloud' in query.lower():
        webbrowser.open("https://www.soundcloud.com/discover")
    elif 'twitter' in query.lower():
        webbrowser.open("https://www.twitter.com/home")
    elif 'traduttore' in query.lower():
        webbrowser.open("https://translate.google.com")
    elif 'gemini' in query.lower():
        webbrowser.open("https://gemini.google.com/app")
    elif 'cmacked' in query.lower():
        webbrowser.open("https://cmacked.com/page/2/")
    elif 'youtube' in query.lower() or 'yt' in query.lower():
        webbrowser.open("https://www.youtube.com")
    elif 'instagram' in query.lower() or 'ig' in query.lower():
        webbrowser.open("https://www.instagram.com")
    elif 'github' in query.lower():
        webbrowser.open("https://www.github.com")
    elif 'drive' in query.lower():
        webbrowser.open("https://www.drive.google.com")
    elif 'soundcloud' in query.lower():
        webbrowser.open("https://www.soundcloud.com")
    elif 'amazon' in query.lower():
        webbrowser.open("https://www.amazon.it")
    elif 'twitch' in query.lower():
        webbrowser.open("https://www.twich.tv")
    # App
    elif 'premiere' in query.lower():
        subprocess.Popen([
            "/Applications/Adobe Premiere Pro 2022/Adobe Premiere Pro 2022.app/Contents/MacOS/Adobe Premiere Pro 2022"])
    elif 'after effect' in query.lower():
        subprocess.Popen(
            ["/Applications/Adobe After Effects 2022/Adobe After Effects 2022.app/Contents/MacOS/After Effects"])
    elif 'photoshop' in query.lower():
        subprocess.Popen(
            ["/Applications/Adobe Photoshop 2022/Adobe Photoshop 2022.app/Contents/MacOS/Adobe Photoshop 2022"])
    elif 'spotify' in query.lower():
        subprocess.Popen(["/Applications/Spotify.app/Contents/MacOS/Spotify"])
    elif 'discord' in query.lower():
        subprocess.Popen(["/Applications/Discord.app/Contents/MacOS/Discord"])
    elif 'telegram' in query.lower():
        subprocess.Popen(["/Applications/Telegram.localized/Telegram.app/Contents/MacOS/Telegram"])
    elif 'whatsapp' in query.lower():
        subprocess.Popen(["/Applications/WhatsApp.app/Contents/MacOS/WhatsApp"])
    # Other internet function
    elif 'IP' in query.lower():
        print("Sto ottenendo le diagnostiche di rete")
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("Host:", hostname)
        print("Indirizzo IP:", ip)
    elif 'ping' in query.lower() or 'net' in query.lower() or 'internet' in query.lower():
        ping_command = ["ping", "-c", "5", "4.4.4.4"]
        subprocess.call(ping_command)
    # Command from terminal
    elif 'asitop' in query.lower():
        subprocess.run(["open", "-a", "iTerm"])
        keyboard.write('sudo asitop')
        keyboard.send('enter')
        keyboard.write(access_code)
        keyboard.send('enter')
    elif 'neofetch' in query.lower():
        subprocess.run(["open", "-a", "iTerm"])
        keyboard.write('neofetch')
        keyboard.send('enter')
    elif 'diagnostic' in query.lower():
        subprocess.Popen(["open", "-a", "iTerm"])
        new_window()

        time.sleep(3)
        keyboard.write("sudo")
        time.sleep(1)
        keyboard.send('space')
        keyboard.write('asitop')
        keyboard.send('enter')
        keyboard.write(access_code)
        keyboard.send('enter')

        new_window()

        time.sleep(1)
        keyboard.write('neofetch')
        time.sleep(1)
        keyboard.press('enter')
        time.sleep(3)

        new_window()

        time.sleep(1)
        keyboard.write('ping')
        keyboard.send('space')
        keyboard.write('4.4.4.4')
        keyboard.send('enter')

        # sleep for 5 packets
        time.sleep(5)

        # stop sending ping
        with KeyBoard.pressed(Key.ctrl):
            KeyBoard.press('c')
            KeyBoard.release('c')

        subprocess.run(["open", "-a", "Activity Monitor"])

        print('Ecco fatto!')

    elif 'CPU' in query.lower():
        cpu_percent = psutil.cpu_percent()
        print("L'utilizzo della CPU è:", cpu_percent, "%")
    elif 'RAM' in query.lower():
        mem_percent = psutil.virtual_memory().percent
        print("L'utilizzo della RAM è:", mem_percent, "%")
    elif 'batteria' in query.lower():
        battery = psutil.sensors_battery()
        battery_percent = battery.percent
        print("La batteria è al", battery_percent, "%")

    elif 'gener' in query.lower() or 'password' in query.lower() or 'casual' in query.lower() or 'random' in query.lower():
        caratteri = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(caratteri) for _ in range(psw_def_length))
        print("La password casuale generata è:", password)

    elif 'reset' in query.lower():
        reset_psw_request = input('Sei sicuro di voler reimpostare la password?(y/n)')
        if reset_psw_request == 'y':
            print("Non posso modificare la password mentre il sistema è in esecuzione")
            print("Apri il mio codice sorgente e modificala manualmente, grazie")
        else:
            print("Ok annullo l'operazione")
            start()
    elif 'chi' in query.lower() or 'sei' in query.lower() or 'chi sei' in query.lower():
        print("Io sono IRIS, l'Intelligenza Rivoluzionaria, Intuitiva e Sperimentale")
    elif 'ora' in query.lower() or 'ore' in query.lower():
        orario()
    elif 'giorno' in query.lower():
        date()

    elif 'speedtest' in query.lower():
        webbrowser.open("https://www.speedtest.net")
    elif 'riavvi' in query.lower():
        login()
    elif 'standby' in query.lower():
        login()
    elif 'meteo' in query.lower():
        city = input("Per quale città vuoi conoscere il meteo?")
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'

        complete_url = base_url + 'q=' + city + '&appid=' + weather_api_key

        response = requests.get(complete_url)

        if response.status_code == 200:
            data = response.json()
            main_data = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            temperature_celsius = temperature - 273.15  # La temperatura è fornita in Kelvin, convertiamola in Celsius
            print(
                f"A {city} il tempo è {main_data} ({description}) con una temperatura di {temperature_celsius:.2f}°C")
        else:
            print("Impossibile ottenere informazioni meteo per la città specificata.")

    elif 'chatgpt' in query.lower():
        webbrowser.open('https://chat.openai.com')

    elif 'screenshot' in query.lower():
        time.sleep(5)
        screenshot()

    elif 'computer' in query.lower() or 'pc' in query.lower():
        pc_action = input('Vuoi effettuare un riavvio o uno spegnimento?')
        if pc_action == 'riavvio':
            subprocess.Popen(["open", "-a", "iTerm"])
            time.sleep(2)
            new_tab()
            time.sleep(2)
            keyboard.write('sudo reboot')
            time.sleep(3)
            keyboard.send('enter')
            time.sleep(1)
            keyboard.write(access_code)
            keyboard.send('enter')
        elif pc_action == 'spegnimento':
            subprocess.Popen(["open", "-a", "iTerm"])
            time.sleep(2)
            new_tab()
            time.sleep(2)
            keyboard.write('sudo shutdown -h now')
            time.sleep(3)
            keyboard.send('enter')
            time.sleep(1)
            keyboard.write('viapcampagna')
            keyboard.send('enter')
        else:
            print('Non ho capito')
    elif 'event' in query.lower():
        try:
            service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
            event = {
                'summary': 'Evento di prova',
                'description': 'Descrizione dell\'evento di prova',
                'start': {
                    'dateTime': '2024-05-04T10:00:00',
                    'timeZone': 'Europe/Rome',
                },
                'end': {
                    'dateTime': '2024-05-04T12:00:00',
                    'timeZone': 'Europe/Rome',
                },
            }
            event = service.events().insert(calendarId='ee2f7c819d7e9ed40b888b90f528f8380b069702a165fb2311aa29afaf31b1e6@group.calendar.google.com', body=event).execute()
            print('Evento creato:', event.get('htmlLink'))
        except Exception as e:
            print('Si è verificato un errore durante la creazione dell\'evento:', e)

    else:
        print("Non ho capito o forse i server hanno un malfunzionamento")
        restart_request = input("Provo a effettuare un riavvio?(y/n)")
        if restart_request == "y":
            login()
        else:
            start()


def start():
    wishme()
    while True:
        query = input("Come posso aiutarla oggi?")
        Iris_modules(query)


def login():
    print('Caricamento...')
    time.sleep(1)
    writed_access_code = input("IRIS è protetto da una password, immettila per continuare:")
    if writed_access_code == access_code:
        print("*Accesso eseguito*")
        start()
    else:
        print("Le credenziali di accesso sono errate, riprova")
        login()


if __name__ == '__main__':
    login()
