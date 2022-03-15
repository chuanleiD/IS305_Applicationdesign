import os
import pyautogui
import time
from cv2 import imread,matchTemplate,TM_SQDIFF,minMaxLoc,rectangle,resize,imshow,waitKey,destroyAllWindows,INTER_NEAREST



def ifstart():
    tempFile = "picture\\begin.png"
    pyautogui.screenshot('big.png')
    gray = imread("big.png", 0)
    img_template = imread(tempFile, 0)

    os.remove("big.png")



def imgAutoCick(tempFile, whatDo, debug=False):
    pyautogui.screenshot('big.png')
    gray = imread("big.png", 0)
    img_template = imread(tempFile, 0)
    w, h = img_template.shape[::-1]
    res = matchTemplate(gray, img_template, TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = minMaxLoc(res)
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    pyautogui.moveTo(top + h / 2, left + w / 2, duration=0.2)
    whatDo(x)

    if debug:
        img = imread("big.png", 1)
        rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
        img = resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=INTER_NEAREST)
        imshow("processed", img)
        waitKey(0)
        destroyAllWindows()
    os.remove("big.png")


def signIn(meeting_id, meeting_key, wait_time=5, app_address="C:\软件\腾讯会议\WeMeet\wemeetapp.exe"):
    '''
    本模块主要引入腾讯会议号，进入会议之中；
    '''
    # 调用cmd命令打开腾讯会议
    os.startfile(app_address)
    time.sleep(wait_time)  # 等待启动
    imgAutoCick("picture\\joinbtn.png", pyautogui.click, False)
    time.sleep(0.5)  # 截取需要点击的地方的小

    imgAutoCick("picture\\meeting_id.png", pyautogui.click, False)
    pyautogui.write(meeting_id)
    time.sleep(0.5)
    imgAutoCick("picture\\final.png", pyautogui.click, False)
    time.sleep(0.5)

    imgAutoCick("picture\\key.png", pyautogui.click, False)
    pyautogui.write(meeting_key)
    time.sleep(0.5)
    imgAutoCick("picture\\final2.png", pyautogui.click, False)
    time.sleep(0.5)


#signIn("648289912", "6080")





