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
import speech_recognition as sr



access_code = 'viapcampagna'
KeyBoard = Controller()
psw_def_lenght = 12
weather_api_key = '72aeef4512500a15bbd668cec05fdb34'


# Hotkeys
def new_tab():
    with KeyBoard.pressed(Key.cmd):
        KeyBoard.press('t')
        KeyBoard.release('t')


def new_window():
    with KeyBoard.pressed(Key.cmd):
        KeyBoard.press('n')
        KeyBoard.release('n')


def Iris_modules(main_task_request):
    # Website saved
    if 'google' in main_task_request.lower():
        webbrowser.open("https://www.google.com")
    elif 'gmail' in main_task_request.lower():
        webbrowser.open("https://www.gmail.com")
    elif 'youtube' in main_task_request.lower() or 'yt' in main_task_request.lower():
        webbrowser.open("https://www.youtube.com")
    elif 'instagram' in main_task_request.lower() or 'ig' in main_task_request.lower():
        webbrowser.open("https://www.instagram.com")
    elif 'github' in main_task_request.lower():
        webbrowser.open("https://www.github.com")
    elif 'drive' in main_task_request.lower():
        webbrowser.open("https://www.drive.google.com")
    elif 'soundcloud' in main_task_request.lower():
        webbrowser.open("https://www.soundcloud.com")
    elif 'amazon' in main_task_request.lower():
        webbrowser.open("https://www.amazon.it")
    elif 'twich' in main_task_request.lower():
        webbrowser.open("https://www.twich.tv")
    # App
    elif 'premiere' in main_task_request.lower():
        subprocess.Popen([
            "/Applications/Adobe Premiere Pro 2022/Adobe Premiere Pro 2022.app/Contents/MacOS/Adobe Premiere Pro 2022"])
    elif 'after effect' in main_task_request.lower():
        subprocess.Popen(
            ["/Applications/Adobe After Effects 2022/Adobe After Effects 2022.app/Contents/MacOS/After Effects"])
    elif 'photoshop' in main_task_request.lower():
        subprocess.Popen(
            ["/Applications/Adobe Photoshop 2022/Adobe Photoshop 2022.app/Contents/MacOS/Adobe Photoshop 2022"])
    elif 'spotify' in main_task_request.lower():
        subprocess.Popen(["/Applications/Spotify.app/Contents/MacOS/Spotify"])
    elif 'discord' in main_task_request.lower():
        subprocess.Popen(["/Applications/Discord.app/Contents/MacOS/Discord"])
    elif 'telegram' in main_task_request.lower():
        subprocess.Popen(["/Applications/Telegram.localized/Telegram.app/Contents/MacOS/Telegram"])
    elif 'whatsapp' in main_task_request.lower():
        subprocess.Popen(["/Applications/WhatsApp.app/Contents/MacOS/WhatsApp"])
    # Other internet function
    elif 'IP' in main_task_request.lower():
        print("Sto ottenendo le diagnostiche di rete")
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("Host:", hostname)
        print("Indirizzo IP:", ip)
    elif 'ping' in main_task_request.lower() or 'net' in main_task_request.lower() or 'internet' in main_task_request.lower():
        ping_command = ["ping", "-c", "5", "4.4.4.4"]
        subprocess.call(ping_command)
    # Command from terminal
    elif 'asitop' in main_task_request.lower():
        subprocess.run(["open", "-a", "iTerm"])
        keyboard.write('sudo asitop')
        keyboard.send('enter')
        keyboard.write(access_code)
        keyboard.send('enter')
    elif 'neofetch' in main_task_request.lower():
        subprocess.run(["open", "-a", "iTerm"])
        keyboard.write('neofetch')
        keyboard.send('enter')
    elif 'diagnostic' in main_task_request.lower():
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

    elif 'CPU' in main_task_request.lower():
        cpu_percent = psutil.cpu_percent()
        print("L'utilizzo della CPU è:", cpu_percent, "%")
    elif 'RAM' in main_task_request.lower():
        mem_percent = psutil.virtual_memory().percent
        print("L'utilizzo della RAM è:", mem_percent, "%")
    elif 'batteria' in main_task_request.lower():
        battery = psutil.sensors_battery()
        battery_percent = battery.percent
        print("La batteria è al", battery_percent, "%")

    elif 'gener' in main_task_request.lower() or 'password' in main_task_request.lower() or 'casual' in main_task_request.lower() or 'random' in main_task_request.lower():
        caratteri = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(caratteri) for _ in range(psw_def_lenght))
        print("La password casuale generata è:", password)

    elif 'reset' in main_task_request.lower():
        reset_psw_request = input('Sei sicuro di voler reimpostare la password?(y/n)')
        if reset_psw_request == 'y':
            print("Non posso modificare la password mentre il sistema è in esecuzione")
            print("Apri il mio codice sorgente e modificala manualmente, grazie")
        else:
            print("Ok annullo l'operazione")
            start()
    elif 'chi' in main_task_request.lower() or 'sei' in main_task_request.lower() or 'chi sei' in main_task_request.lower():
        print("Io sono IRIS, l'Intelligenza Rivoluzionaria, Intuitiva e Sperimentale")
    elif 'ora' in main_task_request.lower() or 'ore' in main_task_request.lower():
        data_ora_attuali = datetime.datetime.now()
        data_ora_formattata = data_ora_attuali.strftime("%d-%m-%Y %H:%M:%S")
        print("La data e l'ora attuali sono:", data_ora_formattata)
    elif 'giorno' in main_task_request.lower() or 'oggi' in main_task_request.lower():
        data_ora_attuali = datetime.datetime.now()
        data_ora_formattata = data_ora_attuali.strftime("%d-%m-%Y %H:%M:%S")
        print("La data e l'ora attuali sono:", data_ora_formattata)

    elif 'speedtest' in main_task_request.lower():
        webbrowser.open("https://www.speedtest.net")
    elif 'riavvi' in main_task_request.lower():
        login()
    elif 'standby' in main_task_request.lower():
        login()
    elif 'meteo' in main_task_request.lower():
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

    elif 'chatgpt' in main_task_request.lower():
        webbrowser.open('https://chat.openai.com')

    elif 'computer' in main_task_request.lower() or 'pc' in main_task_request.lower():
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

    else:
        print("Non ho capito o forse c'è un problema nei miei datacenter")
        restart_request = input("Provo a effettuare un riavvio?")
        if restart_request == "y":
            login()
        else:
            start()


def start():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ascolto...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            transcribed_text = r.recognize_sphinx(audio, show_all=False)
            print("Trascrizione:", transcribed_text)
            Iris_modules(transcribed_text)
        except sr.UnknownValueError:
            print("Sphinx non ha potuto comprendere il parlato")
        except sr.RequestError as e:
            print("Errore durante la richiesta al servizio di riconoscimento vocale: {0}".format(e))
def login():
    print('Caricamento...')
    writed_access_code = input("IRIS è protetto da una password, immettila per continuare:")
    if writed_access_code == access_code:
        print("Accesso eseguito")
        start()
    else:
        print("Le credenziali di accesso sono errate, riprova")
        login()


if __name__ == '__main__':
    login()
