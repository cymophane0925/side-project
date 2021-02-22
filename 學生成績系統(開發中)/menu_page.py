import tkinter as tk
import tkinter.messagebox
import sqlite3
import os
import time
from tkinter import ttk



def menu_system():
    
    def st_data():#學生資料頁面
 
        def combo_change(event): #連動式下拉選單
            st_level = st_level_combo.get()
            if st_level:
                comboclass["values"] = studentClasses.get(st_level)
            else:
                comboclass.set([])
        
        def insertdata():
            localtime = time.localtime(time.time())#紀錄時間
            urtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())            
            stna = st_name.get() #姓名
            stsc = school_name.get() #學校
            stl = st_level_combo.get() #學制級別
            stlc = comboclass.get() #年級
            stcls = st_class.get() #班級
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
            sqlstr = "insert into studentdata values( '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(stna, stsc, stl, stlc, stcls, sts, stadr, stp, stec, stecp, stm, stre, now_tag, urtime)
            conn.execute(sqlstr)
            conn.commit()  #更新資料庫用
            tk.messagebox.showinfo('success', '新增成功') 
    
            conn.close()
    
        def rebackpage():             
            window.destroy()
            menu_system()
        
            
        
        
        #封鎖其他選項
        
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
        #學生學級年級下拉視選單
        st_level_combo = ttk.Combobox(window, values=tuple(studentClasses.keys()), width=8)
        st_level_combo.place(x=380, y=150)
        st_level_combo.bind('<<ComboboxSelected>> ', combo_change)
        #就讀年級
        st_school_class = tk.Label(window, text='就讀年級:')
        st_school_class.place(x=480, y=150)
        comboclass = ttk.Combobox(window,width=10)
        comboclass.place(x=550, y=150)
        #班級
        st_class = tk.StringVar()
        st_class_labe = ttk.Label(window, text='班級:', width=20).place(x=650, y=150)
        st_class_entry = ttk.Entry(window, textvariable=st_class, width=10).place(x=690, y=150)
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
        #返回
        btnDown2 = tk.Button(window, text = '返 回', width=10, command=rebackpage)
        btnDown2.place(x=520, y=500)    
        

           
        
        
        
        
        
        
                                                     
    def insert_grades():#成績登錄

        def sql_compute(sqlstr):
            conn = sqlite3.connect('Student_achievement_data.sqlite')
            cursor = conn.execute(sqlstr)
            rows = cursor.fetchall()
            conn.commit()
            conn.close()
            return rows
        
    
        
        def st_info(event):#下拉視選單選擇後讀出基本資料(學校選擇>年級)
            nameinfo = st_name_combo.get()        
            if nameinfo:            
                st_gr_combo['values'] = datachange(sql_compute("select grade2 from studentdata where school = '{}'".format(nameinfo)))             
            else:
                st_gr_combo.set([])
                
        def st_info2(event):#年級選擇>班級
            gradeinfo = st_gr_combo.get()        
            if gradeinfo:            
                st_cl_combo['values'] = datachange(sql_compute("select class from studentdata where grade2 = '{}'".format(gradeinfo)))                       
            else:
                st_cl_combo.set([])
                
        def st_info3(event):#班級>姓名
            classinfo = st_cl_combo.get()
            gradeinfo = st_gr_combo.get()         
            if classinfo:            
                st_p_combo['values'] = datachange(sql_compute("select name from studentdata where class = '{}' and grade2 = '{}' ".format(classinfo,gradeinfo )))                       
            else:
                st_p_combo.set([])                          
                
        def school_year():#製作學年表##現在年分轉學年度且往前5年
            localtime = time.localtime(time.time())#現在時間(時間搓)
            u = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#轉換時間格式
            y = u.split('-')
            p = int(y[0]) - 1911
            rows=[p-r for r in range(12)]
            year = ['{} 學年度'.format(k) for k in rows]
            return year 
        
        def school_year_2():#下拉式選單values
            year2 = ('上學期', '下學期')
            return year2
        
        def exam_type():#下拉式選單values
            exam = ('第一次段考(期中考)', '第二次段考(期中考)', '第三次段考(期末考)', '第四次段考(期末考)')
            return exam
        
        def datachange(data):# 資料型態轉換
            rows = [r[0] for r in data]
            return list(set(rows))
        def addinfo():
            localtime = time.localtime(time.time())#紀錄時間
            urtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            schn = st_name_combo.get()#校名
            stgr = st_gr_combo.get()#年級
            stcl = st_cl_combo.get()#班級
            stn = st_p_combo.get()#姓名
            scy = schoolyear_combo.get()#學年度
            scy2 = schoolyear2_combo.get()#上下學期
            scy3 = schoolyear3_combo.get() #段考
            sb1 = st_point1.get()
            p1 = point_combo1.get()
            sb2 = st_point2.get()
            p2 = point_combo2.get()
            sb3 = st_point3.get()
            p3 = point_combo3.get()
            sb4 = st_point4.get()
            p4 = point_combo4.get()
            sb5 = st_point5.get()
            p5 = point_combo5.get()
            sb6 = st_point6.get()
            p6 = point_combo6.get()
            sb7 = st_point7.get()
            p7 = point_combo7.get()
            sb8 = st_point8.get()
            p8 = point_combo8.get()
            now_tag = 1
            
            conn = sqlite3.connect( 'Student_achievement_data.sqlite' )
            sqlstr = "insert into studentgrades values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(schn, stgr, stcl, stn, scy, scy2, scy3, p1, sb1, p2, sb2, p3, sb3, p4, sb4, p5, sb5, p6, sb6, p7, sb7, p8, sb8, now_tag, urtime)
            conn.execute(sqlstr)
            conn.commit()  #更新資料庫用
            tk.messagebox.showinfo('success', '新增成功') 
       
            conn.close()
            
            
        def rebackpage1():#返回             
            window.destroy()
            menu_system()
    
        def delSource1():  #刪除
            name_nums = st_p_combo.get()
        
            if name_nums:
                conn = sqlite3.connect( 'Student_achievement_data.sqlite' )            
                sqlstr = "select * from studentgrades where studentname = {}" .format( name_nums )
                cursor=conn.execute(sqlstr) 
                row = cursor.fetchone()
                #print(row)
                if row == None:
                    tk.messagebox.showinfo('Fail', "{} not exist!".format(name_nums))
                else:
                    sqlstr = "update studentgrades set tag=0 where studentname ='{}'".format( name_nums )
                    conn.execute(sqlstr)
                    conn.commit()  #更新資料庫用
                    tk.messagebox.showinfo('success', '刪除成功')
                    
                conn.close()
            else:
                tk.messagebox.showinfo('Fail', '請選擇姓名')                        
                  
          
        #title    
        basdata_title = tk.Label(window, text='學生成績登錄',font=("新細明體", 16) , width=20).place(x=330, y=20)
        
        #學校
        st_name_labe = ttk.Label(window, text='就讀學校 :').place(x=280, y=80)   
        sample = sql_compute("select school from studentdata where tag = 1")
        st_name_combo = ttk.Combobox(window, values=datachange(sample), width=10)
        st_name_combo.place(x=360, y=80)
        st_name_combo.bind('<<ComboboxSelected>> ', st_info)
        
        #年級
        st_gr_labe = ttk.Label(window, text='年級 :').place(x=480, y=80)
        st_gr_combo = ttk.Combobox(window, width=10)
        st_gr_combo.place(x=520, y=80)
        st_gr_combo.bind('<<ComboboxSelected>> ', st_info2)
        #班級
        st_cl_labe = ttk.Label(window, text='班級 :').place(x=640, y=80)
        st_cl_combo = ttk.Combobox(window, width=10)
        st_cl_combo.place(x=680, y=80)
        st_cl_combo.bind('<<ComboboxSelected>> ', st_info3)    
        #姓名
        st_p_labe = ttk.Label(window, text='學生姓名 :').place(x=280, y=120)
        st_p_combo = ttk.Combobox(window, width=10)
        st_p_combo.place(x=360, y=120)    
        #學生基本資訊
        #st_msg = tk.StringVar()
        #msg_lable = tk.Label(window, textvariable=st_msg, font = (8), fg='blue', justify='left')
        #msg_lable.place(x=280, y=110)
        
        #學年度/學期/考試種類
        st_schoolyear_labe = ttk.Label(window, text='學年度/分類:').place(x=280, y=160)
        schoolyear_combo = ttk.Combobox(window,values=school_year(), width=10)
        schoolyear_combo.place(x=360, y=160)
        schoolyear_combo.current(0)
        
        schoolyear2_combo= ttk.Combobox(window,values=school_year_2(), width=10)
        schoolyear2_combo.place(x=470, y=160)
        schoolyear2_combo.current(0)
        
        schoolyear3_combo= ttk.Combobox(window,values=exam_type(), width=20)
        schoolyear3_combo.place(x=580, y=160)
        schoolyear3_combo.current(0)
        
        #學生分數一
        subject = ('選擇科目:','國文', '英文', '數學', '自然', '社會', '生物', '歷史', '地理', '公民', '理化', '物理', '化學', '健康與體育', '英文作文', '國文作文')
        st_point1 = tk.StringVar()
        st_point1_labe = ttk.Label(window, text='填入分數一 :').place(x=280, y=200)
        point_combo1 = ttk.Combobox(window, values=subject, width=10)
        point_combo1.place(x=360, y=200)
        point_combo1.current(0)
        st_point1_entry = ttk.Entry(window, textvariable=st_point1, width=15).place(x=470, y=200)
        
        st_point2 = tk.StringVar()
        st_point2_labe = ttk.Label(window, text='填入分數二 :').place(x=280, y=240)
        point_combo2 = ttk.Combobox(window, values=subject, width=10)
        point_combo2.place(x=360, y=240)
        point_combo2.current(0)
        st_point2_entry = ttk.Entry(window, textvariable=st_point2, width=15).place(x=470, y=240)
        
        st_point3 = tk.StringVar()
        st_point3_labe = ttk.Label(window, text='填入分數三 :').place(x=280, y=280)
        point_combo3 = ttk.Combobox(window, values=subject, width=10)
        point_combo3.place(x=360, y=280)
        point_combo3.current(0)
        st_point3_entry = ttk.Entry(window, textvariable=st_point3, width=15).place(x=470, y=280)
    
        st_point4 = tk.StringVar()
        st_point4_labe = ttk.Label(window, text='填入分數四 :').place(x=280, y=320)
        point_combo4 = ttk.Combobox(window, values=subject, width=10)
        point_combo4.place(x=360, y=320)
        point_combo4.current(0)
        st_point4_entry = ttk.Entry(window, textvariable=st_point4, width=15).place(x=470, y=320)    
    
    
        st_point5 = tk.StringVar()
        st_point5_labe = ttk.Label(window, text='填入分數五 :').place(x=280, y=360)
        point_combo5 = ttk.Combobox(window, values=subject, width=10)
        point_combo5.place(x=360, y=360)
        point_combo5.current(0)
        st_point5_entry = ttk.Entry(window, textvariable=st_point5, width=15).place(x=470, y=360)
        
        st_point6 = tk.StringVar()
        st_point6_labe = ttk.Label(window, text='填入分數六 :').place(x=280, y=400)
        point_combo6 = ttk.Combobox(window, values=subject, width=10)
        point_combo6.place(x=360, y=400)
        point_combo6.current(0)
        st_point6_entry = ttk.Entry(window, textvariable=st_point6, width=15).place(x=470, y=400)
        
        st_point7 = tk.StringVar()
        st_point7_labe = ttk.Label(window, text='填入分數七 :').place(x=280, y=440)
        point_combo7 = ttk.Combobox(window, values=subject, width=10)
        point_combo7.place(x=360, y=440)
        point_combo7.current(0)
        st_point7_entry = ttk.Entry(window, textvariable=st_point7, width=15).place(x=470, y=440)
        
        st_point8= tk.StringVar()
        st_point8_labe = ttk.Label(window, text='填入分數八 :').place(x=280, y=480)
        point_combo8 = ttk.Combobox(window, values=subject, width=10)
        point_combo8.place(x=360, y=480)
        point_combo8.current(0)
        st_point8_entry = ttk.Entry(window, textvariable=st_point8, width=15).place(x=470, y=480)
        #顯示新增成果
        #lstStudent = tk.Listbox(window, width=380)
        #lstStudent.place(x=280, y=430, width=500, height=100)
        
        #登錄sqlite
        btnDown = tk.Button(window, text='新 增', width=10,command=addinfo)
        btnDown.place(x=360, y=550)
        #返回
        btnDown2 = tk.Button(window, text='返 回', width=10,command=rebackpage1)
        btnDown2.place(x=500, y=550)  
        
        #刪除
        btnDown3 = tk.Button(window, text='刪 除', width=10,command=delSource1)
        btnDown3.place(x=640, y=550)
        
        
    
    
    def grades_search():#成績查詢
        def sql_compute(sqlstr):
            conn = sqlite3.connect('Student_achievement_data.sqlite')
            cursor = conn.execute(sqlstr)
            rows = cursor.fetchall()
            conn.commit()
            conn.close()
            return rows
        
        
        def st_info(event):#下拉視選單選擇後讀出基本資料(學校選擇>年級)
            nameinfo = st_name_combo.get()        
            if nameinfo:            
                st_gr_combo['values'] = datachange(sql_compute("select grade from studentgrades where school = '{}'".format(nameinfo)))             
            else:
                st_gr_combo.set([])
                
        def st_info2(event):#年級選擇>班級
            gradeinfo = st_gr_combo.get()        
            if gradeinfo:            
                st_cl_combo['values'] = datachange(sql_compute("select class from studentgrades where grade = '{}'".format(gradeinfo)))                       
            else:
                st_cl_combo.set([])
                
        def st_info3(event):#班級>姓名
            classinfo = st_cl_combo.get()
            gradeinfo = st_gr_combo.get()         
            if classinfo:            
                st_p_combo['values'] = datachange(sql_compute("select studentname from studentgrades where class = '{}' and grade = '{}' ".format(classinfo, gradeinfo )))                       
            else:
                st_p_combo.set([])                          
                
        def school_year(event):#製作學年表##現在年分轉學年度且往前5年
            nameinfo = st_p_combo.get()
            classinfo = st_cl_combo.get()
            gradeinfo = st_gr_combo.get() 
            if nameinfo:
                schoolyear_combo['values'] =datachange(sql_compute("select year from studentgrades where studentname ='{}' and class = '{}' and grade = '{}' ".format(nameinfo, classinfo, gradeinfo)))
            else:
                schoolyear_combo.set([])           
                   
        def school_year_2(event):#下拉式選單values
            yearinfo = schoolyear_combo.get()
            nameinfo = st_p_combo.get()
            classinfo = st_cl_combo.get()
            gradeinfo = st_gr_combo.get() 
            if yearinfo:
                schoolyear2_combo['values'] =datachange(sql_compute("select semester from studentgrades where studentname ='{}' and class = '{}' and grade = '{}' and year ='{}'".format(nameinfo, classinfo, gradeinfo, yearinfo)))
            else:
                schoolyear2_combo.set([])
            
        
        def exam_type(event):#下拉式選單values
            yearinfo = schoolyear_combo.get()
            nameinfo = st_p_combo.get()
            classinfo = st_cl_combo.get()
            gradeinfo = st_gr_combo.get()
            semesterinfo = schoolyear2_combo.get()
            if semesterinfo:
                schoolyear3_combo['values'] =datachange(sql_compute("select exam from studentgrades where studentname ='{}' and class = '{}' and grade = '{}' and year ='{}' and semester = '{}'".format(nameinfo, classinfo, gradeinfo, yearinfo, semesterinfo)))
            else:
                schoolyear3_combo.set([])
        
        def datachange(data):# 資料型態轉換
            rows = [r[0] for r in data]
            return list(set(rows))
        
        def datachange2(data):# 資料型態轉換 tuple >list
            for r in data:
                rows = list(r)
            return rows[0:23]
        
        def rangegread(data):
            season = ''
            for i in range(7, 23, 2):
                season += ('' if data[i] =='選擇科目:' else data[i]) + ' '  + ('' if data[i+1] =='' else data[i+1]) + ' '
            lstStudent.insert('end', season)
                
    
        def result_insert(data):
            r1 = '學校: ' + data[0] 
            lstStudent.insert(0, r1)
            r2 = '年級/班級: ' + data[1] + data[2]
            lstStudent.insert(1, r2)
            r3 = '姓名: ' + data[3]
            lstStudent.insert(2, r3)
            r4 = data[4] +' '+ data[5] +'\n'+ data[6]+' '+'分數:'
            lstStudent.insert(3, r4)        
            rangegread(data)
            
        
        def searchdata():
            sch = st_name_combo.get()
            grd = st_gr_combo.get()
            cla = st_cl_combo.get()
            stn = st_p_combo.get()
            ye = schoolyear_combo.get()
            sem = schoolyear2_combo.get()
            examd = schoolyear3_combo.get()
            data = datachange2(sql_compute("select * from studentgrades where school = '{}' and grade = '{}'  and class = '{}' and studentname = '{}' and year = '{}' and semester ='{}' and exam ='{}'".format(sch, grd, cla, stn, ye ,sem,examd)))
            result_insert(data)
        def rebackpage2():#返回             
            window.destroy()
            menu_system()         
          
        #title    
        basdata_title = tk.Label(window, text='學生成績查詢',font=("新細明體", 16) , width=20).place(x=330, y=20)
        
        #學校
        st_name_labe = ttk.Label(window, text='就讀學校 :').place(x=280, y=80)   
        sample = sql_compute("select school from studentgrades where tag = 1")
        st_name_combo = ttk.Combobox(window, values=datachange(sample), width=10)
        st_name_combo.place(x=360, y=80)
        st_name_combo.bind('<<ComboboxSelected>> ', st_info)
        
        #年級
        st_gr_labe = ttk.Label(window, text='年級 :').place(x=480, y=80)
        st_gr_combo = ttk.Combobox(window, width=10)
        st_gr_combo.place(x=520, y=80)
        st_gr_combo.bind('<<ComboboxSelected>> ', st_info2)
        #班級
        st_cl_labe = ttk.Label(window, text='班級 :').place(x=640, y=80)
        st_cl_combo = ttk.Combobox(window, width=10)
        st_cl_combo.place(x=680, y=80)
        st_cl_combo.bind('<<ComboboxSelected>> ', st_info3)    
        #姓名
        st_p_labe = ttk.Label(window, text='學生姓名 :').place(x=280, y=120)
        st_p_combo = ttk.Combobox(window, width=10)
        st_p_combo.place(x=360, y=120)
        st_p_combo.bind('<<ComboboxSelected>> ', school_year)    
        #學生基本資訊
        #st_msg = tk.StringVar()
        #msg_lable = tk.Label(window, textvariable=st_msg, font = (8), fg='blue', justify='left')
        #msg_lable.place(x=280, y=110)
        
        #學年度/學期/考試種類
        st_schoolyear_labe = ttk.Label(window, text='學年度/分類:').place(x=280, y=160)
        schoolyear_combo = ttk.Combobox(window, width=10)
        schoolyear_combo.place(x=360, y=160)
        schoolyear_combo.bind('<<ComboboxSelected>> ', school_year_2)
    
        
        schoolyear2_combo= ttk.Combobox(window, width=10)#上下學期
        schoolyear2_combo.place(x=470, y=160)
        schoolyear2_combo.bind('<<ComboboxSelected>> ', exam_type)
        
        schoolyear3_combo= ttk.Combobox(window, width=20)#第幾次段考
        schoolyear3_combo.place(x=580, y=160)
    
        
        #顯示新增成果
        lstStudent = tk.Listbox(window, width=380)
        lstStudent.place(x=280, y=220, width=500, height=100)
        
        #顯示新增成果
        #LT = tk.StringVar()
        #lstStudent = tk.Label(window, textvariable = LT, font=(10),fg='blue', justify='left')
        #lstStudent.place(x=280, y=200)
        
        #登錄sqlite
        btnDown = tk.Button(window, text = '查詢', command=searchdata ,width=10)
        btnDown.place(x=360, y=550)
        #返回
        btnDown2 = tk.Button(window, text = '返 回', command=rebackpage2, width=10)
        btnDown2.place(x=520, y=550)     
     
        

        
    #主要介面
    window = tk.Tk()
    window.geometry('850x600')
    window.title('學生成績登錄系統-Menu')
    window.resizable(0, 0)
    
    
    def menu_view():
        #選單
        place_null = tk.Label(window, text='', width=20).pack(anchor=tk.NW, ipady=5, pady=2)
        st_menu = ttk.Button(window, text='學生資料登錄', width=20, command=st_data, state=tk.NORMAL).pack(anchor=tk.NW, ipady=5, pady=2)
        st_grades = ttk.Button(window, text='學期成績登錄', width=20, command=insert_grades, state=tk.NORMAL).pack(anchor=tk.NW, ipady=5, pady=2)
        st_grades_inquire = ttk.Button(window, text='學期成績查詢', width=20,command=grades_search, state=tk.NORMAL).pack(anchor=tk.NW, ipady=5, pady=2)
        st_grades_data = ttk.Button(window, text='學生資料查詢', width=20, state=tk.DISABLED).pack(anchor=tk.NW, ipady=5, pady=2)
        st_grades_ana = ttk.Button(window, text='歷年成績分析', width=20, state=tk.DISABLED).pack(anchor=tk.NW, ipady=5, pady=2)
        page_back = ttk.Button(window, text='返回登錄頁面', width=20, state=tk.DISABLED).pack(anchor=tk.NW, ipady=5, pady=2)
    
    
    
    
    menu_view()
    
    window.mainloop()
    
    
    
