import sys
from PySide6.QtWidgets import QApplication
from login1_ui import Ui_MainWindow
from dashboard import MyDashboard
from register_ui import Ui_Form

class WindowManager:
    def __init__(self):
        self.app = QApplication.instance() or QApplication([])
        self.login1 = None
        self.dashboard = None
        self.register_ui = None
        self.current_window = None 
        self.session_active = False  # Session state

    def show_main_window(self,user_name):
         if self.session_active:
            self.dashboard = MyDashboard(self,user_name)
            self.dashboard.show()
         else:
            self.show_login_window()
    
    def show_login_window(self):
        self.login1 = Ui_MainWindow(self)
        self.login1.show()

    def show_register_window(self):
        self.register_ui = Ui_Form(self)
        self.register_ui.form.show()
        self.current_window = self.register_ui.form   

    def close_current_window(self, window):
        window.close()
        self.current_window = None
        
    def create_session(self):
        self.session_active = True

    def clear_session(self):
        self.session_active = False    

if __name__ == "__main__":
    manager = WindowManager()
    manager.show_login_window()
    sys.exit(manager.app.exec())
