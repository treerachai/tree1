# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("กรุณาเอาเอา PIN นี้ไปไส่ในหน้าไลน์ '" + pin + "' SELFBOT PY.3 BY.SAI")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='สแกน QR นี้ '
        else:
            notice=''
        self.callback('SELF ' + notice + 'BOT PY.3 BY.SAI\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)