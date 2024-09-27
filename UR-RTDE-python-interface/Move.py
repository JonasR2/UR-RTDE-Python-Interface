import rtde_control, rtde_receive, rtde_io, ast, sys , pyperclip, time, os, pyautogui
from PyQt5 import QtWidgets
from move_gui import Ui_MainWindow


speed = 0.03
dir_path = os.path.dirname(os.path.realpath(__file__))


try:
    ip = "192.168.0.11"
    rtde_c = rtde_control.RTDEControlInterface(ip)
    rtde_r = rtde_receive.RTDEReceiveInterface(ip)
    rtde_io_ = rtde_io.RTDEIOInterface(ip)
    rtde_c.sendCustomScriptFile(dir_path + "\\localscripts\\gripperactivate.script")

except:
    print("Robot not connected")




class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("UR Python Interface")
        # Move, Getpos, home
        self.ui.move.clicked.connect(self.move)
        self.ui.movel.clicked.connect(self.movel)
        self.ui.getpos.clicked.connect(self.getpos)
        self.ui.home.clicked.connect(self.home)
        # Movement buttons pressed
        self.ui.up.pressed.connect(self.up)
        self.ui.down.pressed.connect(self.down)
        self.ui.left.pressed.connect(self.left)
        self.ui.right.pressed.connect(self.right)
        self.ui.forward.pressed.connect(self.forward)
        self.ui.backward.pressed.connect(self.backward)
        # Rotation buttons
        self.ui.up_2.pressed.connect(self.up_2)
        self.ui.down_2.pressed.connect(self.down_2)
        self.ui.left_2.pressed.connect(self.left_2)
        self.ui.right_2.pressed.connect(self.right_2)
        self.ui.forward_2.pressed.connect(self.forward_2)
        self.ui.backward_2.pressed.connect(self.backward_2)
        # Movement buttons released
        self.ui.up.released.connect(self.released)
        self.ui.down.released.connect(self.released)
        self.ui.left.released.connect(self.released)
        self.ui.right.released.connect(self.released)
        self.ui.forward.released.connect(self.released)
        self.ui.backward.released.connect(self.released)
        # Rotation release
        self.ui.up_2.released.connect(self.released)
        self.ui.down_2.released.connect(self.released)
        self.ui.left_2.released.connect(self.released)
        self.ui.right_2.released.connect(self.released)
        self.ui.forward_2.released.connect(self.released)
        self.ui.backward_2.released.connect(self.released)
        # Gripper
        self.ui.activategripper.clicked.connect(self.activategripper)
        self.ui.opengripper.released.connect(self.opengripper)
        self.ui.closegripper.released.connect(self.closegripper)
        # Slider
        self.ui.slider.sliderMoved.connect(self.slider)
        self.ui.slider.setSliderPosition(99)

        # Local script
        self.ui.uploadscript.clicked.connect(self.uploadscript)
        # Copy position
        self.ui.copy.clicked.connect(self.copy)
        # Freedrive
        self.ui.Freedrive.clicked.connect(self.Freedrive)
        self.ui.Endfreedrive.clicked.connect(self.Endfreedrive)
        # Unlock protective stop
        self.ui.unlockprotectivestop.clicked.connect(self.unlockprotectivestop)

    # Move, home, getpos
    def move(self):
        k = self.ui.textEdit.toPlainText()
        k = ast.literal_eval(k)
        rtde_c.moveJ(k)
    def movel(self):
        k = self.ui.textEdit.toPlainText()
        k = ast.literal_eval(k)
        rtde_c.moveL_FK(k)
    def getpos(self):
        global pos
        pos = str((rtde_r.getActualQ())) ##Gets joint positions
        self.ui.textEdit.setText(pos)

    def unlockprotectivestop(self):
        rtde_c.disconnect()
        rtde_c.reconnect()
        print(rtde_c.getRobotStatus())

    def slider(self):
        scale = self.ui.slider.value() / 33
    def home(self):
        scale = self.ui.slider.value() / 5
        rtde_c.moveJ([3.535665273666382, -1.1158512395671387, 0.7795198599444788, -1.2353530687144776, -1.5640376249896448, 3.507690191268921],speed*scale)

    # Movement buttons
    def up(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, 0, speed * scale, 0, 0, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def down(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, 0, -speed * scale, 0, 0, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def left(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, -speed * scale, 0, 0, 0, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def right(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, speed * scale, 0, 0, 0, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def forward(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([-speed * scale, 0, 0, 0, 0, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def backward(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([speed * scale, 0, 0, 0, 0, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def released(self):
        rtde_c.jogStop()
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    # Orientation
    def up_2(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, 0, 0, 0, 0, speed * scale])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def down_2(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, 0, 0, 0, 0, -speed * scale])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def left_2(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, 0, 0, speed * scale, 0, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def right_2(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, 0, 0, -speed * scale, 0, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def forward_2(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, 0, 0, 0, -speed * scale, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    def backward_2(self):
        scale = self.ui.slider.value() / 33
        rtde_c.jogStart([0, 0, 0, 0, speed * scale, 0])
        if (rtde_c.getRobotStatus() == 1):
            pyautogui.alert("Singularity condition - Unlock protective stop to continue using the robot.")
    # Gripper
    def activategripper(self):
        global gripper
        rtde_c.sendCustomScriptFile(dir_path + "\\localscripts\\gripperactivate.script")
    def opengripper(self):
        global gripper
        rtde_c.sendCustomScriptFile(dir_path + "\\localscripts\\gripperopen.script")
    def closegripper(self):
        global gripper
        rtde_c.sendCustomScriptFile(dir_path + "\\localscripts\\gripperclose.script")
    # Slider

    # Upload local script
    def uploadscript(self):
        from tkinter import Tk  # from tkinter import Tk for Python 3.x
        from tkinter.filedialog import askopenfilename
        Tk().withdraw()  # suppress tkinter gui
        filename = askopenfilename()

        if filename != '':
            rtde_c.sendCustomScriptFile(filename)
        else:
            print("No file was chosen")
    # Copy position to clipboard
    def copy(self):
        global pos
        pyperclip.copy(pos)

    def Freedrive(self):
        rtde_c.teachMode()

        buttons_to_disable = [self.ui.up, self.ui.down, self.ui.left, self.ui.right, self.ui.forward, self.ui.backward, self.ui.left_2, self.ui.right_2, self.ui.forward_2, self.ui.backward_2, self.ui.up_2, self.ui.down_2, self.ui.uploadscript, self.ui.opengripper, self.ui.closegripper, self.ui.activategripper, self.ui.movel, self.ui.move, self.ui.home]
        for button in buttons_to_disable:
            button.setEnabled(False)  # Disable each button in the list

    def Endfreedrive(self):
        rtde_c.endTeachMode()
        buttons_to_enable = [self.ui.up, self.ui.down, self.ui.left, self.ui.right, self.ui.forward, self.ui.backward, self.ui.left_2, self.ui.right_2, self.ui.forward_2, self.ui.backward_2, self.ui.up_2, self.ui.down_2, self.ui.uploadscript, self.ui.opengripper, self.ui.closegripper, self.ui.activategripper, self.ui.movel, self.ui.move, self.ui.home]
        for button in buttons_to_enable:
            button.setEnabled(True)  # Disable each button in the list

    def dig0pulse(self):
        rtde_io_.setStandardDigitalOut(0,1)
        time.sleep(0.5)
        rtde_io_.setStandardDigitalOut(0,0)

    def dig1pulse(self):
        rtde_io_.setStandardDigitalOut(1,1)
        time.sleep(0.5)
        rtde_io_.setStandardDigitalOut(1,0)

    def dig2on(self):
        rtde_io_.setStandardDigitalOut(2,1)

    def dig2off(self):
        rtde_io_.setStandardDigitalOut(2,0)


def app_create():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    # app.setWindowIcon(QtGui.QIcon("Path"))
    win = my_app()
    win.show()
    sys.exit(app.exec_())


print(dir_path)
app_create()


