from flask import Flask, request, render_template, redirect, url_for, session, flash
import os

app = Flask(__name__)

# Путь к вашему текстовому файлу для хранения данных
DATA_FILE = '/UserList.txt'

@app.route('/')
def index():
    return render_template('LogIn.html')
        
@app.route('/LogIn', methods=['POST'])
def submit():
    mail = request.form['Usermail']
    Password_send = request.form['Password']
    
    # Сохраняем данные в текстовом файле
    with open(DATA_FILE, 'r') as file:
        file.write(f'{First_name},{Second_name},{Gender},{mail},{Password_send} \n')
    if  Password_send and mail == DATA_FILE:
        return redirect(url_for('PersonalAccount.html'))
    else: 
        return(redirect(url_for('LogIn.html')))



if __name__ == '__main__':
    app.run(debug=True)