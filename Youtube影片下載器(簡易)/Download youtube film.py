#youtube 自己抓影片(沒版權不能抓)
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
from pytube import YouTube
import os


def rbvideo():
    global getvideo
    labelMsg.config(text='')
    getvideo = videorb.get()

def clickDown():
    global getvideo, strftype, listradio
    labelMsg.config(text='')
    if (url.get()==''):
        labelMsg.config(text = '請選擇下載路徑')
        return
    
    if(path.get()==''):
        labelMsg.config(text = '請選擇下載資料夾')
        return
    else:
        pathdir = path.get()
        pathdir = pathdir.replace("\\", "\\\\")
        
    try:
        yt = YouTube(url.get())
        yt.streams.filter(subtype='mp4', res= getvideo, progressive= True).first().download(pathdir)
        labelMsg.config(text ='下載完成!')
    except:
        labelMsg.config(text = '影片無法下載!有可能涉及版權問題，請支持正版!')
        
def select_path():
    path_ = askdirectory()
    path.set(path_)        



win = tk.Tk()
win.geometry('660x280')
win.title('下載Youtube影片(有版權無法下載)')
getvideo = '360p' #影片格式
videorb = tk.StringVar( )#選項按鈕值
url = tk.StringVar() #影片網址值
path = tk.StringVar() #存檔資料夾

label1 = tk.Label(win, text = 'Youtube網址:')
label1.place(x=123, y=30)
entryUrl = tk.Entry(win, textvariable = url)
entryUrl.config(width=45)
entryUrl.place(x=220, y=30)


entryPath = tk.Entry(win, textvariable = path)
entryPath.config(width=45)
entryPath.place(x=220, y=70)
Down_loadpath = tk.Button(win, text = '存檔路徑:', command = select_path)
Down_loadpath.place(x=145, y=67)

btnDown = tk.Button(win, text = '下載影片', command = clickDown)
btnDown.place(x=200, y=110)

rb1 = tk.Radiobutton(win, text = '360, mp4', variable = videorb, value = '360', command = rbvideo)
rb1.place(x=200, y=150)
rb1.select()
rb2 = tk.Radiobutton(win, text ='720p, mp4', variable = videorb, value = '720', command = rbvideo)
rb2.place(x=200, y=180)


labelMsg = tk.Label(win, text='', fg='red')#訊息標籤
labelMsg.place(x=200, y=220)

win.mainloop()




