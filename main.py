import decidecourse
import txtreader






if __name__ == '__main__':
    #txtreader.get_db()
    mylist = decidecourse.decide_course()
    print("会议号：", mylist[7])
    print("密码：", mylist[8])


