import os
import glob


def get_devices():
    devices = os.popen("adb devices").read()
    devices_list = devices.split()
    num = 0
    for i in devices_list:
        if i == "devices":
            num += 1
    return devices_list


# def get_IMEI():
#     devices_list = get_devices()
#     for i in devices_list[4:-1]:
#         # print("设备码：", i)
#         devices_version = os.popen("adb -s " + i + " shell getprop ro.build.version.release").read()
#         devices_version_num = devices_version.split(".")
#         devices_version_num1 = int(devices_version_num[0])


def install_app():
    devices_list = get_devices()
    for i in devices_list[4:-1]:
        # print("设备码：", i)
        apk_file = glob.glob("*.apk")
        if len(apk_file) >= 1:
            for apk in glob.glob("*.apk"):
                print("apk:", apk)
                os.system("adb -s " + i + " install -r " + apk)
                print("安装",apk,"完成！")
        else:
            print("没找到apk")
            os.system("pause")


# def chcek():
#     devices_list = get_devices()
#     for i in devices_list[4:-1]:
#         devices_package = os.popen("adb -s  " + i + " shell pm list package -3").read()
#         print("已安装的非系统包包名：", devices_package)
#         if "应用包名" in devices_package:
#             os.system("adb -s " + i + " shell am start -n ........Activity")
#             print("应用已经安装")
#             os.system("pause")
#         else:
#             print(None)
#             os.system("pause")


if __name__ == '__main__':
    get_devices()
    install_app()
