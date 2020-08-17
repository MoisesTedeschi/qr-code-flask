import pyqrcode


def qrcode_genetator(info):
    qrcode = pyqrcode.create(info)
    qrcode.png(info+'.png', scale=8)