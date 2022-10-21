from ctypes import alignment
from msilib.schema import TextStyle
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit)
from PyQt5.QtCore import  Qt  

app = QApplication([])

window = QWidget()

window.resize(300,500)

window.show()

label1 = QLabel("Перше число")
input1 = QLineEdit()

label2 = QLabel("Друге число")
input2 = QLineEdit()

button1 = QPushButton("Знайти більше")
button2 = QPushButton("Знайти меньше")
result = QLabel("Результат: ?")

main_line = QVBoxLayout()

main_line.addWidget(label1, alignment=Qt.AlignCenter)
main_line.addWidget(input1, alignment=Qt.AlignCenter)
main_line.addWidget(label2, alignment=Qt.AlignCenter)
main_line.addWidget(input2, alignment=Qt.AlignCenter)
main_line.addWidget(button1, alignment=Qt.AlignCenter)
main_line.addWidget(button2, alignment=Qt.AlignCenter)
main_line.addWidget(result, alignment=Qt.AlignCenter, )

window.setLayout(main_line)


listn = list()
        
def result1():
    listn.append(input1.text())
    listn.append(input2.text())
    a = max(listn)
    result.setText(f"Рузельтат: " + a)
    listn.clear()
def result2():
    listn.append(input1.text())
    listn.append(input2.text())
    b = min(listn)
    result.setText(f"Рузельтат: " + b)
    listn.clear()
    
                    
button1.clicked.connect(result1)
button2.clicked.connect(result2)

app.exec_()