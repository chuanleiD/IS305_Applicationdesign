import pyautogui
import cv2
import os


tempFile = "picture\\begin.png"
pyautogui.screenshot('big.png')
gray = cv2.imread("big.png", 0)
img_template = cv2.imread(tempFile, 0)
res = cv2.matchTemplate(gray, img_template, cv2.TM_SQDIFF)
print(res)
os.remove("big.png")




