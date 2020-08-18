from qr import qrcode_genetator
from flask import Flask, render_template, send_file, request
from pyqrcode import QRCode

app = Flask(__name__)

@app.route('/')
@app.route('/qr-code-generator')
def home():
    return render_template('index.html')


@app.route('/converted', methods = ['GET', 'POST'])
def converted():
    global info_input

    if request.method == "POST":
        info_input = request.form['valor_entrada']
        print(info_input)
        return render_template('converted.html')

    return render_template('index.html')

@app.route('/download')
def download():
    qrcode_genetator(info_input)
    filename = info_input+'.png'
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
