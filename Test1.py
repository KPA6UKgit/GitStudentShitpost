from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Путь к вашему текстовому файлу для хранения данных
DATA_FILE = 'DATATEST.txt'

@app.route('/')
def index():
    return render_template('index.html')

    # Сохраняем данные в текстовом файле
@app.route('/save_data', methods=['POST'])
def save_data():
       # Предположим, что вы получаете данные из формы
       data = request.form['data']  # Замените 'data' на имя вашего поля формы

       # Открываем файл для записи
       with open('output.txt', 'a') as file:  # 'a' - режим добавления
           file.write(data + '\n')  # Записываем данные и добавляем перевод строки

       return 'Данные сохранены!'
        
  

if __name__ == '__main__':
    app.run(debug=True)