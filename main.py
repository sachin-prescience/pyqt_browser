import sys

from PyQt6.QtCore import QThread, QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import *


PORT = 5000
ROOT_URL = "http://localhost:{}".format(PORT)


class FlaskThread(QThread):
    def __init__(self, application):
        QThread.__init__(self)
        self.application = application

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=PORT)


def provide_GUI_for(application):
    qtapp = QApplication(sys.argv)

    webapp = FlaskThread(application)
    webapp.start()

    qtapp.aboutToQuit.connect(webapp.terminate)

    webview = QWebEngineView()
    webview.load(QUrl(ROOT_URL))
    webview.show()

    return qtapp.exec()


from web.server import app

if __name__ == "__main__":
    sys.exit(provide_GUI_for(app))
