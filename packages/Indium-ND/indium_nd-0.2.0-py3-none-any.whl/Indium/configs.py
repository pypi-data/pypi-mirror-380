import ctypes, pyautogui, time
import os, shutil

def MoveFile(src, dst):
    shutil.move(src, dst)

def CopyFile(src, dst):
    shutil.copy(src, dst)

def DeleteFile(path):
    os.remove(path)

def RenameFile(src, new_name):
    dst = os.path.join(os.path.dirname(src), new_name)
    os.rename(src, dst)

def FullScreenMode():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 3)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(0.5)  # wait a bit
    pyautogui.hotkey('alt', 'enter')  # trigger true fullscreen
