import os
import sys


def dump_device_info():
    '''
    显示设备信息
    '''
    size_str = os.popen('adb shell wm size').read()
    device_str = os.popen('adb shell getprop ro.product.model').read()
    density_str = os.popen('adb shell wm density').read()
    print("""**********
Screen: {size}
Density: {dpi}
DeviceType: {type}
OS: {os}
Python: {python}
**********""".format(
        size=size_str.strip(),
        type=device_str.strip(),
        dpi=density_str.strip(),
        os=sys.platform,
        python=sys.version
    ))