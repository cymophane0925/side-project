#BMI計算器

import tkinter as tk

def bmi_count():    

    if height_entry.get() == '' and weight_entry.get() =='':
        rt.set('請輸入數值')
    else:
        hts = float(height_entry.get()) / 100
        wts = float(weight_entry.get())
        bmi_value =float(wts / (hts**2))
        rt.set('您的身高(height): {} m\n 您的體重(weight): {} Kg\n您的BMI指數為:{:.2f} \n{}'.format(hts, wts, bmi_value, bmi_check(bmi_value)))
def bmi_check(bmi_value):
    k = bmi_value
    if k < 18.5 :
        return '體重過輕，多吃一點'
    elif 18.5 <= k and k < 24:
        return 'BMI正常，持續保持!!'
    else:
        return'太胖了!!該減肥了' 

Window = tk.Tk()
Window.geometry('500x500')
Window.title('計算機')
Window.resizable(width = False, height = False)

title_label = tk.Label(Window, text = 'BMI計算機', font = ("標楷體", 24), padx = 20, pady = 20)
title_label.pack()

height_header = tk.Label(Window,text = '身高(cm): ', font = ("標楷體",14))
height_header.place(x=120, y=90)

weight_header = tk.Label(Window,text = '體重(Kg): ', font = ("標楷體",14))
weight_header.place(x=120, y=140)

ht = tk.StringVar()
wt = tk.StringVar()
rt = tk.StringVar()
height_entry = tk.Entry(Window, textvariable = ht)
height_entry.place(x=220, y=90, width = 150, height = 25)
weight_entry = tk.Entry(Window, textvariable = wt)
weight_entry.place(x=220, y=140, width = 150, height = 25)

result_label = tk.Label(Window, textvariable = rt, fg = 'red', font = ("標楷體", 14))
result_label.place(x=130, y=200)

Button_count = tk.Button(Window, text = '計算BMI', command = bmi_count  )
Button_count .place(x=220, y=300)

Window.mainloop()
