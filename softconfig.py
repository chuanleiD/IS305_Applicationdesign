import get_appaddress


# 获取配置信息
def configuration_information():
    mylist = []
    with open("配置文件\\config.txt", encoding='utf-8') as read_file:  # 打开文件
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


# 标注课程已写入
def write():
    mylist = ""
    with open("配置文件\\config.txt", encoding='utf-8') as read_file:  # 打开文件
        for line in read_file:
            mylist += line
    read_file.close()

    mylist += ("\n" + "课程状态：已写入")
    with open("配置文件\\config.txt", "w", encoding='utf-8') as f:
        f.write(mylist)  # 自带文件关闭功能，不需要再写f.close()


# app_address 数据初始化
def config_initialization():
    mylist = ""
    [app_address, result] = get_appaddress.address()

    with open("配置文件\\config.txt", encoding='utf-8') as read_file:  # 打开文件
        for line in read_file:
            if line.find("腾讯会议exe路径") != -1 and len(line) < 13:
                line = "腾讯会议exe路径：" + app_address + "\n"
            mylist += line
    read_file.close()

    with open("配置文件\\config.txt", "w", encoding='utf-8') as f:
        f.write(mylist)  # 自带文件关闭功能，不需要再写f.close()

    return result



def update_configuration(new_config):
    college_start = new_config[0]
    app_address = new_config[1]
    wait_time = str(new_config[2])

    mylist = ""

    with open("配置文件\\config.txt", encoding='utf-8') as read_file:  # 打开文件
        for line in read_file:
            if line.find("腾讯会议exe路径") != -1:
                line = "腾讯会议exe路径：" + app_address + "\n"
            elif line.find("开学日期") != -1:
                line = "开学日期：" + college_start + "\n"
            elif line.find("腾讯会议打开时间") != -1:
                line = "腾讯会议打开时间：" + wait_time + "\n"
            mylist += line
    read_file.close()

    with open("配置文件\\config.txt", "w", encoding='utf-8') as f:
        f.write(mylist)  # 自带文件关闭功能，不需要再写f.close()



def first_configuration():
    result = 0

    with open("配置文件\\config.txt", encoding='utf-8') as read_file:  # 打开文件
        for line in read_file:
            if line.find("腾讯会议exe路径") != -1:
                if len(line) < 13:
                    result = 1
    read_file.close()

    return result

