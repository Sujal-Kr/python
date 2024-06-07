# A function is used to remove the items from the list box is delete function .
# Get function is used to get the items that are selected in the list box.
# xview:The  function is used to display the horizontal scrollbar on the list box.
# yview:The function is used to display the vertical scrollbar on the list box

from tkinter  import *
def get_selected():
    print(list.get(list.curselection()))
top=Tk()
top.geometry("300x400")
label=Label(top,text="Famous Cricketers",foreground="red",)
list=Listbox(top)
list.insert(1,"Dhoni")
list.insert(2,"Sachin")
list.insert(3,"Virat")
list.delete(0)
list.xview()
label.pack()
list.pack()
btn=Button(top,command=get_selected,text="Click me")
btn.pack()
top.mainloop()


