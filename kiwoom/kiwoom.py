#OCX 방식의 컴포넌트 => 응용프로그램에서 키움 오픈API 실행할수 있도록 한것 // 제어가 가능!
#파이썬에서 위의 제어를 하도록
from PyQt5.QAxContainer import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        print("kiwoom 클래스 입니다")
        self.get_ocx_instance()
        self.event_slots()
        self.signal_login_CommConnect()
        #아래 함수로 응용프로그램을 제어할 수 있음

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)

    def login_slot(self, errCode):
        print(errCode)

    def signal_login_CommConnect(self):
        self.dynamicCall("CommConnect()")
