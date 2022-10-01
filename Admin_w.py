#from log_in import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser
import datetime
from time import strftime 
from display_p3 import bill_dis
  
#main_w()

#button image
def bill_create():
    #fuction time date
    def time(): 

        string = strftime('%H:%M:%S %p') 
        e.config(text = string) 
        e.after(1000, time)
        
    def date():
        e.datetime.date.now()
        
    root2 = Tk()

    #window configuration
    root2.title("UNICORN SUPER STORE")
    root2.geometry("1350x700+0+0")
    root2.iconbitmap("fevicon1.ico")
    root2.configure(background='#aa92fa')

    def logout():
        root2.destroy();

    #Developer 19124018 (JOY PATEL) & 19124021 (KHUSHAL GOYAL)
    #frame for header
    
    """logo = ImageTk.PhotoImage(Image.open("unilogo_.png"))
    imglogo = Label(root2,image=logo,bg="#aa92fa")
    imglogo.pack()"""
    header = LabelFrame(root2,borderwidth=0,width=1300 ,bg="#aa92fa",fg="black")
    header.pack()

    namecomp = Label(header, text="UNICORN SUPER STORE",font=("Arial black",40,"bold"), bg="#aa92fa",fg="black",width=1300)
    namecomp.pack(side=TOP)


    subname = Label(header, text="FIND EVERYTHING, ANYTHING YOU WANT....",font=("ink free",15),bg="#aa92fa",fg="black")
    subname.pack()

    e = Label(header, font = ('Arial', 15), bg = '#aa92fa', fg = 'purple')
    e.pack(side=TOP)
    print("khushal")


    #frame for str and buttons
    complex_ = LabelFrame(root2,borderwidth=0,width=1300 ,bg="#aa92fa",fg="black")
    complex_.pack()

    space_5 = Label(complex_, text="",font=("Arial", 20), bg="#aa92fa" )
    space_5.pack()

    str_magic = Label(complex_, text="Welcome JOY & KHUSHAL",font=("Arial",15), bg="#aa92fa",fg="black",width=1300)
    str_magic.pack(side=TOP)


    #button image
    photo = PhotoImage(file = r"log_out.png")
    photo1 = photo.subsample(1, 1)

    log_out = Button(complex_, text=" Log Out ",borderwidth=2, font=("Arial",13), bg="#e3bffd",fg="black",image=photo1,compound = LEFT,command=logout)
    log_out.pack(side=RIGHT,padx=10)

    space_6 = Label(complex_, text=" ",font=("Arial", 20), bg="#aa92fa" )
    space_6.pack(side=RIGHT)

    p_bill = Button(complex_, text="Previous Bill",borderwidth=2, font=("Arial",13), bg="#e3bffd",fg="black")
    p_bill.pack(side=RIGHT)
    #variable for input
    src=StringVar();
    quan=StringVar();

    def back_search():
        f = open("database.txt", "w");
        f.write("\n09873-Maggi[0345]-90");
        f.write("\n09874-Towel[9845]-39");
        f.write("\n09876-Bucket[8975]-49");
        f.write("\n09877-Fruits[2345]-67");
        f.write("\n09878-Stationary[0989]-89");
        f.write("\n09879-Books[0989]-67");
        f.write("\n09880-Utensils[2388]-43");
        f.write("\n09881-cloths[2312]-78");
        f.close();
        k="";
        v="";
        z=0;
        #open and read the file after the appending:
        num=src.get();
        search = open("database.txt")
        for i in search:
            if num in i:
                opl_lbl.insert(END,i);
                lbl_display.insert(END,i);
                z=1;
        if(z==0):
            opl_lbl.insert(END,"The product is not available.");
            lbl_display.insert(END,"The product is not available.");
        
    def searc_clear():
        opl_lbl.delete(1.0,END);
        lbl_display.delete(1.0,END);
        total=0.0;

    def Addtocart():
        k="";
        v="";
        z=0;
        global total;
        #open and read the file after the appending:
        num=src.get();
        quantity=quan.get();
        search = open("database.txt")
        for i in search:
            if num in i:
                mn=i.split("-");
                productp=float(mn[2]);
                q=float(quantity);
                price=q*productp;
                total=price;
                lbl_display.insert(END,total);
                lbl_display.insert(END,"\n");
                return total;

   


    #frame main
    mainfrm = LabelFrame(root2,borderwidth=0 ,bg="#aa92fa",fg="black")
    mainfrm.pack(side=LEFT, fill=Y,expand=TRUE)

    searchlbl = Label(mainfrm, text="Search Product : ", font=("Arial",15), bg="#aa92fa",fg="black")
    searchlbl.grid(row=0, column=3,padx= 10,pady=10)

    #space_7 = Label(mainfrm, text=" ",font=("Arial", 20), bg="#aa92fa" )
    #space_7.grid(row=0,column=3,padx= 5,pady=5)

    enter_search_lbl = Entry(mainfrm, bd=5,borderwidth=1,width= 50, textvariable=src)
    enter_search_lbl.grid(row=0, column=4,padx= 10,pady=10,ipady=4)

    space_9 = Label(mainfrm, text=" ",font=("Arial", 20), bg="#aa92fa" )
    space_9.grid(row=0,column=5,padx= 5,pady=5)


    photo2 = PhotoImage(file = r"search_edit.png")
    photo3 = photo2.subsample(1, 1)


    src_btn = Button(mainfrm, text=" Search",borderwidth=2, font=("Arial",13), bg="#e3bffd",fg="black",width=100,image=photo3,compound = LEFT,command=back_search)
    src_btn.grid(row=0, column=6,padx= 10,pady=10)

    opl_lbl = Text(mainfrm, bd=5,borderwidth=1, height=2,width= 60)
    opl_lbl.grid(columnspan=6, padx= 10,pady=10)

    photo4 = PhotoImage(file = r"romove_edit.png")
    photo5 = photo4.subsample(1, 1)

    remove_btn = Button(mainfrm, text=" Remove",borderwidth=2, font=("Arial",13), bg="#e3bffd",fg="black",width=100,image=photo5,compound = LEFT,command=searc_clear)
    remove_btn.grid(row=1,column=6,padx= 10,pady=10)

    space_10 = Label(mainfrm, text=" ",font=("Arial", 20), bg="#aa92fa" )
    space_10.grid(row=2,column=2,padx= 5,pady=5)

    quantity_lbl = Label(mainfrm, text="Quantity : ", font=("Arial",15), bg="#aa92fa",fg="black")
    quantity_lbl.grid(row=3,column=3,padx= 10,pady=10)

    enter_quantity_lbl = Entry(mainfrm, bd=5,borderwidth=1, width= 20,textvariable=quan)
    enter_quantity_lbl.grid(row=3, column=4,padx= 10,pady=10,ipady=9)

    #space_11 = Label(mainfrm, text=" ",font=("Arial", 20), bg="#aa92fa" )
    #space_11.grid(row=4,column=2,padx= 5,pady=5)


    photo6 = PhotoImage(file = r"cart_edit.png")
    photo7 = photo6.subsample(1, 1)

    display_btn = Button(mainfrm, text="  Add To Cart",borderwidth=2, font=("Arial",13), bg="#e3bffd",fg="black",width=150,image=photo6,compound = LEFT,command=lambda:[Addtocart()])
    display_btn.grid(columnspan=7,padx= 10,pady=10)


    photo9 = PhotoImage(file = r"generatebill_edit.png")
    photo10 = photo9.subsample(1, 1)

    final_btn = Button(mainfrm, text="  Generate Bill",borderwidth=2, font=("Arial",20), bg="#e3bffd",fg="black",width=300,image=photo10,compound = LEFT,command=lambda:[bill_dis()])
    final_btn.grid(columnspan=7,padx= 10,pady=10)
    
    ###########################CHECK BOX##########################################

    pay_opt = Label(mainfrm, text="Payment Options", font=("Arial",15,"bold"), bg="#aa92fa",fg="black")
    pay_opt.grid(columnspan=7)
    #row=7,column=3,padx= 10,pady=10
    pay = IntVar()
    
    Radiobutton(mainfrm, text="VISA Card", variable=pay, bg="#aa92fa",fg="black", value=1).grid(columnspan=7)
    
    Radiobutton(mainfrm, text="Credit/Debit Card", variable=pay, bg="#aa92fa",fg="black", value=2).grid(columnspan=7)
    #row = 8,column=4
    Radiobutton(mainfrm, text="Master Card", variable=pay, bg="#aa92fa",fg="black", value=3).grid(columnspan=7)
    
    Radiobutton(mainfrm, text="BHIM UPI", variable=pay, bg="#aa92fa",fg="black", value=4).grid(columnspan=7)
    

    #frame display
    display = LabelFrame(root2,borderwidth=9 ,bg="#aa92fa",fg="black",width= 90)
    display.pack()
    
    lbl_display = Text(display, bd=5,borderwidth=10,width= 90,relief=RIDGE)
    lbl_display.pack()







    #frame for footer
    footer = LabelFrame(root2,borderwidth=0,bg="#aa92fa",fg="black")
    footer.pack(side=BOTTOM)



    

    """space_12 = Label(footer, text=" ",font=("Arial", 20), bg="#aa92fa" )
    space_12.pack(side=BOTTOM)"""

    footinfo = Label(footer, text="Developed by KJ Developers (All Terms And Condition Are Reserved Under Rights 2020)",font=("Arial",10),bg="#aa92fa",fg="black",width=1300)
    footinfo.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

    
    time() 
    mainloop()
bill_create();







