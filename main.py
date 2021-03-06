#pip install os-sys
import sys
#pip install PyQt5
from PyQt5.QtCore import *
from  PyQt5.QtWidgets import *
#pip install PyQtWebEngine
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn =QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)


        #browser forword button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)


        # browser reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # browser home button
        homw_btn = QAction('Home',self)
        homw_btn.triggered.connect(self.navigate_bar)
        navbar.addAction(homw_btn)

        # browser url import field
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

    # browser home button location
    def navigate_bar(self):
        self.browser.setUrl(QUrl('http://google.com'))

    # browser url import field
    def navigate_to_url(self):
        url = self.url_bar()
        self.browser.setUrl(QUrl(url))


app = QApplication(sys.argv)
QApplication.setApplicationName('Devhack team')
window = MainWindow()
app.exec()
