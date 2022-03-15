import decidecourse
import txtreader
import autoclick

#打包命令 pyinstaller -w -i E:\Python_projects\应用软件课程设计\logo3.ico -n 网课助手 E:\Python_projects\应用软件课程设计\main.py
def configuration_information():
    mylist = []
    with open("config.txt", encoding='utf-8') as read_file:  # 打开文件
        for line in read_file:
            line = line.strip('\n')
            a = line.find("：")
            mylist.append(line[a+1:])
    read_file.close()

    college_start = mylist[0]
    filename = mylist[1]
    app_address = mylist[2]
    wait_time = int(mylist[3])

    if len(mylist) == 4:
        ifread = 0
    elif len(mylist) > 4:
        ifread = 1

    b = (college_start, filename, app_address, wait_time, ifread)
    return b


if __name__ == '__main__':

    config = configuration_information()
    #('20220214', 'course_txt\\course.txt', 'C:\\软件\\腾讯会议\\WeMeet\\wemeetapp.exe', 5, 1)

    college_start = config[0]
    filename = config[1]
    app_address = config[2]
    wait_time = config[3]
    if_read = config[4]

    if if_read == 0:
        txtreader.get_db(filename)
        mylist = ""
        with open("config.txt", encoding='utf-8') as read_file:  # 打开文件
            for line in read_file:
                mylist += line
        read_file.close()

        mylist += ("\n"+"课程状态：已写入")
        with open("config.txt", "w", encoding='utf-8') as f:
            f.write(mylist)  # 自带文件关闭功能，不需要再写f.close()


    mylist = decidecourse.decide_course(college_start)
    meeting_id = mylist[7]
    meeting_key = mylist[8]
    autoclick.signIn(meeting_id, meeting_key, wait_time, app_address)


