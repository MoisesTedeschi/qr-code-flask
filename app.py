from qr import qrcode_genetator
from flask import Flask, render_template, send_file, request


app = Flask(__name__)


@app.route('/qr-code-generator')
def home():
    return render_template('index.html')


@app.route('/converterd', methods = ['POST'])
def convert():
    global info_input
    info_input = request.form['test']
    return render_template('converted.html')


@app.route('/download')
def download():
    qrcode_genetator(info_input)
    filename = f'{info_input}.png'
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
