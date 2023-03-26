from flask import Flask, render_template

azul_app = Flask(__name__)

@azul_app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    azul_app.run(debug=True)