from softconfig import configuration_information
from softconfig import write
from txtreader import get_db
from decidecourse import decide_course
from autoclick import signIn
#打包命令 pyinstaller -w -i E:\Python_projects\应用软件课程设计\logo3.ico -n 网课助手 E:\Python_projects\应用软件课程设计\main.py


def online_course_now():
    config = configuration_information()

    college_start = config[0]
    filename = config[1]
    app_address = config[2]
    wait_time = config[3]
    if_read = config[4]

    if if_read == 0:
        get_db(filename)
        write()

    mylist = decide_course(college_start)
    meeting_id = mylist[7]
    meeting_key = mylist[8]
    signIn(meeting_id, meeting_key, wait_time, app_address)


#online_course()