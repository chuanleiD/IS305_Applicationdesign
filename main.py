import decidecourse
import txtreader
import autoclick
import softconfig
import get_appaddress
#打包命令 pyinstaller -w -i E:\Python_projects\应用软件课程设计\logo3.ico -n 网课助手 E:\Python_projects\应用软件课程设计\main.py


if __name__ == '__main__':

    config = softconfig.configuration_information()

    college_start = config[0]
    filename = config[1]
    app_address = config[2]
    wait_time = config[3]
    if_read = config[4]

    if if_read == 0:
        address = get_appaddress.address()
        txtreader.get_db(filename)
        softconfig.write(address)
        app_address = address

    mylist = decidecourse.decide_course(college_start)
    meeting_id = mylist[7]
    meeting_key = mylist[8]
    autoclick.signIn(meeting_id, meeting_key, wait_time, app_address)


