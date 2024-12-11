from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

# Путь к вашему текстовому файлу для хранения данных
DATA_FILE = '/UserList.txt'

@app.route('/')
def index():
    return render_template('Registration.html')
        
@app.route('/submit', methods=['POST'])
def submit():
    First_name = request.form['First_name']
    Second_name = request.form ['Second_name']
    mail = request.form['Usermail']
    Password_send = request.form['Password']
    
    with open(DATA_FILE, 'a') as file:
        file.write(f'{First_name},{Second_name},{mail},{Password_send} \n')
    return render_template('LogIn.html')

    

if __name__ == '__main__':
    app.run(debug=True)