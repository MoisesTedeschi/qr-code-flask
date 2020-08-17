import pyqrcode


def qrcode_genetator(info):
    qrcode = pyqrcode.create(info)
    #qrcode.svg (info+'.svg', scale=8)
    #qrcode.svg (info+'.eps', scale=2)
    qrcode.png(info+'.png', scale = 6)
