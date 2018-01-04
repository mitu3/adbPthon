import device
from command import *



def main():
    device.dump_device_info()

    installapp('sss.apk')
    keyevent(3)
    huadong('100 500 200 1000')
    screencap('sdf.png','C:\\Users\Administrator\Desktop')




main()