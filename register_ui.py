from PySide6 import QtCore, QtGui, QtWidgets
import pyodbc
import sys

class Ui_Form(object):
     
    def __init__(self, manager):
        self.manager = manager
        self.form = QtWidgets.QWidget() 
        self.setupUi(self.form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(566, 425)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 280, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(120, 175, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QLineEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(250, 165, 211, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 280, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.Name = QtWidgets.QLabel(parent=Form)
        self.Name.setGeometry(QtCore.QRect(120, 135, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.plainTextEdit = QtWidgets.QLineEdit(parent=Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(250, 125, 211, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(120, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 210, 211, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(100, 330, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 340, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.register)
        self.pushButton_3.clicked.connect(self.redirect_to_login)
        self.pushButton_2.clicked.connect(self.clear_field)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Clear"))
        self.label.setText(_translate("Form", "Email ID"))
        self.pushButton.setText(_translate("Form", "Register"))
        self.pushButton_3.setText(_translate("Form", "Login"))
        self.Name.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "Register Form"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "Click here for Login"))

    def register(self):
        password = self.textEdit_2.text()
        name = self.plainTextEdit.text()
        email = self.textEdit.text()
        
        # Database connection parameters
        server = 'ALOK\\SQLEXPRESS'
        database = 'alokdb'
        
        try:
            # Establish connection to the database
            connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            
            # Check if the email already exists in the database
            query = "SELECT * FROM users1 WHERE email = ?"
            cursor.execute(query, (email,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                QtWidgets.QMessageBox.critical(None, 'Registration', 'Email already exists. Please choose a different one.')
            else:
                # Insert the new user data into the database
                insert_query = "INSERT INTO users1 (name, email, password) VALUES (?, ?, ?)"
                cursor.execute(insert_query, (name, email, password))
                conn.commit()
                
                QtWidgets.QMessageBox.information(None, 'Registration', 'Registration successful!')
                self.clear_field()
        
        except pyodbc.Error as e:
            QtWidgets.QMessageBox.critical(None, 'Database Error', f'An error occurred: {str(e)}')
        
        finally:
            # Close the database connection
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    

    def clear_field(self):  
        self.plainTextEdit.clear()
        self.textEdit.clear() 
        self.textEdit_2.clear() 

    def redirect_to_login(self):
        self.manager.show_login_window()  
        self.manager.close_current_window(self.form)    
             


