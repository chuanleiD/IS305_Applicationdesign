import os.path
import time
import easygui
import softconfig
import online_course
import threading
from Background_Start import background_start

global run_symbol

def mybegin():
    ping_or_scan = easygui.buttonbox("请选择您要进行的操作", "腾讯会议助手_by_Dcl", image="pic/pic0.gif", choices=["立即打开网课", "添加会议", "后台运行", "初始配置", "退出"])

    if ping_or_scan == '退出':
        return
    else:
        if ping_or_scan == '立即打开网课':
            size = os.path.getsize("配置文件\\course.txt")
            if size == 0:
                os.startfile("配置文件\\course.txt")
                result = write_course()
                if result:
                    online_course.online_course_now()
                    return
                else:
                    return
            else:
                online_course.online_course_now()
                return

        elif ping_or_scan == '添加会议':
            add_meeting()
        elif ping_or_scan == '后台运行':
            background_operation()
        elif ping_or_scan == '初始配置':
            config_set()
    return


def write_course():
    ping_or_scan = easygui.buttonbox("是否已经输入课程信息", "腾讯会议助手_by_Dcl", image="pic/pic1.gif",
                                     choices=["是的，我已输入", "退出"])
    if ping_or_scan == '退出':
        return 0
    elif ping_or_scan == "是的，我已输入":
        return 1

    return 0


def add_meeting():
    filename = "配置文件\\course.txt"
    clear = open(filename, 'w').close()
    os.startfile(filename)
    ping_or_scan = easygui.buttonbox("是否已经输入会议信息", "腾讯会议助手_by_Dcl", image="pic/pic2.gif",
                                     choices=["是的，我已输入", "退出"])
    if ping_or_scan == '退出':
        return 0
    elif ping_or_scan == "是的，我已输入":

        return 1
    return 0



def background_operation():
    global run_symbol
    run_symbol = 0

    wait_threads = []  # 用来存放执行read函数线程的列表
    run_threads = []  # 用来存放执行write函数线程的列表

    for i in range(1, 2):  # 创建1个线程用于read()，并添加到read_threads列表
        t = threading.Thread(target=background_wait)  # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开))
        wait_threads.append(t)

    for i in range(1, 2):  # 创建1个线程执行write()，并添加到write_threads列表
        t = threading.Thread(target=background_run)  # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开))
        run_threads.append(t)

    for i in range(0, 1):  # 启动存放在read_threads和write_threads列表中的线程
        wait_threads[i].start()
        run_threads[i].start()

    return


def background_wait():
    global run_symbol
    ping_or_scan = easygui.buttonbox("正在后台运行中", "腾讯会议助手_by_Dcl", image="pic/pic3.gif", choices=["退出"])
    if ping_or_scan == '退出':
        run_symbol = 1
        time.sleep(1)
        return
    return


def background_run():
    global run_symbol
    num = 0

    while run_symbol != 1:
        num += 1
        print(run_symbol, num)
        background_start()
        for i in range(0, 60, 1):
            time.sleep(5)
            if run_symbol == 1:
                return
    return


def config_set():
    config = softconfig.configuration_information()

    college_start = config[0]
    app_address = config[2]
    wait_time = str(config[3])

    list1 = ["开学时间", "腾讯会议EXE地址", "打开EXE的反应时间"]
    list2 = [college_start, app_address, wait_time]
    new_config = easygui.multenterbox(msg="请修改您的设置，格式请保持一致", title="Config设置修改界面", fields=list1, values=list2, callback=None, run=True)

    if (college_start!=new_config[0] or app_address!=new_config[1] or wait_time!=new_config[2]):
        softconfig.update_configuration(new_config)

    mybegin()
    return



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    panduan = softconfig.first_configuration()
    if panduan:
        result = softconfig.config_initialization()
        if result == 0:
            ping_or_scan = easygui.buttonbox("请为桌面添加腾讯会议快捷方式\n或手动在初始配置界面添加腾讯会议链接", "腾讯会议助手_by_Dcl", choices=["好的，我已知晓"])

    mybegin()



