import os
import re
from tkinter import *
from tkinter.ttk import *
import getpass

def get_text(a):
    if(len(a)>9):
        return a[0:9]+"..."
    else:
        return a    


x=1
y=1
def open_file(a):

    os.system("xdg-open "+a)
def go_back(path):
    var=path.split("/")
    var.pop()
    st="/".join(var)
    
    return st

def is_file(chaine):
    if(chaine.startswith(".")):
        return False
    if(re.findall("(.)*(\.)(.)*",chaine)):
        return True
    else :
        return False

tab=dict()
var=os.listdir('.')
for a in var:
   
    tab[a]=os.path.abspath(a)

def open_list(arg1):
    tab2=dict()
    for a in os.listdir(os.path.abspath(arg1)):
        
        tab2[a]=os.path.abspath(arg1)+"/"+a



    for widget in f.winfo_children():
        widget.destroy()
    x=1
    y=1    

    btn=Button(f,text="go back",image=photo2,compound=TOP,command=lambda arg1=go_back(os.path.abspath(arg1)):open_list(arg1))
    btn2=Button(f,text="Bureau",image=photo4,compound=TOP,command=lambda arg1="/home/"+str(getpass.getuser())+"/Bureau":open_list(arg1))
    btn.grid(column=0, row=0,padx=10, pady=10)
    lb=Label(f,text="current : "+os.path.abspath(arg1))
    btn2.grid(column=1, row=0,padx=10, pady=10)
    lb.grid(column=2,row=0,padx=10, pady=10)
 
  
    for a in tab2:
      if(is_file(a)==False):  
        btn = Button(f, text=get_text(a),image=photo, compound=TOP,command=lambda arg1=tab2[a] : open_list(arg1))
      else:
        btn = Button(f, text=get_text(a), image=photo3,compound=TOP,command=lambda arg1=tab2[a] : open_file(arg1))
            
      btn.grid(column=x, row=y,padx=5, pady=5)
      y+=1
      if(y>=10):
          y=1
          x+=1  




        
root = Tk()
scroll_bar = Scrollbar(root) 
  
scroll_bar.pack( side = RIGHT, fill = Y )

f=Listbox(root,yscrollcommand = scroll_bar.set)
f.pack(side=LEFT,fil=BOTH)

scroll_bar.config( command = f.yview ) 




photo = PhotoImage(file ="image.png") 
photo=photo.subsample(4,10) 

photo2 = PhotoImage(file ="back.png") 
photo2=photo2.subsample(4,10) 

photo3 = PhotoImage(file ="file.png") 
photo3=photo3.subsample(4,10) 

photo4 = PhotoImage(file ="desk.png") 
photo4=photo4.subsample(4,10) 

root.config(bg="grey")
root.wm_title("File explorer")
btn=Button(f,text="go back",image=photo2,compound=TOP,command=lambda arg1=go_back(os.path.abspath('.')):open_list(arg1))
btn.grid(column=0, row=0,padx=10, pady=10)
btn2=Button(f,text="Bureau",image=photo4,compound=TOP,command=lambda arg1="/home/"+str(getpass.getuser())+"/Bureau":open_list(arg1))

lb=Label(f,text="current : "+os.path.abspath('.'))
btn2.grid(column=1, row=0,padx=10, pady=10)
lb.grid(column=2,row=0,padx=10, pady=10)

for a in tab:

    if(is_file(a)==False):
        btn = Button(f, text=get_text(a), image=photo,compound=TOP,command=lambda arg1=tab[a] : open_list(arg1))
    else:
        btn = Button(f, text=get_text(a), image=photo3,compound=TOP,command=lambda arg1=tab[a] : open_file(arg1))
        
    btn.grid(column=x, row=y,padx=5, pady=5)
    y+=1
    if(y>=10):
          y=1
          x+=1  

root.geometry("1320x720")
root.mainloop()
