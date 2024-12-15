from flask import Flask, request, render_template
from forms import RegistrationForm
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
DATA_FILE = 'UserList.txt'
@app.route('?')
@app.route('/submit', methods=['GET','POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data


        with open('UserList.txt','a') as file:
            file.write(f'{name},{email}\n')
        return 'Данные успешно отправлены!'
    return render_tmplate('index.html', form=form)
if __name__ == '__main__':
    app.run(debuf=True)