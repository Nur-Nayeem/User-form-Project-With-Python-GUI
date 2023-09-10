from tkinter import *

root=Tk()
root.title("User Form")
root.geometry("600x500+400+100")
root.resizable(False,False)
lvl=Label(root,text="User Entry Form",font=("times new roman",25,"bold"),bg="lightblue").place(relwidth=1)

def get_data():
    if var_name.get()=="" or var_email.get()=="":
        lvl_result.config(text="Please Fill the Name and Email block")
    else:
        if var_chk.get()==1:
            result="USER NAME: "+var_name.get()+"\n EMAIL: "+var_email.get()+"\n GENDER: "+var_gnder.get()
            lvl_result.config(text=str(result))
        else:
            lvl_result.config(text="Please Accept the turm and conditions")
        
    
    

username=Label(root,text="User Name",font=("times new roman",20)).place(x=20,y=60)
email=Label(root,text="Email",font=("times new roman",20)).place(x=20,y=120)
gender=Label(root,text="Gender",font=("times new roman",20)).place(x=20,y=180)

var_name=StringVar()
var_email=StringVar()
var_gnder=StringVar()
var_chk=IntVar()
usertxt=Entry(root,textvariable=var_name,font=("times new roman",20,"")).place(x=180,y=60,relwidth=0.6) # we can use width in relwidth
emailtxt=Entry(root,textvariable=var_email,font=("times new roman",20,"")).place(x=180,y=120,relwidth=0.6)
maleslct=Radiobutton(root,variable=var_gnder,text="Male",value="male",font=("times new roman",20)).place(x=180,y=180)
femaleslct=Radiobutton(root,variable=var_gnder,text="Female",value="female",font=("times new roman",20)).place(x=280,y=180)
var_gnder.set("male")
chk=Checkbutton(root,variable=var_chk,text="Accept the turm and conditions",onvalue=1,offvalue=0,font=("times new roman",15)).place(x=180,y=240)
# var_chk.set()
btn=Button(root,text="Submit",font=("times new roman",30),bg="gray",fg="white",command=get_data).place(x=210,y=300,height=40)
lvl_result=Label(root,font=("times new roman",20))
lvl_result.place(x=0,y=380,relwidth=1)

root.mainloop()