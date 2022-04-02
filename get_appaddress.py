'''
获取腾讯会议EXE地址
'''

from os import listdir
from os.path import join
from win32com.client import Dispatch
import getpass

#----------------------------------------------------------------------------------------
#通过腾讯会议图标，获得腾讯会议exe文件地址
def address():
    # 获取当前用户名
    user_name = getpass.getuser()
    # 获取桌面位置
    directory = "C:\\Users\\" + user_name + "\\Desktop"

    shell = Dispatch('wScript.shell')
    address = "C:\\软件\\腾讯会议\\WeMeet\\wemeetapp.exe"
    # 找到地址
    result = 0
    for fn in listdir(directory):
        if fn.endswith('.lnk'):
            link = join(directory, fn)
            # 找到腾讯会议快捷方式
            if link.find("腾讯会议") != -1:
                # 找到EXE的位置
                address = shell.CreateShortCut(link).Targetpath
                result = 1

    return [address, result]
#----------------------------------------------------------------------------------------