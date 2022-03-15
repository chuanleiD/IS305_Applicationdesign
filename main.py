import decidecourse
import txtreader
import autoclick

def configuration_information():
    mylist = []
    with open("config.txt", encoding='utf-8') as read_file:  # 打开文件
        for line in read_file:
            line = line.strip('\n')
            a = line.find("：")
            mylist.append(line[a+1:])
    read_file.close()

    college_start = mylist[0]
    if_read = int(mylist[1])
    filename = mylist[2]
    app_address = mylist[3]
    wait_time = int(mylist[4])

    b = (college_start, if_read, filename, app_address, wait_time)
    return b


if __name__ == '__main__':
    config = configuration_information()
    #('20220214', 1, 'course_txt\\course.txt', 'C:\\软件\\腾讯会议\\WeMeet\\wemeetapp.exe', 5)

    college_start = config[0]
    if_read = config[1]
    filename = config[2]
    app_address = config[3]
    wait_time = config[4]

    if if_read == 0:
        txtreader.get_db(filename)

    mylist = decidecourse.decide_course(college_start)
    meeting_id = mylist[7]
    meeting_key = mylist[8]
    autoclick.signIn(meeting_id, meeting_key, wait_time, app_address)


