import os.path

import easygui
import softconfig
import online_course

def mybegin():
    ping_or_scan = easygui.buttonbox("请选择您要进行的操作", "腾讯会议助手_by_Dcl", image="pic/pic0.gif", choices=["立即打开网课", "后台运行", "初始配置", "退出"])

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
                else:
                    return
            else:
                online_course.online_course_now()

        elif ping_or_scan == '后台运行':
            background_operation()
        elif ping_or_scan == '初始配置':
            config_set()
    return



def write_course():
    ping_or_scan = easygui.buttonbox("是否已经输入课程信息", "腾讯会议助手_by_Dcl", image="pic/pic0.gif",
                                     choices=["是的，我已输入", "退出"])
    if ping_or_scan == '退出':
        return 0
    elif ping_or_scan == "是的，我已输入":
        return 1

    return 0



def background_operation():
    ping_or_scan = easygui.buttonbox("正在后台运行中", "腾讯会议助手_by_Dcl", image="pic/pic1.gif", choices=["网课", "会议", "退出"])

    if ping_or_scan == '退出':
        return
    '''
    else:
        if ping_or_scan == '网课':
            online_course.online_course()
        if ping_or_scan == '会议':
            meeting_choose()
    return
    '''


def config_set():
    config = softconfig.configuration_information()

    college_start = config[0]
    app_address = config[2]
    wait_time = str(config[3])

    mystr = "开学时间："+college_start+"\n"+"腾讯会议："+app_address+"\n"+"开机等待时间："+wait_time+"\n"
    ping_or_scan = easygui.buttonbox(mystr, "腾讯会议助手_by_Dcl", choices=["返回"])

    if ping_or_scan == '返回':
        mybegin()


softconfig.config_initialization()
mybegin()


