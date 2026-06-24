from tkinter import *
from tkinter import messagebox

class  Simple_Calculator:
    def __init__(self,root):
        self.root=root
        self.root.title("simple_Calculator")
        self.root.geometry("400x525")
        self.root.configure(bg='grey50')
        self.root.wm_iconbitmap(r"C:\Users\dell\Downloads\3700465-business-calculating-calculator-finance-maths-technological_108748.ico")
        self.root.resizable(False, False)
        self.scvalue = StringVar()
        self.scvalue.set("")

        self.create_widget()
    def create_widget(self):
        display_frame=Frame(self.root,bg='grey18',height=80)
        display_frame.pack(fill='x',padx=0,pady=0,side=TOP  )
        self.display_result=Entry(display_frame,textvar=self.scvalue,font=('lucida',24),bg='darkgrey',fg='black',insertbackground='white',bd=0,highlightthickness=1,highlightbackground="gray30", highlightcolor="deep sky blue")
        self.display_result.place(x=20, y=9, width=300, height=60)
        free_space=Label(display_frame,bg='grey18',fg='dark slate grey',text='🖋️',font=('Helvicta',34))
        free_space.place(x=340, y=16, width=100, height=35)

        Button_Frame=Frame(self.root,bg='grey33',height=500)
        Button_Frame.pack(fill='both',padx=0,pady=0)

        Button_0=Button(Button_Frame,text='0',font=("Helvetica", 40, "bold"),bg="grey33",fg="black",bd=0,padx=13,activebackground='dark slate grey')
        Button_1 = Button(Button_Frame, text='1', font=("Helvetica", 40, "bold"),bg="grey33", fg="black",activebackground='dark slate grey', bd=0,padx=13)
        Button_2 = Button(Button_Frame, text='2',font=("Helvetica", 40, "bold"), bg="grey33", fg="black",activebackground='dark slate grey', bd=0,padx=13)
        Button_backspace = Button(Button_Frame, text='🔙',font=("Helvetica", 40, "bold"), bg="grey33", fg="black",activebackground='dark slate grey', bd=0, padx=1)

        Button_3 = Button(Button_Frame, text='3', font=("Helvetica", 40, "bold"),bg="grey33", fg="black",activebackground='dark slate grey', bd=0,padx=13)
        Button_4 = Button(Button_Frame, text='4',font=("Helvetica", 40, "bold"), bg="grey33", fg="black",activebackground='dark slate grey', bd=0,padx=13)
        Button_5 = Button(Button_Frame, text='5', font=("Helvetica", 40, "bold"),bg="grey33", fg="black",activebackground='dark slate grey', bd=0,padx=13)
        Button_add = Button(Button_Frame, text='+', font=("Helvetica", 43, "bold"),bg="grey33", fg="black",activebackground='dark slate grey', bd=0,padx=13)

        Button_6 = Button(Button_Frame, text='6',font=("Helvetica", 40, "bold"), bg="grey33", fg="black", bd=0,activebackground='dark slate grey', padx=1)
        Button_7 = Button(Button_Frame, text='7',font=("Helvetica", 40, "bold"), bg="grey33", fg="black", bd=0,activebackground='dark slate grey', padx=1)
        Button_8 = Button(Button_Frame, text='8',font=("Helvetica", 40, "bold"), bg="grey33", fg="black", bd=0,activebackground='dark slate grey',padx=13)
        Button_subtract = Button(Button_Frame, text='-', font=("Helvetica", 43, "bold"),bg="grey33", fg="black", bd=0,activebackground='dark slate grey',padx=13)
        Button_9 = Button(Button_Frame, text='9',font=("Helvetica", 40, "bold"), bg="grey33", fg="black", bd=0,activebackground='dark slate grey')
        Button_multiply = Button(Button_Frame, text='*',font=("Helvetica", 43, "bold"), bg="grey33", fg="black", bd=0,activebackground='dark slate grey', padx=13)
        Button_divide = Button(Button_Frame, text='/',font=("Helvetica", 40, "bold"), bg="grey33", fg="black", bd=0,activebackground='dark slate grey', padx=13)
        Button_evaluate = Button(Button_Frame, text='=', font=("Helvetica", 37, "bold"),bg="grey33", fg="black", bd=0,activebackground='dark slate grey',padx=13)

  #Arranging ans packing buttons

        Button_0.grid(row=0, column=0)
        Button_1.grid(row=0, column=1)
        Button_2.grid(row=0, column=2)
        Button_backspace.grid(row=0, column=3)

        Button_3.grid(row=1, column=0)
        Button_4.grid(row=1, column=1)
        Button_5.grid(row=1, column=2)
        Button_add.grid(row=1, column=3)

        Button_6.grid(row=2, column=0)
        Button_7.grid(row=2, column=1)
        Button_8.grid(row=2, column=2)
        Button_subtract.grid(row=2, column=3)

        Button_9.grid(row=3, column=0)
        Button_multiply.grid(row=3, column=1)
        Button_divide.grid(row=3, column=2)
        Button_evaluate.grid(row=3, column=3)

    #Binding Buttons with events
        Button_0.bind("<Button-1>",self.click)
        Button_1.bind("<Button-1>", self.click)
        Button_2.bind("<Button-1>", self.click)
        Button_3.bind("<Button-1>", self.click)
        Button_4.bind("<Button-1>", self.click)
        Button_5.bind("<Button-1>", self.click)
        Button_6.bind("<Button-1>", self.click)
        Button_7.bind("<Button-1>", self.click)
        Button_8.bind("<Button-1>", self.click)
        Button_9.bind("<Button-1>", self.click)
        Button_multiply.bind("<Button-1>", self.click)
        Button_divide.bind("<Button-1>", self.click)
        Button_evaluate.bind("<Button-1>", self.click)
        Button_add.bind("<Button-1>", self.click)
        Button_subtract.bind("<Button-1>", self.click)
        Button_backspace.bind("<Button-1>",self.click)

    def click(self,event):
        text=event.widget.cget("text")
        if text=="=":
            if self.scvalue.get().isdigit():
                value=int(self.scvlaue.get())
            else:
                try:
                    value=eval(self.display_result.get())
                except Exception as e:
                    print("Error")
                    value="Error"
            self.scvalue.set(value)
            self.display_result.update()
        elif text=="🔙":
            value=self.display_result.get()
            new_value=value[0:-1]
            self.scvalue.set(new_value)
            self.display_result.update()
        else:
            self.scvalue.set(self.scvalue.get()+text)
            self.display_result.update()





if __name__=='__main__':
    window=Tk()
    app=Simple_Calculator(window)

    window.mainloop()











