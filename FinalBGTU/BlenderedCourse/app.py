from flask import Flask, request, render_template

app = Flask(__name__)

DATA_FILE = 'UserList.txt'

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/submit', methods=['POST'])
def submit_registration():
    First_name = request.form['First_name']
    Second_name = request.form['Second_name']
    mail = request.form['Usermail']
    Password_send = request.form['Password']
    with open(DATA_FILE, 'a') as file:
        file.write(f'{First_name},{Second_name},{mail},{Password_send} \n')
    
    return render_template('LogIn.html')

@app.route('/submit_login', methods=['POST'])
def user_login():
    usermail = request.form['Usermail']
    password_check = request.form['Password']
    with open(DATA_FILE, 'r') as data:
        for line in data:
            First_name, Second_name, email, Password = line.strip().split(',') ##First и Second nam'ы негде использовать, но они нужны чтобы программа правильно распаковала данные 
            if email == usermail and Password == password_check:
                return render_template('PersonalAccount.html')
    return render_template('LogIn.html')

if __name__ == '__main__':
    app.run(debug=True)