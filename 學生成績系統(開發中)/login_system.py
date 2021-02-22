#帳號密碼登入系統

import tkinter as tk
import tkinter.messagebox
import sqlite3
import os
from menu_page import menu_system 

def loginsystem():
    
    def sql_compute(sqlstr):
        conn = sqlite3.connect('Student_achievement_data.sqlite')
        cursor = conn.execute(sqlstr)
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return rows
    
    def sign_user(): #註冊介面
        def sign_button(): #註冊資料登錄        
            nn = new_user_name.get()
            np = new_user_pwd.get()
            cp = ck_new_pwd.get()
            ic = id_code.get()
            now_tag = 1        
            if nn == '': #帳號為空
                user_msg.set('請輸入帳號')            
            elif np == '':
                user_msg.set('請輸入6位數密碼')
            elif len(np) < 6:
                user_msg.set('密碼必須大於等於6位數')
            elif ic =='':
                user_msg.set('請輸入身分證')
            elif ic.islower():#身分證出現小寫
                user_msg.set('身分證字母不能為小寫')
            elif len(ic) != 10:
                user_msg.set('身分證格式錯誤')
            elif np != cp :
                user_msg.set('密碼必須一致，請再次確認')
                if cp == '':
                    user_msg.set('請輸入密碼')               
            else:
                rows = sql_compute("select * from user_account where tag = 1") #查詢資料庫帳號是否重複
                u = [ r[0] for (i,r) in enumerate(rows)]
                c = [ r[2] for (i,r) in enumerate(rows)]
                if nn in u:
                    user_msg.set('帳號重複')
                elif ic in c:
                    user_msg.set('身分證帳號重複')      
                else:    
                    sqlstr = "insert into user_account values('{}', '{}', '{}', '{}');".format(nn, np, ic.title(), now_tag)
                    sql_compute(sqlstr)            
                    tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!\n註冊成功')            
                    user_window.destroy()           
                        
        #註冊視窗
        user_window = tk.Toplevel(window)
        user_window.geometry('300x300')
        user_window.title('使用者註冊')
        user_window.resizable(0,0)
        
        #註冊帳號輸入
        new_user_name = tk.StringVar()
        user_label = tk.Label(user_window, text='使用者帳號 :')
        user_label.place(x=10, y=40)
        user_entry = tk.Entry(user_window, textvariable=new_user_name, width=25)
        user_entry.place(x=100, y=40)
        
        
        #註冊密碼輸入
        new_user_pwd = tk.StringVar()
        user_pwd_label = tk.Label(user_window, text = '使用者密碼 :')
        user_pwd_label.place(x=10, y=80)
        user_pwd_entry = tk.Entry(user_window,show = "*", textvariable=new_user_pwd, width=25)
        user_pwd_entry.place(x=100, y=80)
        
        #註冊密碼確認
        ck_new_pwd = tk.StringVar()
        ck_pwd_label = tk.Label(user_window, text = '確認密碼   :')
        ck_pwd_label.place(x=10, y=120)
        ck_pwd_entry = tk.Entry(user_window,show = "*", textvariable=ck_new_pwd, width=25)
        ck_pwd_entry.place(x=100, y=120)
        
        #身分證確認
        id_code = tk.StringVar()
        id_code_label = tk.Label(user_window, text = '輸入身分證   :')
        id_code_label.place(x=10, y=160)
        id_code_entry = tk.Entry(user_window, textvariable=id_code, width=25)
        id_code_entry.place(x=100, y=160)
        #註冊按鈕
        sign_up_button = tk.Button(user_window, text = '註冊新使用者', command=sign_button)
        sign_up_button.place(x=130, y=200)
        
        #註冊訊息
        user_msg = tk.StringVar()
        msg_lable = tk.Label(user_window, textvariable=user_msg, fg='red', justify='left')
        msg_lable.place(x=130, y=240)
        
    def user_check():# 使用者登入
        user = account_nums.get()
        pwd = password_nums.get()
        
        if user =='':
            tkinter.messagebox.showwarning('Error!!', '請輸入帳號')
        elif pwd =='':
            tkinter.messagebox.showwarning('Error!!', '請輸入密碼')
        else:
            rows = sql_compute("select * from user_account where tag = 1") #查詢資料庫帳號是否重複
            u = [ r for (i,r) in enumerate(rows)]
            for k in u:
                if user in k:
                    if pwd in k:
                        tkinter.messagebox.showinfo('Welcome', '登入成功')
                        window.destroy()
                        menu_system()#登入後先換到menu程式
                        break
            else:
                tkinter.messagebox.showwarning('登入失敗', '請確認或註冊帳號密碼')
                
            
    
    
    
    #主要介面
    window = tk.Tk()
    window.geometry('550x350')
    window.title('學生成績登錄系統')
    window.resizable(0, 0)
    
    #使用者帳號
    account_nums = tk.StringVar() #帳號
    label_acc = tk.Label(window, text='Account(使用者帳號)   :')
    label_acc.place(x=65, y=120)
    acc_nums = tk.Entry(window, textvariable=account_nums, width=30)
    acc_nums.place(x=200, y=122)
    
    #使用者密碼
    password_nums = tk.StringVar() #密碼
    label_pass = tk.Label(window, text='Password(使用者密碼) :')
    label_pass.place(x=65, y=160)
    pass_nums = tk.Entry(window, show='*', textvariable=password_nums, width=30)
    pass_nums.place(x=200, y=160)
    
    #登入&註冊按鈕
    login = tk.Button(window, text="Login 登入", width=10, command=user_check )
    login.place(x=200, y=200)
    sign_up = tk.Button(window, text="sign up 註冊", width=10, command=sign_user)
    sign_up.place(x=300, y=200)
    
    #更改密碼&忘記密碼按鈕
    pwd_change = tk.Button(window, text="Change the password - 變更密碼", width=30, relief=tk.GROOVE)
    pwd_change.place(x=170, y=250)
    pwd_find = tk.Button(window, text="Find the password - 找回密碼", width=30, relief=tk.GROOVE)
    pwd_find.place(x=170, y=290)
    
    
    
    window.mainloop()

loginsystem()
