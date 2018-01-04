import sys
import os

'''
    安装app函数
'''
def installapp(appname):
    cmd ='adb install {}'.format(appname)
    try:
        os.system(cmd)
    except Exception as e:
        return e



'''
    卸载app函数
'''
def uninstallapp(appname):
    cmd ='adb uninstall {}'.format(appname)
    try:
        os.system(cmd)
    except Exception as e:
        return e


'''
0 -->  "KEYCODE_UNKNOWN"		20 -->  "KEYCODE_DPAD_DOWN"		40 -->  "KEYCODE_L"		60 -->  "KEYCODE_SHIFT_RIGHT"		80 -->  "KEYCODE_FOCUS"
1 -->  "KEYCODE_MENU"		    21 -->  "KEYCODE_DPAD_LEFT"		41 -->  "KEYCODE_M"		61 -->  "KEYCODE_TAB"		81 -->  "KEYCODE_PLUS"
2 -->  "KEYCODE_SOFT_RIGHT"		22 -->  "KEYCODE_DPAD_RIGHT"		42 -->  "KEYCODE_N"		62 -->  "KEYCODE_SPACE"		82 -->  "KEYCODE_MENU"
3 -->  "KEYCODE_HOME"		23 -->  "KEYCODE_DPAD_CENTER"		43 -->  "KEYCODE_O"		63 -->  "KEYCODE_SYM"		83 -->  "KEYCODE_NOTIFICATION"
4 -->  "KEYCODE_BACK"		24 -->  "KEYCODE_VOLUME_UP"		44 -->  "KEYCODE_P"		64 -->  "KEYCODE_EXPLORER"		84 -->  "KEYCODE_SEARCH"
5 -->  "KEYCODE_CALL"		25 -->  "KEYCODE_VOLUME_DOWN"		45 -->  "KEYCODE_Q"		65 -->  "KEYCODE_ENVELOPE"		85 -->  "TAG_LAST_KEYCODE"
6 -->  "KEYCODE_ENDCALL"		26 -->  "KEYCODE_POWER"		46 -->  "KEYCODE_R"		66 -->  "KEYCODE_ENTER"		
7 -->  "KEYCODE_0"		27 -->  "KEYCODE_CAMERA"		47 -->  "KEYCODE_S"		67 -->  "KEYCODE_DEL"		
8 -->  "KEYCODE_1"		28 -->  "KEYCODE_CLEAR"		48 -->  "KEYCODE_T"		68 -->  "KEYCODE_GRAVE"		
9 -->  "KEYCODE_2"		29 -->  "KEYCODE_A"		49 -->  "KEYCODE_U"		69 -->  "KEYCODE_MINUS"		
10 -->  "KEYCODE_3"		30 -->  "KEYCODE_B"		50 -->  "KEYCODE_V"		70 -->  "KEYCODE_EQUALS"		
11 -->  "KEYCODE_4"		31 -->  "KEYCODE_C"		51 -->  "KEYCODE_W"		71 -->  "KEYCODE_LEFT_BRACKET"		
12 -->  "KEYCODE_5"		32 -->  "KEYCODE_D"		52 -->  "KEYCODE_X"		72 -->  "KEYCODE_RIGHT_BRACKET"		
13 -->  "KEYCODE_6"		33 -->  "KEYCODE_E"		53 -->  "KEYCODE_Y"		73 -->  "KEYCODE_BACKSLASH"		
14 -->  "KEYCODE_7"		34 -->  "KEYCODE_F"		54 -->  "KEYCODE_Z"		74 -->  "KEYCODE_SEMICOLON"		
15 -->  "KEYCODE_8"		35 -->  "KEYCODE_G"		55 -->  "KEYCODE_COMMA"		75 -->  "KEYCODE_APOSTROPHE"		
16 -->  "KEYCODE_9"		36 -->  "KEYCODE_H"		56 -->  "KEYCODE_PERIOD"		76 -->  "KEYCODE_SLASH"		
17 -->  "KEYCODE_STAR"		37 -->  "KEYCODE_I"		57 -->  "KEYCODE_ALT_LEFT"		77 -->  "KEYCODE_AT"		
18 -->  "KEYCODE_POUND"		38 -->  "KEYCODE_J"		58 -->  "KEYCODE_ALT_RIGHT"		78 -->  "KEYCODE_NUM"		
19 -->  "KEYCODE_DPAD_UP"		39 -->  "KEYCODE_K"		59 -->  "KEYCODE_SHIFT_LEFT"		79 -->  "KEYCODE_HEADSETHOOK"		
'''

def keyevent(keynum):
    cmd = 'adb shell input keyevent {} '.format(keynum)

    try:
        resule = os.popen(cmd).read()
    except Exception as e:
        return e
    return resule



'''
    点击模拟操作函数  xy{   x1 y1     (str)}

'''

def stp(xy):
    cmd = 'adb shell input stp  {} '.format(xy)
    try:
        resule = os.popen(cmd).read()
    except Exception as e:
        return e
    return resule


'''
    滑动模拟操作函数  xyt{   x1 y1  x2 y2  time    (str)}

'''

def swipe(xyt):
    cmd = 'adb shell input swipe  {} '.format(xyt)
    try:
        resule = os.popen(cmd).read()
    except Exception as e:
        return e
    return resule




'''
    输入文本函数  strvalue 文本数据   （str）

'''

def input(strvalue):
    cmd = 'adb shell input text  {} '.format(strvalue)



    try:
        resule = os.popen(cmd).read()
    except Exception as e:
        return e

    return resule


'''
    截屏函数  name  (str) 名称   dizhi  (str) 是路径

'''

def screencap(name,*dizhi):

    cmd1 = "adb shell screencap -p /sdcard/{}".format(name)
    cmd2 = "adb pull /sdcard/{} {}".format(name,*dizhi)
    cmd3 = "adb shell rm /sdcard/{}".format(name)

    try:
        resule1 = os.popen(cmd1).read()
        resule2 = os.popen(cmd2).read()
        resule3 = os.popen(cmd3).read()

    except Exception as e:
        return e

    return resule1,resule2,resule3


'''
    录屏函数  name  (str) 名称   dizhi  (str) 是路径

'''

def screencord(name,*dizhi):

    cmd1 = "adb shell screencord  /sdcard/{}".format(name)
    cmd2 = "adb pull /sdcard/{} {}".format(name,*dizhi)
    cmd3 = "adb shell rm /sdcard/{}".format(name)

    try:
        resule1 = os.popen(cmd1).read()
        resule2 = os.popen(cmd2).read()
        resule3 = os.popen(cmd3).read()

    except Exception as e:
        return e

    return resule1,resule2,resule3