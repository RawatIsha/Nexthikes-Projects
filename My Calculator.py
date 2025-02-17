from tkinter import *

def call_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

root=Tk()
root.title('Python Calculator')
##root.geometry('295x240')
##root.resizable(0,0)

def button_click(number):
    current = result_label.get()
    result_label.delete(0, END) 
    result_label.insert(0, current + str(number))
                                                                      


result_label= Label(root,text=0, fg='black')
result_label.grid(row=0, column=0,columnspan=5,padx=10, pady=10)
result_label.config(font=('verdana',30,'bold'))
root.resizable(0,0)


btn7 = Button(root,text='7',width=5,height=1,command=lambda:call_digit(7))
btn7.grid(row=1,column=0,padx=0,pady=0)
btn7.config(font=('verdana',14))

btn8 = Button(root,text='8',width=5,height=1,command=lambda:call_digit(8))
btn8.grid(row=1,column=1,padx=0,pady=0)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9',width=5,height=1,command=lambda:call_digit(9))
btn9.grid(row=1,column=2,padx=0,pady=0)
btn9.config(font=('verdana',14))

btn_add = Button(root,text='+',width=5,height=1)
btn_add.grid(row=1,column=3,padx=0,pady=0)
btn_add.config(font=('verdana',14))


btn4 = Button(root,text='4',width=5,height=1,command=lambda:call_digit(4))
btn4.grid(row=2,column=0,padx=0, pady=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5',width=5,height=1,command=lambda:call_digit(5))
btn5.grid(row=2,column=1,padx=0, pady=0)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6',width=5,height=1,command=lambda:call_digit(6))
btn6.grid(row=2,column=2,padx=0, pady=0)
btn6.config(font=('verdana',14))

btn_sub = Button(root,text='-',width=5,height=1)
btn_sub.grid(row=2,column=3,padx=0, pady=0)
btn_sub.config(font=('verdana',14))

btn1 = Button(root,text='1',width=5,height=1,command=lambda:call_digit(1))
btn1.grid(row=3,column=0,padx=0, pady=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2',width=5,height=1,command=lambda:call_digit(2))
btn2.grid(row=3,column=1,padx=0, pady=0)
btn2.config(font=('verdana',14))

btn3 = Button(root,text='3',width=5,height=1,command=lambda:call_digit(3))
btn3.grid(row=3,column=2,padx=0, pady=0)
btn3.config(font=('verdana',14))

btn_multi = Button(root,text='*',width=5,height=1)
btn_multi.grid(row=3,column=3,padx=0, pady=0)
btn_multi.config(font=('verdana',14))

btn_c = Button(root,text='C',width=5,height=1)
btn_c.grid(row=4,column=0,padx=0, pady=0)
btn_c.config(font=('verdana',14))

btn0 = Button(root,text='0',width=5,height=1,command=lambda:call_digit(0))
btn0.grid(row=4,column=1,padx=0, pady=0)
btn0.config(font=('verdana',14))

btn_equal = Button(root,text='=',width=5,height=1)
btn_equal.grid(row=4,column=2,padx=0, pady=0)
btn_equal.config(font=('verdana',14))

btn_divide = Button(root,text='/',width=5,height=1)
btn_divide.grid(row=4,column=3,padx=0, pady=0)
btn_divide.config(font=('verdana',14))


root.mainloop()