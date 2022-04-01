from os import listdir
from os.path import join
from win32com.client import Dispatch
import getpass


#通过腾讯会议图标，获得腾讯会议exe文件地址
def address():
    user_name = getpass.getuser()  # 获取当前用户名
    directory = "C:\\Users\\" + user_name + "\\Desktop"

    shell = Dispatch('wScript.shell')
    address = "C:\\软件\腾讯会议\\WeMeet\\wemeetapp.exe"

    for fn in listdir(directory):
        if fn.endswith('.lnk'):
            link = join(directory, fn)
            if link.find("腾讯会议") != -1:
                address = shell.CreateShortCut(link).Targetpath


    return address






