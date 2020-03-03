from tkinter import *
from backend import database

db = database()

class interface:

    def get_selection(self,event):
        global selected_tuple
        index = box.curselection()[0]
        selected_tuple = box.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        

    def viewall_command(self):
        box.delete(0,END)
        for row in db.view():
            box.insert(END,row)

    def search_record(self):
        box.delete(0,END)
        for row in db.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
            box.insert(END,row)

    def add_record(self):
        box.delete(0,END)
        if db.search(isbn=isbn_text.get()) == []:
            if(title_text.get() != ""):
                db.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
                box.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
            else:
                box.insert(END,"Enter a book name to add.")
        else:
            box.insert(END,"The isbn already exists.")

    def update_record(self):
        db.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        box.delete(0,END)
        box.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

    def delete_record(self):
        db.delete(selected_tuple[0])
        self.viewall_command()

interface=interface()


window = Tk()

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

box = Listbox(window,height=6,width=35)
box.grid(row=2,column=0,rowspan=6,columnspan=2)
box.bind('<<ListboxSelect>>',interface.get_selection)

scroll1 = Scrollbar(window)
scroll1.grid(row=2,column=2,rowspan=6)

box.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=box.yview)

scroll2 = Scrollbar(window,orient="horizontal")
scroll2.grid(row=7,column=0,columnspan=2)

box.configure(xscrollcommand=scroll2.set)
scroll2.configure(command=box.xview)

b1 = Button(window,text="Search",width=13,command=interface.search_record)
b1.grid(row=2,column=3)

b2 = Button(window,text="Add",width=13,command=interface.add_record)
b2.grid(row=3,column=3)

b3 = Button(window,text="View All",width=13,command=interface.viewall_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update",width=13,command=interface.update_record)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=13,command=interface.delete_record)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=13,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
