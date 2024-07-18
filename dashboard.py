from ui_dashboard import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QLabel



class MyDashboard(QMainWindow, Ui_MainWindow):
    def __init__(self, manager, user_name):
        super().__init__()
        self.manager = manager
        self.user_name = user_name 
        self.setupUi(self)
   
        self.stackedWidget_2 = self.findChild(QStackedWidget, "stackedWidget_2")
        self.setWindowTitle("Dashboard Menu")

        self.icon_name_widget.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_dashboardpage)
        self.dashboard_2.clicked.connect(self.switch_to_dashboardpage)

        self.employee_1.clicked.connect(self.switch_to_Employeepage)
        self.employee_2.clicked.connect(self.switch_to_Employeepage)

        self.notification_1.clicked.connect(self.switch_to_Notificationpage)
        self.notification_2.clicked.connect(self.switch_to_Notificationpage)

        self.profile_1.clicked.connect(self.switch_to_Profilepage)
        self.profile_2.clicked.connect(self.switch_to_Profilepage)

        self.setting_1.clicked.connect(self.switch_to_Settingpage)
        self.setting_2.clicked.connect(self.switch_to_Settingpage)


    def switch_to_dashboardpage(self):
        self.stackedWidget_2.setCurrentIndex(0) 

    def switch_to_Employeepage(self):
        self.stackedWidget_2.setCurrentIndex(1) 

    def switch_to_Notificationpage(self):
        self.stackedWidget_2.setCurrentIndex(2) 

    def switch_to_Profilepage(self):
        self.stackedWidget_2.setCurrentIndex(3) 

    def switch_to_Settingpage(self):
        self.stackedWidget_2.setCurrentIndex(4)    
    
