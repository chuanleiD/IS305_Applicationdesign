import decidecourse
import txtreader
import autoclick





if __name__ == '__main__':
    #txtreader.get_db()
    mylist = decidecourse.decide_course()
    meeting_id = mylist[7]
    meeting_key = mylist[8]
    autoclick.signIn(meeting_id, meeting_key)


