import database


def readtxt(filename="course_txt\\course.txt"):

    course_list = []
    course_num = -1
    week = "星期一"
    time = "1-2"
    with open(filename, encoding='utf-8') as read_file:  # 打开文件
        for line in read_file:
            line = line.strip('\n')
            if len(line) != 0:
                if line.find("星期") != -1 and len(line) < 5:
                    if line == "星期一":
                        mystr = "1"
                    if line == "星期二":
                        mystr = "2"
                    if line == "星期三":
                        mystr = "3"
                    if line == "星期四":
                        mystr = "4"
                    if line == "星期五":
                        mystr = "5"
                    week = mystr
                if line.find("-") != -1 and len(line) < 10:
                    time = line
                if line.find("◇") != -1:
                    course_list.append(week + "@" + time + "@" + line)
                    course_num += 1
                if line.find("周数") != -1:
                    course_list[course_num] = course_list[course_num] + line
    read_file.close()

    return course_list

#print(readtxt())

def get_db(filename="course_txt\\course.txt"):
    mylist = readtxt(filename)
    data = []
    for course in mylist:
        weekday = int(course[0])
        start_time = int(course[2:course.find("-")])
        end_time = int(course[course.find("-")+1:course.find("\t")])

        c1 = course.find("@")
        course_name = course[course.find("@", c1+1)+1:course.find("◇")]

        s1 = course.find("周数")
        s2 = course.find("-", s1, s1+6)
        s3 = course.find("周", s1+2, s1+8)

        if s2 != -1:
            start_week = int(course[s1+3:s2])
            end_week = int(course[s2+1:s3])
        else:
            start_week = int(course[s1+3:s3])
            end_week = int(course[s1 + 3:s3])

        meeting_number = course[course.find("腾讯会议号：")+6:course.find("；密码：")]
        meeting_password = course[course.find("密码：")+3:course.find("课程学时组成")-1]

        if course[course.find("校区：闵行")-3] == "单":
            single_or_double_week = 1
        elif course[course.find("校区：闵行")-3] == "双":
            single_or_double_week = 2
        else:
            single_or_double_week = 0

        a = (course_name, start_time, end_time, weekday, start_week, end_week, meeting_number, meeting_password, single_or_double_week)
        #print(a)
        data.append(a)
    database.insert(data)
    #insert([("操作系统", 1, 1, 9, 16, "576409879", "2932", 0),("数据挖掘", 3, 1, 9, 16, "149716380", "8419", 0)])

