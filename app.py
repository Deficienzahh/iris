from flask import Flask, request, url_for, redirect, render_template
from main import login1

app = Flask(__name__)
@app.route('/',methods=['GET'])

def index ():
    return render_template('index.html')

def auth():
    #recupera input password
    text_input = request.form['text_input']
    #prova autenticazione
    response = login1(text_input)

    return f"<h1>{response}</h1>"


if __name__ == '__main__':
    app.run(debug=True)