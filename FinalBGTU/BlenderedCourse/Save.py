from flask import Flask, request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

# Путь к вашему текстовому файлу для хранения данных
Data_Base = '/UserList.txt'
app.secret_key = 'секретный_ключ'  # Необходимо для использования сессий

@app.route('/')
def index():
    return render_template('Registration.html')
        
@app.route('/submit', methods=['POST'])
def submit():
    First_name = request.form['First_name']
    Second_name = request.form ['Second_name']
    Email = request.form['Usermail']
    Password_send = request.form['Password']
    
    with open(Data_Base, 'a' , encoding='utf-8') as file:
        file(f'{First_name},{Second_name},{Email},{Password_send} \n')
    return(redirect(url_for('LogIn.html')))

def load_users(filename):
    Users = {}
    with open(filename, 'r') as file:
        for line in file:
            First_name, Second_name, Email, Password_send = line.strip().split(',')
            Users[Email] = {
                'first_name': First_name,
                'second_name': Second_name,
                'password_hash': generate_password_hash(Password_send)  # Хэшируем пароль
            }
    return Users

Data_Base = load_users('/UserList.txt')

@app.route('/LogIn', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Email = request.form['Usermail']
        Password_send = request.form['Password']
        
        User = Data_Base.get(Email)
        if User and check_password_hash(User['password_hash'], Password_send):
            session['Usermail'] = Email  # Сохраняем электронную почту в сессии
            flash('Успешный вход в систему!')
            return redirect(url_for('PersonalAccount'))  # Перенаправление на страницу аккаунта
        else:
            flash('Неверный адрес электронной почты или пароль!')
    
    return render_template('login.html')  # Отображение формы входа

@app.route('/PersonalAccount')
def personal_account():
    Email = session.get('Usermail')
    if Email:
        User = Data_Base[Email]
        return render_template('PersonalAccount.html', User=User)
    else:
        flash('Пожалуйста, выполните вход в систему.')
        return redirect(url_for('LogIn.html'))



if __name__ == '__main__':
    app.run(debug=True)
