import os
import time
import sys
import os
import threading as th


def install_pyqt():
    global root
    root = Tk()
    lbl = Label(root, text="필요한 라이브러리 설치중")
    lbl.pack()
    root.mainloop()
try:
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    import PyQt5
except:
    from tkinter import *
    th.Thread(target=install_pyqt, daemon=True).start()
    
    os.system('pip install PyQt5==5.15.2')
    
    lbl = Label(root, text="설치 완료 프로그램 재시작")
    lbl.pack()

app = QApplication([sys.argv])


class widget(QLabel) :   

    def __init__(self, parent =None) -> None:
        super().__init__(parent)
        self.number = 0
        self.setWindowTitle('시스템 종료까지 남은 시간')
        self.resize(220,50)
        # self.show()
        inputtext ,ok = QInputDialog.getInt(self, '타이머', '타이머 시간 입력\n초 시간을 입력해주세요', )
        if not ok or inputtext== 0 :
            self.closeEvent()
            
        # text = QLabel(self)
        self.setFont(QFont('Arial', 20)) 
        self.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.show()
        tt = inputtext # 시간초가 되어야함
        self.tttt = time.time() + tt
        self.tt =  self.tttt - tt
        th.Thread(target=self.set_timer, daemon=True).start()
    def closeEvent(self, ddd=None) -> None:
        sys.exit()
        
    def set_timer(self) :
        while 1:
            self.tt = self.tttt - time.time()
            h =  round(divmod(self.tt, 3600)[0])
            m =  round(divmod(divmod(self.tt, 3600)[1], 60)[0])
            s =  round(divmod(self.tt, 60)[1])
            self.setText('{:02} : {:02} : {:02}'.format(h, m, s))
            
            if time.time() >= self.tttt :
                os.system('shutdown -s -f -t 0')
            time.sleep(1)
                
        
    
start_window = widget()



sys.exit(app.exec_())
