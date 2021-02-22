import tkinter as tk
import tkinter.messagebox
import sqlite3
import os
from tkinter import ttk
from menu_page import main


def st_data():
    def combo_change(event): #連動式下拉選單
        st_level = st_level_combo.get()
        if st_level:
            comboclass["values"] = studentClasses.get(st_level)
        else:
            comboclass.set([])
    
    def insertdata():
        stna = st_name.get() #姓名
        stsc = school_name.get() #學校
        stl = st_level_combo.get() #學制級別
        stlc = comboclass.get() #年級
        sts = sex.get() #性別
        stadr = st_address.get() #住家地址
        stp = st_phone.get() #連絡電話
        stec = st_EC.get() #緊急聯絡人
        stecp = st_EC_phone.get() #緊急聯絡人電話
        stm = st_mail.get() #電子郵件
        stre = st_remark.get() #備註欄
        now_tag = 1
        
        if sts == 1:
            sts = '男生'
        else:
            sts = '女生'
                   
        conn = sqlite3.connect( 'Student_achievement_data.sqlite' )
        sqlstr = "insert into studentdata values( '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}' );".format(stna, stsc, stl, stlc, sts, stadr, stp, stec, stecp, stm, stre, now_tag)
        conn.execute(sqlstr)
        conn.commit()  #更新資料庫用
        tk.messagebox.showinfo('success', '新增成功') 
            
        conn.close()
        
        
    #基本資料title
    basdata_title = tk.Label(window, text='學生基本資料',font=("新細明體", 16) , width=20).place(x=330, y=20)
    #姓名
    st_name = tk.StringVar()
    st_name_labe = ttk.Label(window, text='學生姓名:', width=20).place(x=320, y=70)
    st_name_entry = ttk.Entry(window, textvariable=st_name, width=15).place(x=380, y=70)
    #就讀學校
    school_name= tk.StringVar()
    st_school_labe = ttk.Label(window, text='就讀學校:', width=20).place(x=320, y=110)
    st_school_entry = ttk.Entry(window, textvariable=school_name, width=20).place(x=380, y=110)
    #就讀年級
    st_school_level = ttk.Label(window, text='學制級別:', width=20).place(x=320, y=150)
    #建立年級班級字典
    studentClasses = {'國小': ['一年級', '二年級', '三年級', '四年級', '五年級', '六年級'],
                      '國中': ['一年級', '二年級', '三年級'],
                      '高中': ['一年級', '二年級', '三年級'],
                      }
    #學生班級年級下拉視選單
    st_level_combo = ttk.Combobox(window, values=tuple(studentClasses.keys()), width=8)
    st_level_combo.place(x=380, y=150)
    st_level_combo.bind('<<ComboboxSelected>> ', combo_change)
    #就讀班級
    st_school_class = tk.Label(window, text='就讀年級:')
    st_school_class.place(x=480, y=150)
    comboclass = ttk.Combobox(window)
    comboclass.place(x=550, y=150)
    #性別: 1:男生;0:女生(默認為男聲)
    sex_label = tk.Label(window, text='性別:').place(x=345, y=190)    
    sex = tkinter.IntVar(value=1)
    st_sex_boy = tk.Radiobutton(window, variable=sex, value=1, text='男')
    st_sex_boy.place(x=390, y=190)
    st_sex_girl = tk.Radiobutton(window, variable=sex, value=0, text='女')
    st_sex_girl.place(x=450, y=190)
    
    #住址
    st_address = tk.StringVar()
    st_address_labe = ttk.Label(window, text='住家地址:', width=20).place(x=320, y=230)
    st_address_entry = ttk.Entry(window, textvariable=st_address, width=40).place(x=380, y=230)
    
    #聯絡電話
    st_phone = tk.StringVar()
    st_phone_labe = ttk.Label(window, text='聯絡電話:', width=20).place(x=320, y=270)
    st_phone_entry = ttk.Entry(window, textvariable=st_phone, width=20).place(x=380, y=270)
    #緊急聯絡人、聯絡人手機
    st_EC = tk.StringVar()
    st_EC_labe = ttk.Label(window, text='緊急聯絡人:', width=20).place(x=310, y=310)
    st_EC_entry = ttk.Entry(window, textvariable=st_EC, width=15).place(x=380, y=310)
    
    st_EC_phone = tk.StringVar()
    st_EC_phone_labe = ttk.Label(window, text='電話 :', width=20).place(x=520, y=310)
    st_EC_phone_entry = ttk.Entry(window, textvariable=st_EC_phone, width=20).place(x=560, y=310)    
    
    #email
    st_mail = tk.StringVar()
    st_mail_labe = ttk.Label(window, text='e-mail :', width=20).place(x=330, y=350)
    st_mail_entry = ttk.Entry(window, textvariable=st_mail, width=40).place(x=380, y=350)
    
    #備註欄
    st_remark = tk.StringVar()
    st_remark_labe = ttk.Label(window, text='備註欄 :', width=20).place(x=330, y=390)
    st_remark_entry = ttk.Entry(window, textvariable=st_remark, width=40).place(x=380, y=390)
    
    #登錄sqlite
    btnDown = tk.Button(window, text = '新 增', width=10, command=insertdata)
    btnDown.place(x=420, y=500)
    
    #返回選單
    btnDown2 = tk.Button(window, text = '返回', width=10,)
    btnDown2.place(x=550, y=500)