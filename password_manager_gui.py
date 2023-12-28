#!/usr/bin/python3

"""
    This file is handles all the GUI related tasks
"""
import sys

from PyQt5.Qt import QApplication, QMainWindow, QWidget, QWindow, QLabel, QLayout, QBoxLayout
from PyQt5 import QtWidgets, Qt


class GuiWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(720, 200, 640, 480)
        self.setWindowTitle("Password Manager")

        self.tabs_widget_obj = QtWidgets.QTabWidget(self)
        self.tab1_widget_obj = QWidget()
        self.tab2_widget_obj = QWidget()
        self.tab3_widget_obj = QWidget()

        # For tab1 generating password
        self.vbox_layout = QtWidgets.QVBoxLayout(self)
        self.label1_obj = QLabel("Choose the parameters for generating password")
        self.radio_btn1_obj = QtWidgets.QRadioButton(self)
        self.radio_btn2_obj = QtWidgets.QRadioButton(self)
        self.radio_btn3_obj = QtWidgets.QRadioButton(self)
        self.label2_obj = QLabel(" Choose Length")
        self.combo_box_obj = QtWidgets.QComboBox(self)
        self.generate_button = QtWidgets.QPushButton(self)
        self.label3_obj = QLabel("PASSWORD")
        self.copy_button_obj = QtWidgets.QPushButton(self)

        self.define_objects()

    def define_objects(self):
        # Defining tabs values
        self.tabs_widget_obj.resize(640, 480)
        self.tabs_widget_obj.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabs_widget_obj.addTab(self.tab1_widget_obj, "Password Generator")
        self.tabs_widget_obj.addTab(self.tab2_widget_obj, "Encrypt")
        self.tabs_widget_obj.addTab(self.tab3_widget_obj, "Decrypt")

        # Setting text for radio buttons and submit buttons and combobox
        self.radio_btn1_obj.setText("Alphabets only")
        self.radio_btn2_obj.setText("Alphabets + numbers")
        self.radio_btn3_obj.setText("Alphabets + numbers + special characters")
        self.combo_box_obj.addItems([str(x) for x in range(5, 65)])
        self.combo_box_obj.setMaxVisibleItems(15)
        self.generate_button.setText("Generate")
        self.copy_button_obj.setText("Copy to clipboard")

        # Setting object dimensions
        self.label1_obj.setFixedHeight(40)
        self.radio_btn1_obj.setFixedHeight(20)
        self.radio_btn2_obj.setFixedHeight(20)
        self.radio_btn3_obj.setFixedHeight(20)
        self.label2_obj.setFixedHeight(40)
        self.combo_box_obj.setFixedWidth(100)
        self.combo_box_obj.setFixedHeight(20)
        self.generate_button.setFixedWidth(100)
        self.generate_button.setFixedHeight(40)
        # self.label3_obj.setFixedHeight(40)
        self.copy_button_obj.setFixedWidth(150)

        # Setting all the widgets into layout for password generation tab
        self.vbox_layout.addWidget(self.label1_obj)
        self.vbox_layout.addWidget(self.radio_btn1_obj)
        self.vbox_layout.addWidget(self.radio_btn2_obj)
        self.vbox_layout.addWidget(self.radio_btn3_obj)
        self.vbox_layout.addWidget(self.label2_obj)
        self.vbox_layout.addWidget(self.combo_box_obj)
        self.vbox_layout.addWidget(self.generate_button)
        self.vbox_layout.addWidget(self.label3_obj)
        self.vbox_layout.addWidget(self.copy_button_obj)
        self.tab1_widget_obj.setLayout(self.vbox_layout)




        # self.tabs_widget_obj.adjustSize()




        # self.layout_obj = QtWidgets.QVBoxLayout()
        # self.main_widget = QWidget(self)
        # self.main_widget.setLayout(self.layout_obj)
        # self.label_1 = QLabel("Hi")
        # self.label_2 = QLabel("helo")
        # self.label_3 = QLabel("slkjdlf")
        #
        # self.layout_obj.addWidget(self.label_1)
        # self.layout_obj.addWidget(self.label_2)
        # self.layout_obj.addWidget(self.label_3)
        #
        # self.setCentralWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuiWindow()
    window.show()
    sys.exit(app.exec_())
