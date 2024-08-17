from flask import Flask, request, url_for, redirect, render_template
from logic import server_login, wishme, logic
import os
import subprocess
import signal

app = Flask(__name__)
@app.route('/',methods=['POST', 'GET'])

def index ():
    return render_template('index.html')

@app.route('/auth', methods=['POST', 'GET'])
def auth():
    #recupera input password
    text_input = request.form['text_input']
    #prova autenticazione
    response = server_login(text_input)


    if response == True:
        return redirect(url_for('home'))
    else: 
        error = "La password è errata, riprova"
        return render_template('index.html', error=error)


def shutdown_server():
    pid = os.getpid()  # Ottiene il PID del processo corrente
    os.kill(pid, signal.SIGINT)  # Invia un segnale per terminare il processodef shutdown():

@app.route('/home', methods=['POST', 'GET'])
def home():
    greeting = wishme()
    result = None
    if request.method == 'POST':
        data_input = request.form['text_input']
        result = logic(data_input)
    return render_template('home.html', greeting=greeting, result=result)



@app.route('/shutdown', methods=['POST', 'GET'])

def shutdown():
    if request.method == 'POST':
        shutdown_server()
        return "Il server è stato spento con successo."
    else:
        return render_template('shutdown.html')  

@app.route('/open_source_code')
def open_source_code():
    # Definisci il percorso della cartella (directory) del progetto
    folder_path = os.path.dirname(os.path.abspath(__file__))  # Ottiene la directory attuale del file
    
    try:
        if os.name == 'nt':  # Windows
            os.startfile(folder_path)  # Apre la cartella nel file explorer di Windows
        elif os.name == 'posix':  # macOS o Linux
            subprocess.Popen(['open', folder_path])  # Per macOS (Finder)
            # subprocess.Popen(['xdg-open', folder_path])  # Per Linux (File Manager)
        return "Cartella del progetto aperta con successo!"
    except Exception as e:
        return f"Errore nell'aprire la cartella: {e}"





if __name__ == '__main__':
    app.run(debug=True)