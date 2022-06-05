'''
程序运行主文件
前端操作为主
'''
#----------------------------------------------------------------------------------------
import os.path
import time
import easygui
import softconfig
import online_course
import threading
from Background_Start import background_start
#----------------------------------------------------------------------------------------

# 全局变量用于后台运行时的控制
global run_symbol


#pyinstaller -w -i E:\Python_projects\Applicationdesign\配置文件\logo3.ico -n 网课助手 E:\Python_projects\Applicationdesign\Front_end_design.py


#----------------------------------------------------------------------------------------
# 程序主界面，用于选择几种不同的操作
def mybegin():
    ping_or_scan = easygui.buttonbox("请选择您要进行的操作", "腾讯会议助手_by_Dcl", image="pic/pic0.gif", choices=["立即打开网课", "添加会议", "后台运行", "初始配置", "退出"])

    if ping_or_scan == '退出':
        return
    else:
        if ping_or_scan == '立即打开网课':
            # 判断用户是否写入了他的课程
            size = os.path.getsize("配置文件\\course.txt")
            if size == 0:
                # 打开课程配置文件供用户写入
                os.startfile("配置文件\\course.txt")
                # 如果没有，则启动“写入课程”模块
                result = write_course()
                # 如果用户成功添加，则继续运行。否则退出程序
                if result:
                    online_course.online_course_now()
                    return
                else:
                    return
            else:
                # 正常运行
                online_course.online_course_now()
                return
        # 启动“添加会议”窗口
        elif ping_or_scan == '添加会议':
            add_meeting()
        # 启动“后台运行”窗口
        elif ping_or_scan == '后台运行':
            background_operation()
        # 启动“初始配置”窗口
        elif ping_or_scan == '初始配置':
            config_set()
    return

'''
“写入课程”模块
Bool result 
1为成功，0为失败
'''
def write_course():
    ping_or_scan = easygui.buttonbox("是否已经输入课程信息", "腾讯会议助手_by_Dcl", image="pic/pic1.gif",
                                     choices=["是的，我已输入", "退出"])
    if ping_or_scan == '退出':
        return 0
    elif ping_or_scan == "是的，我已输入":
        return 1

    return 0
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
'''
“写入课程”模块
Bool result 
1为成功，0为失败
'''
def add_meeting():
    # 文件写入的地址
    filename = "配置文件\\meeting.txt"
    # 首先清空其中的内容
    clear = open(filename, 'w').close()
    # 打开该文件，并创建交互界面
    os.startfile(filename)
    ping_or_scan = easygui.buttonbox("是否已经输入会议信息", "腾讯会议助手_by_Dcl", image="pic/pic2.gif",
                                     choices=["是的，我已输入", "退出"])
    if ping_or_scan == '退出':
        return 0
    elif ping_or_scan == "是的，我已输入":

        return 1
    return 0
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# 用于实现“后台运行”功能
def background_operation():
    global run_symbol
    # 全局变量run_symbol置为0
    run_symbol = 0

    # 双线程，一个线程循环判断是否打开会议，一个线程用于交互控制，关闭程序

    # 用来存放执行read函数线程的列表
    wait_threads = []
    # 用来存放执行write函数线程的列表
    run_threads = []

    # 创建1个线程用于background_wait()，并添加到wait_threads列表
    for i in range(1, 2):
        # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开))
        t = threading.Thread(target=background_wait)
        wait_threads.append(t)

    # 创建1个线程执行background_run()，并添加到run_threads列表
    for i in range(1, 2):
        t = threading.Thread(target=background_run)
        run_threads.append(t)

    # 启动存放在wait_threads和run_threads列表中的线程
    for i in range(0, 1):
        wait_threads[i].start()
        run_threads[i].start()

    return


def background_wait():
    global run_symbol
    # 交互界面，如果关闭，全局变量run_symbol置为1
    ping_or_scan = easygui.buttonbox("正在后台运行中", "腾讯会议助手_by_Dcl", image="pic/pic3.gif", choices=["退出"])
    if ping_or_scan == '退出':
        run_symbol = 1
        time.sleep(1)
        return
    return


def background_run():
    global run_symbol
    # 如果全局变量run_symbol为1，停止运行
    num = 0

    while run_symbol != 1:
        num += 1
        print(run_symbol, num)
        # 5分钟执行一次
        background_start()
        # 5分钟拆分，5秒判断一下是否关闭
        for i in range(0, 60, 1):
            time.sleep(5)
            if run_symbol == 1:
                return
    return
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# 初始配置设置功能，用于改变：开学时间、腾讯会议exe地址、打开会议等待时间
def config_set():
    # 读取已有的配置信息
    config = softconfig.configuration_information()

    college_start = config[0]
    app_address = config[2]
    wait_time = str(config[3])

    # 交互界面
    list1 = ["开学时间", "腾讯会议EXE地址", "打开EXE的反应时间"]
    list2 = [college_start, app_address, wait_time]
    new_config = easygui.multenterbox(msg="请修改您的设置，格式请保持一致", title="Config设置修改界面", fields=list1, values=list2, callback=None, run=True)

    # 如果用户进行了修改，则重新写入配置
    if (college_start!=new_config[0] or app_address!=new_config[1] or wait_time!=new_config[2]):
        softconfig.update_configuration(new_config)

    # 重回主界面
    mybegin()
    return



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    # 判断是否第一次打开程序
    panduan = softconfig.first_configuration()
    if panduan:
        # 如果第一次打开，桌面没有腾讯会议图标，则弹出交互界面请用户自己配置腾讯会议地址
        result = softconfig.config_initialization()
        if result == 0:
            ping_or_scan = easygui.buttonbox("请为桌面添加腾讯会议快捷方式\n或手动在初始配置界面添加腾讯会议链接", "腾讯会议助手_by_Dcl", choices=["好的，我已知晓"])
    # 进入主界面
    mybegin()



