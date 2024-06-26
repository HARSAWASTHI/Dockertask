# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<b>Hello,Welcome to contanerised Python App</b><br><b>Name= Harsh Awasthi</b><br><b>Age= 26</b><br><b>E-mail= ***@gmail.com</b><br><b>Batch= Devops</b>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

