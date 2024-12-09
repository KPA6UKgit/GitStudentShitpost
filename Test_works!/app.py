from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Путь к вашему текстовому файлу для хранения данных
DATA_FILE = 'K:/Codding/FinalBGTU/datatest.txt'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    # Сохраняем данные в текстовом файле
    with open(DATA_FILE, 'a') as file:
        file.write(f'{name}, {email}\n')
    
    return 'Данные успешно отправлены!'

if __name__ == '__main__':
    app.run(debug=True)