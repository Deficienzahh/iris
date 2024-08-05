from flask import Flask, request, url_for, redirect, render_template
from logic import server_login, wishme, logic

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
        return """
        <h1>Iris AI</h1>
        <h2>La password è errata</h2>
        <form action="/">
        <button>Torna indietro</button>
        </form>
        """

@app.route('/home', methods=['POST', 'GET'])
def home():
    greeting = wishme()
    result = None
    if request.method == 'POST':
        data_input = request.form['text_input']
        result = logic(data_input)
    return render_template('home.html', greeting=greeting, result=result)



if __name__ == '__main__':
    app.run(debug=True)