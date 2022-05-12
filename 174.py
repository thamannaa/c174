from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

root=Tk()
root.title("rdonalds")
root.geometry("900x500")
burger=ImageTk.PhotoImage(Image.open("burger1.png"))

label_image=Label(root)
label_image.place(relx=0.7,rely=0.5,anchor=CENTER)
label_image["image"]=burger
label_head=Label(root,text="RDonalds",font=("times",40,"bold"),fg="orange")
label_head.place(relx=0.12,rely=0.1,anchor=CENTER)
label_select_dish=Label(root,text="select dish",font=("times",15))
label_select_dish.place(relx=0.06,rely=0.2,anchor=CENTER)
label_select_addons=Label(root,text="select addons",font=("times",15))
label_select_addons.place(relx=0.08,rely=0.5,anchor=CENTER)
dish=["burger","iced-americano"]
toppings=[]
dish_drop=ttk.Combobox(root,state="readonly",values=dish)
dish_drop.place(relx=0.25,rely=0.2,anchor=CENTER)
toppings_drop=ttk.Combobox(root,state="readonly",values=toppings)
toppings_drop.place(relx=0.25,rely=0.5,anchor=CENTER)
dish_amount=Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2,rely=0.75,anchor=CENTER)



class parent():
    def __init__(self):
        print("this is a parent class")
        
    def menu(dish):
        if dish=="burger":
            toppings=["cheese","jalepeeno"]
            toppings_drop["values"]=toppings
            print("you can add the following toppings")
            print("you can add cheese|jalepeeno")
        elif dish=="iced-americano":
            toppings=["chocolate","caramel"]
            toppings_drop["values"]=toppings
            print("you can add followings toppings")
            print("you can add chocolate|caramel")
        else:
            print("enter a valid dish")
            
    def final_amount(dish,addons):
        if dish=="burger" and addons=="cheese":
            dish_amount["text"]="you have to pay 250 USD"
        elif dish=="burger" and addons=="jalepeeno":
            dish_amount["text"]="you have to pay 350 USD"
        elif dish=="iced-americano" and addons=="chocolate":
            dish_amount["text"]="you have to pay 450 USD"
        elif dish=="iced-americano" and addons=="caramel":
            dish_amount["text"]="you have to pay 550 USD"
            
class child1(parent):
    def __init__(self,dish):
        self.new_dish=dish
        
    def get_menu(self):
        new_dish=dish_drop.get()
        parent.menu(new_dish)
        
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish=dish
        self.new_addons=addons
        
    def get_final_amount(self):
        new_dish=dish_drop.get()
        new_addons=toppings_drop.get()
        parent.final_amount(new_dish,new_addons)
        
obj_child1=child1(dish_drop.get())
obj_child1.get_menu()
obj_child2=child2(dish_drop.get(),toppings_drop.get())
obj_child2.get_final_amount()
        
btn_addons=Button(root,text="check addons",bg="blue",fg="white",relief=FLAT,command=obj_child1.get_menu)  
btn_addons.place(relx=0.06,rely=0.3,anchor=CENTER)
btn_amount=Button(root,text="amount",bg="blue",fg="white",relief=FLAT,command=obj_child2.get_final_amount)  
btn_amount.place(relx=0.04,rely=0.6,anchor=CENTER)
            
root.mainloop()      
           
    
