from tkinter import *
def btnClick(number):
      global operator
      operator= operator + str(number)
      text_Input.set(operator)
def btnClear():
      global operator
      operator=""
      text_Input.set(operator)
def btnequal():
      global operator
      sumup=str(eval(operator))
      text_Input.set(sumup)
      operator=""

      
            
    
window= Tk()
window.title("calculator")
operator=""
text_Input= StringVar()
textDisplay = Entry(window, font=("arial", 20, "bold"), bd=50, textvariable=text_Input, insertwidth=4, bg='powder blue', justify="right")
textDisplay.grid(columnspan=4)
button7= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='7',command=lambda:btnClick(7))
button7.grid(row=1, column=0)
button8= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='8',command=lambda:btnClick(8))
button8.grid(row=1, column=1)
button9= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='9',command=lambda:btnClick(9))
button9.grid(row=1, column=2)
buttonadd= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='+',command=lambda:btnClick("+"))
buttonadd.grid(row=1, column=3)
################################
button4= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='4',command=lambda:btnClick(4))
button4.grid(row=2, column=0)
button5= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='5',command=lambda:btnClick(5))
button5.grid(row=2, column=1)
button6= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='6',command=lambda:btnClick(6))
button6.grid(row=2, column=2)
buttonsub= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='-',command=lambda:btnClick("-"))
buttonsub.grid(row=2, column=3)
################

button1= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='1',command=lambda:btnClick(1))
button1.grid(row=3, column=0)
button2= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("aria", 20, "bold"), text='2',command=lambda:btnClick(2))
button2.grid(row=3, column=1)
button3= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='3',command=lambda:btnClick(3))
button3.grid(row=3, column=2)
buttonmul= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='*',command=lambda:btnClick("*"))
buttonmul.grid(row=3, column=3)
####

button0= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='0',command=lambda:btnClick(0))
button0.grid(row=4, column=0)
buttoncnl= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("aria", 20, "bold"), text='C',command=btnClear)
buttoncnl.grid(row=4, column=1)
buttondiv= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='/',command=lambda:btnClick("/"))
buttondiv.grid(row=4, column=2)
buttoneq= Button(window, padx=16,pady=16, bd=8,bg='powder blue', fg="black", font=("arial", 20, "bold"), text='=',command=btnequal)
buttoneq.grid(row=4, column=3)




window.mainloop()