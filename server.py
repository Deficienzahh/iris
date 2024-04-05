from flask import Flask, request
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

app = Flask(__name__)

# Imposta le variabili globali necessarie
KeyBoard = Controller()
access_code = 'viapcampagna'
psw_def_lenght = 12
weather_api_key = '72aeef4512500a15bbd668cec05fdb34'
def new_tab():
    with KeyBoard.pressed(Key.cmd):
        KeyBoard.press('t')
        KeyBoard.release('t')

def new_window():
    with KeyBoard.pressed(Key.cmd):
        KeyBoard.press('n')
        KeyBoard.release('n')


# Funzioni ausiliarie per il backend Flask
def handle_website_request(url):
    subprocess.Popen(["open", url])


def handle_application_request(application_path):
    subprocess.Popen(["open", application_path])


# Funzioni per le rotte del backend Flask
@app.route('/')
def home():
    return 'Benvenuto nel backend di Iris!'


@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form['question']
    return handle_task(question)


def handle_task(main_task_request):
    # Implementa le funzionalità di Iris qui
    if 'google' in main_task_request.lower():
        handle_website_request("https://www.google.com")
    elif 'gmail' in main_task_request.lower():
        handle_website_request("https://www.gmail.com")
    elif 'youtube' in main_task_request.lower() or 'yt' in main_task_request.lower():
        handle_website_request("https://www.youtube.com")
    # Implementa altre funzionalità di Iris qui
    else:
        return "Non ho capito la tua richiesta"

    return "Operazione eseguita con successo"

if __name__ == '__main__':
    app.run(debug=True)
