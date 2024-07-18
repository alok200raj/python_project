from PySide6 import QtCore, QtGui, QtWidgets
import pyodbc


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(100, 50, 100, 50)
        self.verticalLayout.setSpacing(20)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: black;")
        self.verticalLayout.addWidget(self.label_2)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setSpacing(10)

        self.Name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Name.setStyleSheet("color: black;")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Name)

        self.plainTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px; color: black;")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: black;")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)

        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textEdit.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px; color: black;")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #007BFF; color: white; padding: 10px; border-radius: 5px; color: black;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #DC3545; color: white; padding: 10px; border-radius: 5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color: black;")
        self.verticalLayout.addWidget(self.label_4)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #28A745; color: white; padding: 10px; border-radius: 5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3, alignment=QtCore.Qt.AlignCenter)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.clear_field)
        self.pushButton_3.clicked.connect(self.redirect_to_register)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name.setText(_translate("MainWindow", "Email ID"))
        self.label.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "Login Form"))
        self.label_4.setText(_translate("MainWindow", "New users Register Here"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))

    def submit(self):
        email = self.plainTextEdit.text()
        password = self.textEdit.text()

        # Database connection parameters
        server = 'ALOK\\SQLEXPRESS'
        database = 'alokdb'

        try:
            connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()

            # Check if the email and password exist in the database
            query = "SELECT * FROM users1 WHERE email = ? AND password = ?"
            cursor.execute(query, (email, password))
            result = cursor.fetchone()

            if result:
                user_name = result[3] 
                QtWidgets.QMessageBox.information(None, 'Login', 'Login successful!')
                self.clear_field()
                self.manager.create_session()
                self.redirect_to_dashboard(user_name)
            else:
                QtWidgets.QMessageBox.critical(None, 'Login', 'Login failed. Check your email and password.')

            conn.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Connection', f'Failed to connect to database: {str(e)}')

    def clear_field(self):
        self.plainTextEdit.clear()
        self.textEdit.clear()

    def redirect_to_dashboard(self, user_name):
        self.manager.close_current_window(self)
        self.manager.show_main_window(user_name)

    def redirect_to_register(self):
        self.manager.show_register_window()
        self.manager.close_current_window(self)