from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit
from PyQt5.QtGui import QFont
import sys
class login_win(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit')
        self.setFixedSize(500,350)
        self.l1()
        self.l2()

    def l1(self):
        username = QLineEdit(self)
        username.setPlaceholderText("Username....")
        username.move(75, 90)
        username.setFont(QFont("Times New Roman", 12))
        username.setFixedSize(350, 50)
        username.setStyleSheet("""
            QLineEdit {
                border: 3px solid black;
                border-radius: 15px;
                padding: 35px;
            }
            QLineEdit:focus {
                border: 3px solid green;
            }
            QLineEdit:hover {
                border: 3px solid blue;
            }
        """)
    def l2(self):
        username = QLineEdit(self)
        username.setPlaceholderText("Username....")
        username.move(75, 180)
        username.setFont(QFont("Times New Roman", 12))
        username.setFixedSize(350, 50)
        username.setStyleSheet("""
            QLineEdit {
                border: 3px solid black;
                border-radius: 15px;
                padding: 35px;
            }
            QLineEdit:focus {
                border: 3px solid green;
            }
            QLineEdit:hover {
                border: 3px solid blue;
            }
        """)

app = QApplication(sys.argv)
window = login_win()
window.show()
sys.exit(app.exec_())
