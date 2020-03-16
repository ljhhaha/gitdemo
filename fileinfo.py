# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:04:11 2019

@author: LENOVO
"""

from tkinter import *#引用tkinter库
top=Tk()#创建新界面
top.title('学生管理系统登陆界面')#命名
label_1=Label(top,text='用户名')#创建标签
label_2=Label(top,text='密码')
textbox_1=Entry(top)#输入
textbox_2=Entry(top,show='*')
button_1=Button(top,text='Login',command=lambda:login())#创建按钮
button_2=Button(top,text='退出',command=top.destroy)#关闭界面
label_1.grid_configure(column=1,row=1,columnspan=1,rowspan=1)#设定尺寸
label_2.grid_configure(column=1,row=2,columnspan=1,rowspan=1)
textbox_1.grid_configure(column=2,row=1,columnspan=10,rowspan=1)
textbox_2.grid_configure(column=2,row=2,columnspan=10,rowspan=1)
button_1.grid_configure(column=1,row=3,columnspan=5,rowspan=1)
button_2.grid_configure(column=6,row=3,columnspan=5,rowspan=1)
teacher_account={'admin':{'Pwd':'123456','Name':'Admin'},'admin2':{'Pwd':'987654321','Name':'Admin2'}}
student_list={'BZB':100,'bzb':80,'Bzb':95}
def login():#设定按钮对应的函数
    account=textbox_1.get()#得到文本框中的值
    code=textbox_2.get()
    if account in teacher_account:#判断输入的用户名是否在存储范围内
        if teacher_account[account]['Pwd']==code:#判断用户名和密码是否对应
            top.destroy()#关闭界面
            top_success=Tk()#创建新界面
            top_success.title('登录成功')#命名
            def use():#命名按钮对应的函数
                top_success.destroy()#关闭界面
                top_use=Tk()#创建新界面
                top_use.title('学生管理系统')#命名
                button_4=Button(top_use,text='添加成绩',command=lambda:add()).pack()#设置按钮
                button_5=Button(top_use,text='查看成绩',command=lambda:search()).pack()
                button_6=Button(top_use,text='退出系统',command=top_use.destroy).pack()
                button_4.grid_configure(column=1,row=1,columnspan=4,rowspan=1)#设置尺寸
                button_5.grid_configure(column=1,row=2,columnspan=4,rowspan=1)
                button_6.grid_configure(column=1,row=3,columnspan=4,rowspan=1)
            label_3=Label(top_success,text='欢迎，教师'+teacher_account[account]['Name']).pack()#设置标签
            button_3=Button(top_success,text='OK',command=use).pack()
            button_3.grid_configure(column=6,row=3,columnspan=2,rowspan=1)
    else:
        top.destroy()
        top_false=Tk()
        top_false.title('登录失败')
        label_4=Label(top_false,text='用户名或密码错误').pack()
        button_7=Button(top_false,text='OK',command=top_false.destroy).pack()
        button_7.grid_configure(column=6,row=3,columnspan=2,rowspan=1)
import tkinter.simpledialog
def add():
    name=tkinter.simpledialog.askstring('提示','请输入学生姓名')#设置界面
    if name in student_list:#如果输入的名字已经在集合内
        tkinter.messagebox.showinfo('错误','该学生已存在')#输出对应的语句
    else:#如果输入的名字不在列表内
        score=tkinter.simpledialog.askinteger('提示','请输入学生成绩')#输入对应的成绩
        student_list.update({name:score})#将相对应的名字和成绩添加到集合
    '''
    top_add=Tk()
    top_add.title('提示')
    label_5=Label(top_add,text='请输入学生姓名').pack()
    textbox_3=Entry(top_add).pack()
    textbox_3.grid_configure(column=1,row=2,columnspan=10,rowspan=1).pack()
    button_8=Button(top_add,text='OK',command=lambda:add1()).pack()
    button_9=Button(top_add,text='Cancel',command=top_add.destroy).pack()
    button_8.grid_configure(column=1,row=3,columnspan=2,rowspan=1)
    button_9.grid_configure(column=5,row=3,columnspan=2,rowspan=1)
    a=textbox_3.get()
    if a in student_list:
        def add1():
            top_add1=Tk()
            top_add1.title('错误')
            label_6=Label(top_add1,text='该学生已存在').pack()
            button_10=Button(top_add1,text='OK',command=top_add1.destroy).pack()
            button_10.grid_configure(column=6,row=3,columnspan=2,rowspan=1)
    else:
        def add1():
            top_add2=Tk()
            top_add2.title('提示')
            textbox_4=Entry(top_add2).pack()
            label_7=Label(top_add2,text='请输入学生成绩').pack()
            textbox_4.grid_configure(column=1,row=2,columnspan=10,rowspan=1).pack()
            def add2():
                student_list.update({a,textbox_4.get()})
                top_add2.destroy()
            button_10=Button(top_add,text='OK',command=add2).pack()
            button_11=Button(top_add,text='Cancel',command=top_add2.destroy).pack()
            button_10.grid_configure(column=1,row=3,columnspan=2,rowspan=1)
            button_11.grid_configure(column=5,row=3,columnspan=2,rowspan=1)
            '''
def search():#设置‘查看成绩’所对应按钮的函数
    for each in student_list.items():#输出名字及对应的成绩
        print('姓名:',each[0],'    ','成绩:',each[1])
mainloop()#展示