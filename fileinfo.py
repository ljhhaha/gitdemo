# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:04:11 2019

@author: LENOVO
"""

from tkinter import *#����tkinter��
top=Tk()#�����½���
top.title('ѧ������ϵͳ��½����')#����
label_1=Label(top,text='�û���')#������ǩ
label_2=Label(top,text='����')
textbox_1=Entry(top)#����
textbox_2=Entry(top,show='*')
button_1=Button(top,text='Login',command=lambda:login())#������ť
button_2=Button(top,text='�˳�',command=top.destroy)#�رս���
label_1.grid_configure(column=1,row=1,columnspan=1,rowspan=1)#�趨�ߴ�
label_2.grid_configure(column=1,row=2,columnspan=1,rowspan=1)
textbox_1.grid_configure(column=2,row=1,columnspan=10,rowspan=1)
textbox_2.grid_configure(column=2,row=2,columnspan=10,rowspan=1)
button_1.grid_configure(column=1,row=3,columnspan=5,rowspan=1)
button_2.grid_configure(column=6,row=3,columnspan=5,rowspan=1)
teacher_account={'admin':{'Pwd':'123456','Name':'Admin'},'admin2':{'Pwd':'987654321','Name':'Admin2'}}
student_list={'BZB':100,'bzb':80,'Bzb':95}
def login():#�趨��ť��Ӧ�ĺ���
    account=textbox_1.get()#�õ��ı����е�ֵ
    code=textbox_2.get()
    if account in teacher_account:#�ж�������û����Ƿ��ڴ洢��Χ��
        if teacher_account[account]['Pwd']==code:#�ж��û����������Ƿ��Ӧ
            top.destroy()#�رս���
            top_success=Tk()#�����½���
            top_success.title('��¼�ɹ�')#����
            def use():#������ť��Ӧ�ĺ���
                top_success.destroy()#�رս���
                top_use=Tk()#�����½���
                top_use.title('ѧ������ϵͳ')#����
                button_4=Button(top_use,text='��ӳɼ�',command=lambda:add()).pack()#���ð�ť
                button_5=Button(top_use,text='�鿴�ɼ�',command=lambda:search()).pack()
                button_6=Button(top_use,text='�˳�ϵͳ',command=top_use.destroy).pack()
                button_4.grid_configure(column=1,row=1,columnspan=4,rowspan=1)#���óߴ�
                button_5.grid_configure(column=1,row=2,columnspan=4,rowspan=1)
                button_6.grid_configure(column=1,row=3,columnspan=4,rowspan=1)
            label_3=Label(top_success,text='��ӭ����ʦ'+teacher_account[account]['Name']).pack()#���ñ�ǩ
            button_3=Button(top_success,text='OK',command=use).pack()
            button_3.grid_configure(column=6,row=3,columnspan=2,rowspan=1)
    else:
        top.destroy()
        top_false=Tk()
        top_false.title('��¼ʧ��')
        label_4=Label(top_false,text='�û������������').pack()
        button_7=Button(top_false,text='OK',command=top_false.destroy).pack()
        button_7.grid_configure(column=6,row=3,columnspan=2,rowspan=1)
import tkinter.simpledialog
def add():
    name=tkinter.simpledialog.askstring('��ʾ','������ѧ������')#���ý���
    if name in student_list:#�������������Ѿ��ڼ�����
        tkinter.messagebox.showinfo('����','��ѧ���Ѵ���')#�����Ӧ�����
    else:#�����������ֲ����б���
        score=tkinter.simpledialog.askinteger('��ʾ','������ѧ���ɼ�')#�����Ӧ�ĳɼ�
        student_list.update({name:score})#�����Ӧ�����ֺͳɼ���ӵ�����
    '''
    top_add=Tk()
    top_add.title('��ʾ')
    label_5=Label(top_add,text='������ѧ������').pack()
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
            top_add1.title('����')
            label_6=Label(top_add1,text='��ѧ���Ѵ���').pack()
            button_10=Button(top_add1,text='OK',command=top_add1.destroy).pack()
            button_10.grid_configure(column=6,row=3,columnspan=2,rowspan=1)
    else:
        def add1():
            top_add2=Tk()
            top_add2.title('��ʾ')
            textbox_4=Entry(top_add2).pack()
            label_7=Label(top_add2,text='������ѧ���ɼ�').pack()
            textbox_4.grid_configure(column=1,row=2,columnspan=10,rowspan=1).pack()
            def add2():
                student_list.update({a,textbox_4.get()})
                top_add2.destroy()
            button_10=Button(top_add,text='OK',command=add2).pack()
            button_11=Button(top_add,text='Cancel',command=top_add2.destroy).pack()
            button_10.grid_configure(column=1,row=3,columnspan=2,rowspan=1)
            button_11.grid_configure(column=5,row=3,columnspan=2,rowspan=1)
            '''
def search():#���á��鿴�ɼ�������Ӧ��ť�ĺ���
    for each in student_list.items():#������ּ���Ӧ�ĳɼ�
        print('����:',each[0],'    ','�ɼ�:',each[1])
mainloop()#չʾ