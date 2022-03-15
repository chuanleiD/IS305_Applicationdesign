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

    if len(mylist) <= 4:
        ifread = 0
    else:
        ifread = 1

    b = (college_start, filename, app_address, wait_time, ifread)
    return b


def write(app_address):
    mylist = ""
    with open("config.txt", encoding='utf-8') as read_file:  # 打开文件
        for line in read_file:
            if line.find("腾讯会议exe路径") != -1:
                line = "腾讯会议exe路径：" + app_address + "\n"
            mylist += line
    read_file.close()

    mylist += ("\n" + "课程状态：已写入")
    with open("config.txt", "w", encoding='utf-8') as f:
        f.write(mylist)  # 自带文件关闭功能，不需要再写f.close()




