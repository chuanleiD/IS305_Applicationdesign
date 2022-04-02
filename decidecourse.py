import database
import gettime


# 课程号映射到分钟型时间
def course_time(a):
    b = [0, 480, 535, 600, 655, 720, 775, 840, 895, 960, 1015, 1080, 1135, 1175, 1220, 1275]
    return b[a]


# 决定课程打开哪个
def decide_course(college_start='20220214'):
    mylist = database.read_db()
    week_now = gettime.get_week(college_start)
    localtime = gettime.get_time()
    weekday = gettime.get_weekday()

    list2 = []
    mycourse = mylist[0]
    for course in mylist:
        if course[4] == weekday and week_now >= course[5] and week_now <= course[6]:
            if course[9] == 0 or (course[9] == 1 and week_now % 2 == 1) or (course[9] == 2 and week_now % 2 == 0):
                list2.append(course)

    #print(list2)
    if len(list2) > 0:
        mycourse = list2[0]
    else:
        mycourse = mylist[0]


    for i in range(0, len(list2), 1):
        course = list2[i]
        if i == 0 and localtime < course_time(course[3]):
            mycourse = course
            break
        elif i == len(list2) - 1:
            mycourse = list2[i]
            break
        elif localtime > course_time(course[3]) and (i <= len(list2)-2 and localtime < course_time(list2[i+1][3])):
            mycourse = list2[i+1]
            break

    return mycourse

#a = (course_name, start_time, end_time, weekday, start_week, end_week, meeting_number, meeting_password, single_or_double_week)



# 决定会议打开哪个
def decide_background(college_start='20220214', if_read=0):

    result_course = 0
    if ~if_read:
        mylist = database.read_db()
        week_now = gettime.get_week(college_start)
        localtime = gettime.get_time()
        weekday = gettime.get_weekday()

        list2 = []
        mycourse = mylist[0]
        for course in mylist:
            if course[4] == weekday and week_now >= course[5] and week_now <= course[6]:
                if course[9] == 0 or (course[9] == 1 and week_now % 2 == 1) or (course[9] == 2 and week_now % 2 == 0):
                    list2.append(course)

        for i in range(0, len(list2), 1):
            course = list2[i]
            if (course_time(course[3])-localtime) < 5:
                mycourse = course
                result_course = 1


    mylist = database.meeting_read_db()
    result_meeting = 0
    today = gettime.get_day()
    mytime = gettime.get_time()

    mymeeting = mylist[0]
    for meeting in mylist:
        if meeting[2] == today and meeting[1]-mytime < 5:
            mymeeting = meeting
            result_meeting = 1
            break


    result = result_meeting*2 + result_course
    if result_meeting:
        id = mymeeting[3]
        key = mymeeting[4]
    elif result_course:
        id = mycourse[7]
        key = mycourse[8]
    else:
        id = mymeeting[3]
        key = mymeeting[4]

    return [result, id, key]






